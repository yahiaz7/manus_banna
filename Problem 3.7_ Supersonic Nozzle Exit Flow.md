# Problem 3.7: Supersonic Nozzle Exit Flow

**Problem Statement:**
A supersonic nozzle expands air ($\\gamma=1.4$) from reservoir conditions $P_0=10$ atm and $T_0=500$ K to an exit Mach number $M_e=2.5$. The nozzle exhausts into ambient conditions where the pressure is $P_a=1$ atm. Describe the flow pattern at the exit and determine the nature of the waves present.

**Assumptions:**
*   Convergent-divergent nozzle.
*   Isentropic flow *inside* the nozzle up to the exit plane.
*   Air as the working fluid, ideal gas with $\\gamma = 1.4$.

**Objective:**
Determine if the nozzle is overexpanded, underexpanded, or perfectly expanded, and describe the resulting wave pattern outside the nozzle exit.

**Step-by-Step Calculation (Hand-Calculable):**

1.  **Identify Given Pressures:**
    *   Stagnation Pressure: $P_0 = 10 \, atm$
    *   Ambient Back Pressure: $P_a = 1 \, atm$

2.  **Calculate Nozzle Exit Pressure ($P_e$) for Isentropic Expansion:**
    We use the isentropic relation between static and stagnation pressure for the exit Mach number $M_e = 2.5$.
    $$ \frac{P_e}{P_0} = \left( 1 + \frac{\gamma-1}{2} M_e^2 \right)^{-\frac{\gamma}{\gamma-1}} $$ 
    $$ \frac{P_e}{P_0} = \left( 1 + \frac{1.4-1}{2} (2.5)^2 \right)^{-\frac{1.4}{1.4-1}} = (1 + 0.2 \times 6.25)^{-3.5} = (1 + 1.25)^{-3.5} = (2.25)^{-3.5} $$ 
    Using standard isentropic flow tables or a calculator for $M=2.5$ ($\\gamma=1.4$):
    $$ \frac{P_e}{P_0} \approx 0.05853 $$ 
    Therefore, the pressure at the nozzle exit plane, assuming isentropic flow, is:
    $$ P_e = P_0 \times \left( \frac{P_e}{P_0} \right) = (10 \, atm) \times (0.05853) = 0.5853 \, atm $$ 

3.  **Compare Exit Pressure ($P_e$) with Ambient Pressure ($P_a$):**
    *   $P_e = 0.5853 \, atm$
    *   $P_a = 1.0 \, atm$
    Since $P_e < P_a$, the pressure inside the nozzle at the exit is lower than the pressure of the surrounding ambient atmosphere. This condition is known as **overexpanded** flow.

4.  **Describe Flow Pattern and Wave Nature:**
    Because the nozzle is overexpanded ($P_e < P_a$), the supersonic flow exiting the nozzle must adjust to the higher ambient pressure. This pressure adjustment occurs abruptly through shock waves.
    *   **Oblique Shock Waves:** Oblique shock waves will form at the nozzle lip (exit edge), propagating into the exhaust jet. These shocks turn the flow slightly inwards and compress it, increasing the static pressure.
    *   **Shock Reflection/Interaction:** These oblique shocks will propagate across the jet, reflect from the jet boundary (which acts like a constant pressure surface), or interact with shocks from the opposite lip. This interaction and reflection process creates a pattern of intersecting shock waves within the exhaust plume, often visible as "shock diamonds" or Mach diamonds.
    *   **Nature of Waves:** The waves present immediately outside the nozzle exit are **oblique shock waves** due to the overexpanded condition.

**Conclusion:**
The nozzle is operating in an **overexpanded** condition because its exit pressure ($P_e \approx 0.585$ atm) is less than the ambient pressure ($P_a = 1$ atm). Consequently, the flow adjusts to the higher back pressure through a system of **oblique shock waves** originating at the nozzle exit lip.

**Equations Used:**
*   Isentropic Pressure Ratio: $P/P_0 = (1 + \frac{\gamma-1}{2} M^2)^{-\gamma/(\gamma-1)}$
*   Flow Condition Definitions:
    *   Overexpanded: $P_e < P_a$
    *   Underexpanded: $P_e > P_a$
    *   Perfectly Expanded: $P_e = P_a$
