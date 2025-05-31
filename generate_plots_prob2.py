# Python script to calculate and plot results for Problem 2.1 and 2.2
# AER-4027 Problem Sheet

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import pandas as pd

# Constants
GAMMA = 1.4
GAMMA_P1 = GAMMA + 1
GAMMA_M1 = GAMMA - 1
R = 287.0 # J/(kg.K) - Not needed for ratios, but good practice

# --- Isentropic Flow Functions ---
def area_ratio(M, gamma=GAMMA):
    """ Calculates A/A* for a given Mach number M and gamma """
    if M < 1e-9:
        return np.inf
    term1 = 2 / (gamma + 1)
    term2 = 1 + (gamma - 1) / 2 * M**2
    return (1 / M) * (term1 * term2)**((gamma + 1) / (2 * (gamma - 1)))

def pressure_ratio(M, gamma=GAMMA):
    """ Calculates P/P0 for a given Mach number M and gamma """
    return (1 + (gamma - 1) / 2 * M**2)**(-gamma / (gamma - 1))

def temperature_ratio(M, gamma=GAMMA):
    """ Calculates T/T0 for a given Mach number M and gamma """
    return (1 + (gamma - 1) / 2 * M**2)**(-1)

def mach_from_area_ratio(AR, gamma=GAMMA, subsonic=True):
    """ Calculates Mach number M from A/A* ratio (AR) """
    if AR < 1.0:
        raise ValueError("Area ratio must be >= 1")
    if AR == 1.0:
        return 1.0

    # Function whose root is M
    def func(M): 
        return area_ratio(M, gamma) - AR

    try:
        if subsonic:
            # Search for subsonic root between 0 and 1
            M_sol = brentq(func, 1e-9, 1.0 - 1e-9) 
        else:
            # Search for supersonic root between 1 and a large number (e.g., 10)
            M_sol = brentq(func, 1.0 + 1e-9, 10.0)
    except ValueError: # Handle cases where root might not be found in interval
        M_sol = np.nan 
    return M_sol

def mach_from_pressure_ratio(PR, gamma=GAMMA):
    """ Calculates Mach number M from P/P0 ratio (PR) """
    if PR > 1.0 or PR <= 0:
         # P/P0 must be between 0 and 1
         # Handle P/P0=1 separately as it gives M=0
        if PR == 1.0:
            return 0.0
        else: # Invalid pressure ratio
            raise ValueError("Pressure ratio must be (0, 1]")
    
    term = (PR**(-(gamma - 1) / gamma) - 1) * (2 / (gamma - 1))
    if term < 0: # Should not happen for valid PR
        return np.nan
    return np.sqrt(term)

# --- Normal Shock Functions ---
def normal_shock_mach(M1, gamma=GAMMA):
    """ Calculates M2 downstream of a normal shock given M1 """
    if M1 <= 1.0:
        # print(f"Warning: Normal shock requires M1 > 1. Got M1={M1}")
        return M1 # No shock
    num = M1**2 + 2 / (gamma - 1)
    den = (2 * gamma / (gamma - 1)) * M1**2 - 1
    if den <= 0: return np.nan # Avoid division by zero or sqrt of negative
    return np.sqrt(num / den)

def normal_shock_pressure_ratio(M1, gamma=GAMMA):
    """ Calculates P2/P1 across a normal shock given M1 """
    if M1 <= 1.0:
        return 1.0 # No pressure change if no shock
    return 1 + (2 * gamma / (gamma + 1)) * (M1**2 - 1)

def normal_shock_stagnation_pressure_ratio(M1, gamma=GAMMA):
    """ Calculates P02/P01 across a normal shock given M1 """
    if M1 <= 1.0:
        return 1.0 # No stagnation pressure loss if no shock
    term1_base = ((gamma + 1) * M1**2) / ((gamma - 1) * M1**2 + 2)
    term1 = term1_base**(gamma / (gamma - 1))
    term2_base = (gamma + 1) / (2 * gamma * M1**2 - (gamma - 1))
    term2 = term2_base**(1 / (gamma - 1))
    return term1 * term2

# --- Problem 2.1 Specifics ---
def nozzle_area(x):
    """ Area function A(x) for Problem 2.1 """
    return 11.9774 * x**2 - 15.4774 * x + 6.0

