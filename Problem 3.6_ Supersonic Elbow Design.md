# Problem 3.6: Supersonic Elbow Design

**Problem Statement:**
Design a supersonic elbow to turn a flow with an initial Mach number $M_1 = 2.5$ through an angle $\theta_{turn} = 20^\circ$. Describe the design and calculate the final Mach number $M_2$ and the ratios $P_2/P_1$ and $T_2/T_1$. Assume two-dimensional planar, isentropic flow of air with $\gamma = 1.4$.

**Approach:**
An isentropic supersonic turn is achieved using Prandtl-Meyer expansion waves. The elbow will consist of a convex corner that allows the flow to expand and turn.

**Assumptions:**
*   Steady, two-dimensional, planar flow.
*   Isentropic flow (no shocks, no friction).
*   Ideal gas with constant specific heats, $\gamma = 1.4$.

**Step-by-Step Calculation (Hand-Calculable):**

1.  **Calculate Initial Prandtl-Meyer Angle ($\\nu_1$):**
    We need the value of the Prandtl-Meyer function $\nu(M)$ for the initial Mach number $M_1 = 2.5$.
    The formula is:
    $$ \nu(M) = \sqrt{\frac{\gamma+1}{\gamma-1}} \arctan\left( \sqrt{\frac{\gamma-1}{\gamma+1}(M^2-1)} \right) - \arctan\left( \sqrt{M^2-1} \right) $$ 
    For $\gamma = 1.4$ and $M_1 = 2.5$:
    *   $\\sqrt{\frac{\gamma+1}{\gamma-1}} = \sqrt{\frac{2.4}{0.4}} = \sqrt{6} \approx 2.4495$
    *   $M_1^2 = 2.5^2 = 6.25$
    *   $\\sqrt{M_1^2-1} = \sqrt{5.25} \approx 2.2913$
    *   $\\sqrt{\frac{\gamma-1}{\gamma+1}(M_1^2-1)} = \sqrt{\frac{1}{6}(5.25)} = \sqrt{0.875} \approx 0.9354$
    *   $\\arctan(2.2913) \approx 66.42^\circ$
    *   $\\arctan(0.9354) \approx 43.09^\circ$
    $$ \nu_1 = \nu(2.5) = (2.4495)(43.09^\circ) - 66.42^\circ \approx 105.55^\circ - 66.42^\circ \approx 39.13^\circ $$ 

2.  **Calculate Final Prandtl-Meyer Angle ($\\nu_2$):**
    The flow turns through an expansion angle $\theta_{turn} = 20^\circ$. The Prandtl-Meyer function increases by this amount:
    $$ \nu_2 = \nu_1 + \theta_{turn} = 39.13^\circ + 20^\circ = 59.13^\circ $$ 

3.  **Calculate Final Mach Number ($M_2$):**
    We need to find the Mach number $M_2$ for which $\nu(M_2) = 59.13^\circ$. This typically requires solving the Prandtl-Meyer function implicitly or using standard gas tables.
    *   Using tables for $\gamma=1.4$:
        *   $\\nu(M=3.5) \approx 58.53^\circ$
        *   $\\nu(M=3.6) \approx 60.06^\circ$
    *   Linear interpolation:
        $$ M_2 \approx 3.5 + (3.6 - 3.5) \frac{59.13 - 58.53}{60.06 - 58.53} = 3.5 + 0.1 \frac{0.60}{1.53} \approx 3.5 + 0.1(0.392) \approx 3.539 $$ 
    So, the final Mach number is $M_2 \approx \mathbf{3.54}$.

4.  **Calculate Static Pressure Ratio ($P_2/P_1$):**
    Since the flow is isentropic, the stagnation pressure $P_0$ is constant. We use the isentropic pressure ratio $P/P_0 = (1 + \frac{\gamma-1}{2} M^2)^{-\gamma/(\gamma-1)}$.
    *   For $M_1 = 2.5$:
        $P_1/P_0 = (1 + 0.2 \times 2.5^2)^{-3.5} = (1 + 1.25)^{-3.5} = (2.25)^{-3.5} \approx 0.05853$
    *   For $M_2 = 3.54$:
        $P_2/P_0 = (1 + 0.2 \times 3.54^2)^{-3.5} = (1 + 0.2 \times 12.5316)^{-3.5} = (1 + 2.5063)^{-3.5} = (3.5063)^{-3.5} \approx 0.01400$
    *   The ratio is:
        $$ \frac{P_2}{P_1} = \frac{P_2/P_0}{P_1/P_0} \approx \frac{0.01400}{0.05853} \approx \mathbf{0.239} $$ 

5.  **Calculate Static Temperature Ratio ($T_2/T_1$):**
    Since the flow is isentropic and adiabatic, the stagnation temperature $T_0$ is constant. We use the isentropic temperature ratio $T/T_0 = (1 + \frac{\gamma-1}{2} M^2)^{-1}$.
    *   For $M_1 = 2.5$:
        $T_1/T_0 = (1 + 0.2 \times 2.5^2)^{-1} = (2.25)^{-1} \approx 0.4444$
    *   For $M_2 = 3.54$:
        $T_2/T_0 = (1 + 0.2 \times 3.54^2)^{-1} = (3.5063)^{-1} \approx 0.2852$
    *   The ratio is:
        $$ \frac{T_2}{T_1} = \frac{T_2/T_0}{T_1/T_0} \approx \frac{0.2852}{0.4444} \approx \mathbf{0.642} $$ 

**Elbow Design Description:**
The supersonic elbow consists of a single convex corner where the wall turns away from the initial flow direction by $20^\circ$. An expansion fan, composed of an infinite number of Mach waves, originates from this corner. The first wave corresponds to the initial Mach angle $\mu_1 = \arcsin(1/2.5) \approx 23.58^\circ$, and the last wave corresponds to the final Mach angle $\mu_2 = \arcsin(1/3.54) \approx 16.39^\circ$. The fan smoothly turns the flow by $20^\circ$ while accelerating it from $M_1=2.5$ to $M_2=3.54$. The static pressure and temperature decrease across the fan.

**Summary of Results:**
*   Final Mach Number: $M_2 \approx \mathbf{3.54}$
*   Static Pressure Ratio: $P_2/P_1 \approx \mathbf{0.239}$
*   Static Temperature Ratio: $T_2/T_1 \approx \mathbf{0.642}$

**Equations Used:**
*   Prandtl-Meyer Function: $\nu(M)$
*   Expansion Turn Relation: $\nu_2 = \nu_1 + \theta_{turn}$
*   Isentropic Pressure Ratio: $P/P_0(M)$
*   Isentropic Temperature Ratio: $T/T_0(M)$
