# Problem 3.4: Supersonic Transport Nozzle

**Problem Statement:**
A supersonic transport has a convergent-divergent nozzle. At takeoff, the nozzle operates fully expanded with an exit Mach number $M_e = 1.5$. The ambient pressure and temperature are $P_a = 101 \, kPa$ and $T_a = 288 \, K$. The nozzle exit area is $A_e = 0.6 \, m^2$. Calculate the nozzle throat area $A_t$ and the static pressure $P_e$, static temperature $T_e$, and density $\rho_e$ at the exit. Assume $\gamma = 1.4$ and $R = 287 \, J/(kg \cdot K)$.

**Assumptions:**
*   Convergent-divergent nozzle.
*   Operating fully expanded at takeoff: This means the exit pressure $P_e$ equals the ambient pressure $P_a$.
*   Isentropic flow through the nozzle (ideal nozzle).
*   Air as the working fluid, ideal gas with $\gamma = 1.4$ and $R = 287 \, J/(kg \cdot K)$.
*   Stagnation conditions ($P_0, T_0$) refer to conditions inside the engine just before the nozzle.

**Objective:**
Calculate $A_t$, $P_e$, $T_e$, $\rho_e$.

**Step-by-Step Calculation (Hand-Calculable):**

1.  **Exit Static Pressure ($P_e$):**
    The nozzle operates fully expanded, meaning the exit pressure matches the ambient pressure.
    $$ P_e = P_a = 101 \, kPa = \mathbf{101000 \, Pa} $$ 

2.  **Stagnation Pressure ($P_0$):**
    We use the isentropic relation between static and stagnation pressure, knowing $M_e = 1.5$ and $P_e$.
    $$ \frac{P_e}{P_0} = \left( 1 + \frac{\gamma-1}{2} M_e^2 \right)^{-\frac{\gamma}{\gamma-1}} $$ 
    $$ \frac{P_e}{P_0} = \left( 1 + \frac{1.4-1}{2} (1.5)^2 \right)^{-\frac{1.4}{1.4-1}} = (1 + 0.2 \times 2.25)^{-3.5} = (1 + 0.45)^{-3.5} = (1.45)^{-3.5} $$ 
    Using standard isentropic flow tables or a calculator for $M=1.5$ ($\\gamma=1.4$):
    $$ \frac{P_e}{P_0} \approx 0.27240 $$ 
    Therefore, the stagnation pressure required is:
    $$ P_0 = \frac{P_e}{0.27240} = \frac{101000 \, Pa}{0.27240} \approx 370778 \, Pa \approx 370.8 \, kPa $$ 

3.  **Exit Static Temperature ($T_e$):**
    The problem does not provide the stagnation temperature $T_0$. However, the ambient temperature $T_a = 288 \, K$ is given. A common interpretation in such problems, especially when fully expanded conditions are specified matching ambient pressure, is that the exit static temperature might also match the ambient temperature if the flow has adjusted fully. Let's assume $T_e = T_a$ based on this interpretation.
    $$ T_e = T_a = \mathbf{288 \, K} $$ 
    *(Note: If this assumption is incorrect, $T_e$ cannot be determined without knowing $T_0$. If $T_e = T_a$ is assumed, it implies a specific $T_0$.)*
    We can find the implied $T_0$ using the isentropic relation:
    $$ \frac{T_e}{T_0} = \left( 1 + \frac{\gamma-1}{2} M_e^2 \right)^{-1} = (1.45)^{-1} \approx 0.68966 $$ 
    Implied $T_0 = \frac{T_e}{0.68966} = \frac{288 \, K}{0.68966} \approx 417.6 \, K$.

4.  **Exit Density ($\rho_e$):**
    Using the ideal gas law at the exit conditions ($P_e, T_e$):
    $$ \rho_e = \frac{P_e}{R T_e} $$ 
    $$ \rho_e = \frac{101000 \, Pa}{(287 \, J/(kg \cdot K))(288 \, K)} = \frac{101000}{82656} \approx \mathbf{1.2219 \, kg/m^3} $$ 

5.  **Throat Area ($A_t = A^*$):**
    We need the isentropic area ratio $A_e / A^*$ for $M_e = 1.5$.
    $$ \frac{A_e}{A^*} = \frac{1}{M_e} \left[ \frac{1 + \frac{\gamma-1}{2} M_e^2}{\frac{\gamma+1}{2}} \right]^{\frac{\gamma+1}{2(\gamma-1)}} $$ 
    $$ \frac{A_e}{A^*} = \frac{1}{1.5} \left[ \frac{1 + 0.2(1.5)^2}{\frac{1.4+1}{2}} \right]^{\frac{1.4+1}{2(1.4-1)}} = \frac{1}{1.5} \left[ \frac{1.45}{1.2} \right]^{\frac{2.4}{0.8}} = \frac{1}{1.5} [1.20833]^{3.0} $$ 
    Using standard isentropic flow tables or a calculator for $M=1.5$ ($\\gamma=1.4$):
    $$ \frac{A_e}{A^*} \approx 1.1762 $$ 
    The throat area $A_t = A^*$ is:
    $$ A_t = A^* = \frac{A_e}{1.1762} = \frac{0.6 \, m^2}{1.1762} \approx \mathbf{0.5101 \, m^2} $$ 

**Summary of Results:**
*   Exit Static Pressure: $P_e = \mathbf{101 \, kPa}$
*   Exit Static Temperature: $T_e = \mathbf{288 \, K}$ (Based on interpretation $T_e=T_a$)
*   Exit Density: $\rho_e \approx \mathbf{1.222 \, kg/m^3}$
*   Throat Area: $A_t \approx \mathbf{0.510 \, m^2}$

**Equations Used:**
*   Fully Expanded Condition: $P_e = P_a$
*   Isentropic Pressure Ratio: $P/P_0 = (1 + \frac{\gamma-1}{2} M^2)^{-\gamma/(\gamma-1)}$
*   Isentropic Temperature Ratio: $T/T_0 = (1 + \frac{\gamma-1}{2} M^2)^{-1}$
*   Ideal Gas Law: $P = \rho R T$
*   Isentropic Area Ratio: $A/A^* = \frac{1}{M} [\frac{1 + \frac{\gamma-1}{2} M^2}{(\gamma+1)/2}]^{\frac{\gamma+1}{2(\gamma-1)}}$