x_values = np.linspace(0, 1, 21) # x=0, 0.05, ..., 1.0
A_values = nozzle_area(x_values)
A_throat = np.min(A_values)
x_throat_idx = np.argmin(A_values)
x_throat = x_values[x_throat_idx]
A_star = A_throat # Since min area is 1.000 at x=0.646
A_inlet = A_values[0]
A_exit = A_values[-1]
AR_exit = A_exit / A_star

# Calculate limiting conditions
M_exit_sub = mach_from_area_ratio(AR_exit, subsonic=True)
M_exit_sup = mach_from_area_ratio(AR_exit, subsonic=False)
P_exit_sub_ratio = pressure_ratio(M_exit_sub)
P_exit_sup_ratio = pressure_ratio(M_exit_sup)
P_shock_exit_ratio = normal_shock_pressure_ratio(M_exit_sup) * P_exit_sup_ratio

print(f"Problem 2.1 Geometry:")
print(f"  Throat Area A* = {A_star:.4f} at x = {x_throat:.4f}")
print(f"  Inlet Area A(0) = {A_inlet:.4f}, A/A* = {A_inlet/A_star:.4f}")
print(f"  Exit Area A(1) = {A_exit:.4f}, A/A* = {AR_exit:.4f}")
print(f"Limiting Pressure Ratios:")
print(f"  P_exit/P0 (Subsonic Isentropic Exit): {P_exit_sub_ratio:.4f} (M={M_exit_sub:.3f})")
print(f"  P_exit/P0 (Supersonic Isentropic Exit): {P_exit_sup_ratio:.4f} (M={M_exit_sup:.3f})")
print(f"  P_inf/P0 (Shock at Exit): {P_shock_exit_ratio:.4f}")

# Back pressures to analyze
P_inf_ratios = [1.0, 0.98, 0.97, 0.96085, 0.95, 0.9, 0.8, 0.7, 0.6, 0.5, 0.435, 0.4336, 0.4, 0.3, 0.2, 0.1, 0.04, 0.0]

results_mach = pd.DataFrame(index=x_values)
results_pressure = pd.DataFrame(index=x_values)
summary_data = []

