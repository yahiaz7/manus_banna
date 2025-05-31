# Problem 4.5: Supersonic Shock Diffuser Analysis/Design

**Problem Statement:**
Analyze the performance of a specific two-dimensional, two-shock external compression diffuser (inlet). The freestream Mach number is $M_1 = 3.0$. The first wedge deflects the flow by $\delta_1 = 8^\circ$, and the second wedge deflects the flow by an additional $\delta_2 = 12^\circ$. A normal shock occurs downstream of the second oblique shock, bringing the flow to subsonic speed. Calculate the overall total pressure recovery $\eta_{PR}$. Assume air with $\gamma = 1.4$.

**Approach:**
We will calculate the flow properties and stagnation pressure ratios across each shock sequentially: the first oblique shock, the second oblique shock, and the final normal shock.

**Assumptions:**
*   Steady, two-dimensional, planar flow.
*   Ideal gas with constant specific heats, $\gamma = 1.4$.
*   Shocks occur sequentially as described.

**Step-by-Step Calculation (Hand-Calculable):**

1.  **Analyze First Oblique Shock (Region 1 $\to$ Region 2):**
    *   Upstream Mach number: $M_1 = 3.0$
    *   Deflection angle: $\delta_1 = 8^\circ$
    *   Using the $\theta$-$\beta$-$M$ relation (charts, tables, or solver) for $M_1=3.0, \delta_1=8^\circ, \gamma=1.4$, find the weak shock wave angle $\beta_1$:
        $$ \beta_1 \approx 26.39^\circ $$ 
    *   Calculate the normal component of the upstream Mach number:
        $$ M_{n1} = M_1 \sin\beta_1 = 3.0 \sin(26.39^\circ) \approx 3.0 \times 0.4445 \approx 1.334 $$ 
    *   Calculate the stagnation pressure ratio across this shock using $M_{n1}=1.334$. From normal shock tables or the formula:
        $$ \frac{P_{02}}{P_{01}} = \left[ \frac{(\gamma + 1)M_{n1}^2}{(\gamma - 1)M_{n1}^2 + 2} \right]^{\frac{\gamma}{\gamma - 1}} \left[ \frac{\gamma + 1}{2\gamma M_{n1}^2 - (\gamma - 1)} \right]^{\frac{1}{\gamma - 1}} \approx 0.9923 $$ 
    *   Calculate the Mach number after the shock ($M_2$). First find $M_{n2}$ from the normal shock relation using $M_{n1}$:
        $$ M_{n2}^2 = \frac{M_{n1}^2 + 5}{7M_{n1}^2 - 1} = \frac{(1.334)^2 + 5}{7(1.334)^2 - 1} \approx \frac{1.779 + 5}{12.451 - 1} = \frac{6.779}{11.451} \approx 0.5920 $$ 
        $$ M_{n2} = \sqrt{0.5920} \approx 0.769 $$ 
        Now find $M_2$ using $M_2 = M_{n2} / \sin(\beta_1 - \delta_1)$:
        $$ M_2 = \frac{0.769}{\sin(26.39^\circ - 8^\circ)} = \frac{0.769}{\sin(18.39^\circ)} \approx \frac{0.769}{0.3155} \approx 2.437 $$ 
    *   Flow angle after first shock: $\theta_2 = \delta_1 = 8^\circ$.

2.  **Analyze Second Oblique Shock (Region 2 $\to$ Region 3):**
    *   Upstream Mach number (relative to shock): $M_2 = 2.437$
    *   Deflection angle: $\delta_2 = 12^\circ$
    *   Using the $\theta$-$\beta$-$M$ relation for $M_2=2.437, \delta_2=12^\circ$, find the weak shock wave angle $\beta_2$:
        $$ \beta_2 \approx 34.60^\circ $$ (relative to flow direction in Region 2)
    *   Calculate the normal component of the upstream Mach number (for this shock):
        $$ M_{n2} = M_2 \sin\beta_2 = 2.437 \sin(34.60^\circ) \approx 2.437 \times 0.5678 \approx 1.384 $$ 
    *   Calculate the stagnation pressure ratio across this shock using $M_{n2}=1.384$:
        $$ \frac{P_{03}}{P_{02}} \approx 0.9884 $$ 
    *   Calculate the Mach number after the second oblique shock ($M_3$). First find $M_{n3}$:
        $$ M_{n3}^2 = \frac{M_{n2}^2 + 5}{7M_{n2}^2 - 1} = \frac{(1.384)^2 + 5}{7(1.384)^2 - 1} \approx \frac{1.915 + 5}{13.408 - 1} = \frac{6.915}{12.408} \approx 0.5573 $$ 
        $$ M_{n3} = \sqrt{0.5573} \approx 0.7465 $$ 
        Now find $M_3$ using $M_3 = M_{n3} / \sin(\beta_2 - \delta_2)$:
        $$ M_3 = \frac{0.7465}{\sin(34.60^\circ - 12^\circ)} = \frac{0.7465}{\sin(22.60^\circ)} \approx \frac{0.7465}{0.3843} \approx 1.943 $$ 
    *   Flow angle after second shock: $\theta_3 = \theta_2 + \delta_2 = 8^\circ + 12^\circ = 20^\circ$.

3.  **Analyze Normal Shock (Region 3 $\to$ Region 4):**
    *   The flow entering the normal shock has Mach number $M_3 = 1.943$.
    *   Calculate the stagnation pressure ratio across the normal shock ($P_{04}/P_{03}$) using $M_3=1.943$. From standard normal shock tables or calculation:
        $$ \frac{P_{04}}{P_{03}} \approx 0.7480 $$ 
    *   The Mach number after the normal shock ($M_4$) is subsonic.

4.  **Calculate Overall Total Pressure Recovery ($\\eta_{PR}$):**
    The overall recovery is the product of the recoveries across each shock:
    $$ \eta_{PR} = \frac{P_{04}}{P_{01}} = \frac{P_{02}}{P_{01}} \times \frac{P_{03}}{P_{02}} \times \frac{P_{04}}{P_{03}} $$ 
    $$ \eta_{PR} \approx (0.9923) \times (0.9884) \times (0.7480) \approx 0.7338 $$ 

**Result:**
The overall stagnation pressure recovery for this specific two-shock diffuser design ($M_1=3.0$, $\delta_1=8^\circ$, $\delta_2=12^\circ$) followed by a normal shock is approximately $\mathbf{0.734}$ or **73.4%**.

**Equations Used:**
*   Oblique Shock Relations ($\theta$-$\beta$-$M$, $M_n = M \sin\beta$, $M_2(M_{n1}, \beta, \delta)$)
*   Normal Shock Relations ($M_2(M_1)$, $P_{02}/P_{01}(M_1)$)
*   Overall Pressure Recovery: $\eta_{PR} = P_{0, final}/P_{0, initial}$