# Calculate M(x) and P(x)/P0 for different P_inf/P0
for P_inf_P0 in P_inf_ratios:
    col_name = f"Pinf/P0={P_inf_P0:.4f}"
    M_x = np.zeros_like(x_values) * np.nan
    P_P0_x = np.zeros_like(x_values) * np.nan
    M_inlet, M_throat, M_exit, P_exit_P0 = np.nan, np.nan, np.nan, np.nan
    m_dot_param = 0.0
    shock_loc = np.nan

    if P_inf_P0 >= 1.0: # No flow
        M_x.fill(0.0)
        P_P0_x.fill(1.0)
        M_inlet, M_throat, M_exit, P_exit_P0 = 0.0, 0.0, 0.0, 1.0
        m_dot_param = 0.0

    elif P_inf_P0 > P_exit_sub_ratio: # Unchoked subsonic flow
        # Need to iterate to find M_throat < 1 that gives P_exit = P_inf
        def find_m_throat(m_thr):
            if m_thr >= 1.0: return 1e6 # Ensure M_throat < 1
            ar_thr = area_ratio(m_thr)
            a_star_hypo = A_throat / ar_thr
            ar_exit_hypo = A_exit / a_star_hypo
            m_exit_calc = mach_from_area_ratio(ar_exit_hypo, subsonic=True)
            p_exit_calc = pressure_ratio(m_exit_calc)
            return p_exit_calc - P_inf_P0
        
        try:
            M_throat = brentq(find_m_throat, 1e-9, 1.0 - 1e-9)
            A_star_hypo = A_throat / area_ratio(M_throat)
            for i, x in enumerate(x_values):
                AR_hypo = A_values[i] / A_star_hypo
                if i <= x_throat_idx:
                    M_x[i] = mach_from_area_ratio(AR_hypo, subsonic=True)
                else:
                    M_x[i] = mach_from_area_ratio(AR_hypo, subsonic=True) # Still subsonic
                P_P0_x[i] = pressure_ratio(M_x[i])
            M_inlet, M_exit, P_exit_P0 = M_x[0], M_x[-1], P_P0_x[-1]
            m_dot_param = np.sqrt(GAMMA) * M_throat * (1 + GAMMA_M1/2 * M_throat**2)**(-GAMMA_P1/(2*GAMMA_M1)) * (A_throat/A_star) # A_star=1
        except ValueError:
             print(f"Warning: Could not find M_throat for Pinf/P0={P_inf_P0}")
             M_x.fill(np.nan)
             P_P0_x.fill(np.nan)

    else: # Choked flow (P_inf_P0 <= P_exit_sub_ratio)
        M_throat = 1.0
        m_dot_param = np.sqrt(GAMMA) * (2 / GAMMA_P1)**(GAMMA_P1 / (2 * GAMMA_M1))
        P02_P01 = 1.0 # Assume no shock initially
        M_after_shock = np.nan

        # Calculate isentropic solution first
        M_isen = np.zeros_like(x_values)
        P_isen_P0 = np.zeros_like(x_values)
        for i, x in enumerate(x_values):
            AR = A_values[i] / A_star
            if i < x_throat_idx:
                M_isen[i] = mach_from_area_ratio(AR, subsonic=True)
            elif i == x_throat_idx:
                 M_isen[i] = 1.0
            else:
                M_isen[i] = mach_from_area_ratio(AR, subsonic=False)
            P_isen_P0[i] = pressure_ratio(M_isen[i])

        M_inlet = M_isen[0]
        P_exit_isen_sup = P_isen_P0[-1] # Should match P_exit_sup_ratio

        # Check for shock
        if P_inf_P0 >= P_exit_isen_sup: # Shock possible (inside or at exit)
            # Find shock location x_s such that P_exit matches P_inf
            def find_shock_loc(xs):
                if xs <= x_throat or xs > 1.0: return 1e6 # Shock must be in divergent part
                
                # Find M1 just before shock at xs by interpolation or recalculation
                AR_s = nozzle_area(xs) / A_star
                M1_shock = mach_from_area_ratio(AR_s, subsonic=False)
                if np.isnan(M1_shock) or M1_shock <= 1.0: return 1e6

                # Calculate conditions after shock
                M2_shock = normal_shock_mach(M1_shock)
                P02_P01_shock = normal_shock_stagnation_pressure_ratio(M1_shock)
                if np.isnan(M2_shock) or np.isnan(P02_P01_shock) or P02_P01_shock <=0: return 1e6

                # Required A_exit / A*_downstream for M2_shock to reach exit
                AR_exit_downstream = A_exit / (A_star / P02_P01_shock) # A*_downstream = A*_upstream / (P02/P01)
                
                # Find M_exit corresponding to this area ratio (subsonic)
                M_exit_calc = mach_from_area_ratio(AR_exit_downstream, subsonic=True)
                if np.isnan(M_exit_calc): return 1e6
                
                # Calculate P_exit based on P02
                P_exit_calc = pressure_ratio(M_exit_calc) * P02_P01_shock
                
                return P_exit_calc - P_inf_P0

            try:
                # Search only in the divergent section
                shock_loc = brentq(find_shock_loc, x_throat + 1e-6, 1.0 - 1e-9)
                # Recalculate M(x) and P(x)/P0 with shock
                AR_s = nozzle_area(shock_loc) / A_star
                M1_shock = mach_from_area_ratio(AR_s, subsonic=False)
                M_after_shock = normal_shock_mach(M1_shock)
                P02_P01 = normal_shock_stagnation_pressure_ratio(M1_shock)
                A_star_downstream = A_star / P02_P01

                for i, x in enumerate(x_values):
                    if x < shock_loc:
                        M_x[i] = M_isen[i]
                        P_P0_x[i] = P_isen_P0[i]
                    else:
                        AR_downstream = A_values[i] / A_star_downstream
                        M_x[i] = mach_from_area_ratio(AR_downstream, subsonic=True)
                        P_P0_x[i] = pressure_ratio(M_x[i]) * P02_P01
                M_exit = M_x[-1]
                P_exit_P0 = P_P0_x[-1]

            except ValueError: # No shock found inside, implies shock at exit or isentropic/over/under
                if abs(P_inf_P0 - P_shock_exit_ratio) < 1e-4: # Shock at exit
                    shock_loc = 1.0
                    M1_shock = M_exit_sup
                    M_after_shock = normal_shock_mach(M1_shock)
                    P02_P01 = normal_shock_stagnation_pressure_ratio(M1_shock)
                    M_x = M_isen.copy()
                    P_P0_x = P_isen_P0.copy()
                    M_exit = M_after_shock # Mach number just after exit shock
                    P_exit_P0 = P_inf_P0 # Pressure matches back pressure
                else: # Overexpanded (or Design) - Isentropic flow inside nozzle
                    M_x = M_isen.copy()
                    P_P0_x = P_isen_P0.copy()
                    M_exit = M_x[-1] # Isentropic supersonic exit Mach
                    P_exit_P0 = P_P0_x[-1] # Isentropic supersonic exit pressure
                    # Adjustment to P_inf happens outside

        else: # Underexpanded - Isentropic flow inside nozzle
            M_x = M_isen.copy()
            P_P0_x = P_isen_P0.copy()
            M_exit = M_x[-1]
            P_exit_P0 = P_P0_x[-1]
            # Adjustment to P_inf happens outside

    results_mach[col_name] = M_x
    results_pressure[col_name] = P_P0_x
    summary_data.append({
        "Pinf/P0": P_inf_P0,
        "M_inlet": M_inlet,
        "M_throat": M_throat,
        "M_exit": M_exit,
        "P_exit/P0": P_exit_P0,
        "m_dot_param": m_dot_param,
        "shock_loc": shock_loc
    })

summary_df = pd.DataFrame(summary_data)

# --- Plotting --- 
plt.style.use('seaborn-v0_8-notebook')

# 1. Nozzle Contour
plt.figure(figsize=(8, 4))
plt.plot(x_values, A_values, label='A(x)')
plt.plot(x_values, -A_values, label='-A(x)') # Symmetric
plt.plot([x_throat, x_throat], [A_star, -A_star], 'r--', label=f'Throat x={x_throat:.3f}')
plt.title('Problem 2.1: Nozzle Contour A(x)')
plt.xlabel('x')
plt.ylabel('Area per unit width A(x)')
plt.grid(True)
plt.ylim(-max(A_values)*1.1, max(A_values)*1.1)
plt.legend()
plt.tight_layout()
plt.savefig('/home/ubuntu/problem_2_1_contour.png')
plt.close()

# Select representative P_inf/P0 values for M(x) and P(x) plots
plot_cols_indices = [0, 1, 3, 6, 10, 12, 14, 16] # Indices for P_inf/P0 list
plot_cols = results_mach.columns[plot_cols_indices]

# 2. Mach Number vs x
plt.figure(figsize=(10, 6))
results_mach[plot_cols].plot(ax=plt.gca())
plt.title('Problem 2.1: Mach Number M vs x for various $P_{\infty}/P_0$')
plt.xlabel('x')
plt.ylabel('Mach Number M')
plt.grid(True)
plt.legend(title='$P_{\infty}/P_0$', fontsize='small')
plt.tight_layout()
plt.savefig('/home/ubuntu/problem_2_1_M_vs_x.png')
plt.close()

# 3. Pressure Ratio vs x
plt.figure(figsize=(10, 6))
results_pressure[plot_cols].plot(ax=plt.gca())
plt.title('Problem 2.1: Pressure Ratio $P/P_0$ vs x for various $P_{\infty}/P_0$')
plt.xlabel('x')
plt.ylabel('Pressure Ratio $P/P_0$')
plt.grid(True)
plt.legend(title='$P_{\infty}/P_0$', fontsize='small')
plt.tight_layout()
plt.savefig('/home/ubuntu/problem_2_1_P_vs_x.png')
plt.close()

# 4. Summary Plots vs P_inf/P0
summary_df_sorted = summary_df.sort_values(by='Pinf/P0')

fig, axs = plt.subplots(3, 2, figsize=(12, 12), sharex=True)
axs = axs.ravel()

plot_vars = ['m_dot_param', 'M_inlet', 'M_throat', 'M_exit', 'P_exit/P0', 'shock_loc']
y_labels = ['$\dot{m} \sqrt{RT_0}/(P_0 A^*)$', '$M_{inlet}$', '$M_{throat}$', '$M_{exit}$', '$P_{exit}/P_0$', 'Shock Location $x_s$']

for i, var in enumerate(plot_vars):
    axs[i].plot(summary_df_sorted['Pinf/P0'], summary_df_sorted[var], marker='o', linestyle='-')
    axs[i].set_ylabel(y_labels[i])
    axs[i].grid(True)
    if i >= 4: axs[i].set_xlabel('$P_{\infty}/P_0$')

fig.suptitle('Problem 2.1: Nozzle Performance Parameters vs. Back Pressure Ratio $P_{\infty}/P_0$')
plt.xlim(1.05, -0.05) # Reverse x-axis
plt.tight_layout(rect=[0, 0.03, 1, 0.97]) # Adjust layout to prevent title overlap
plt.savefig('/home/ubuntu/problem_2_1_summary_plots.png')
plt.close()

# --- Problem 2.2 Specifics ---
At = 0.0645 # m^2
P0 = 8 * 101325 # Pa
T0 = 470 # K

# Calculate critical pressure and max mass flow
P_crit_P0 = pressure_ratio(1.0, GAMMA)
P_crit = P_crit_P0 * P0
m_dot_choked_param = np.sqrt(GAMMA) * (2 / GAMMA_P1)**(GAMMA_P1 / (2 * GAMMA_M1))
m_dot_max = (P0 * At / np.sqrt(R * T0)) * m_dot_choked_param

print(f"\nProblem 2.2 Converging Nozzle:")
print(f"  P0 = {P0:.1f} Pa")
print(f"  T0 = {T0:.1f} K")
print(f"  At = {At:.4f} m^2")
print(f"  Critical P*/P0 = {P_crit_P0:.4f}")
print(f"  Critical Pb = {P_crit:.1f} Pa")
print(f"  Max mass flow rate = {m_dot_max:.2f} kg/s")

# Calculate m_dot for various Pb
Pb_ratios = np.linspace(1.0, 0.0, 101)
Pb_values = Pb_ratios * P0
m_dot_values = np.zeros_like(Pb_ratios)

for i, pb_ratio in enumerate(Pb_ratios):
    if pb_ratio >= P_crit_P0:
        # Unchoked
        Me = mach_from_pressure_ratio(pb_ratio, GAMMA)
        m_dot_param_i = np.sqrt(GAMMA) * Me * (1 + GAMMA_M1/2 * Me**2)**(-GAMMA_P1/(2*GAMMA_M1))
        m_dot_values[i] = (P0 * At / np.sqrt(R * T0)) * m_dot_param_i
    else:
        # Choked
        m_dot_values[i] = m_dot_max

# Plot m_dot vs Pb
plt.figure(figsize=(8, 5))
plt.plot(Pb_values, m_dot_values)
plt.axvline(P_crit, color='r', linestyle='--', label=f'Choked Flow $P_b \leq {P_crit/1000:.1f}$ kPa')
plt.title('Problem 2.2: Mass Flow Rate vs. Back Pressure for Converging Nozzle')
plt.xlabel('Back Pressure $P_b$ (Pa)')
plt.ylabel('Mass Flow Rate $\dot{m}$ (kg/s)')
plt.grid(True)
plt.legend()
plt.xlim(P0*1.05, -P0*0.05)
plt.ylim(-5, m_dot_max * 1.1)
plt.tight_layout()
plt.savefig('/home/ubuntu/problem_2_2_mdot_vs_Pb.png')
plt.close()

# Save data to files
results_mach.to_csv('/home/ubuntu/problem_2_1_mach_data.csv')
results_pressure.to_csv('/home/ubuntu/problem_2_1_pressure_data.csv')
summary_df.to_csv('/home/ubuntu/problem_2_1_summary_data.csv', index=False)
prob2_2_data = pd.DataFrame({'Pb_Pa': Pb_values, 'm_dot_kg_s': m_dot_values})
prob2_2_data.to_csv('/home/ubuntu/problem_2_2_data.csv', index=False)

print("\nPlots and data files generated for Problems 2.1 and 2.2.")


