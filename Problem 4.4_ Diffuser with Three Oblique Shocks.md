# Problem 4.4: Diffuser with Three Oblique Shocks

**Problem Statement:**
Design a two-dimensional supersonic diffuser using three oblique shocks followed by a normal shock to decelerate flow from $M_1=2.5$ to subsonic speed. Calculate the overall total pressure recovery. Compare the result with the one-shock (Problem 4.2) and two-shock (Problem 4.3) designs. Assume air with $\gamma = 1.4$.

**Approach:**
We extend the design from Problem 4.3 by adding a third wedge section, aiming for even higher pressure recovery. We will use three equal deflection angles followed by a terminal normal shock.

**Design Choice:**
Let the initial Mach number be $M_1 = 2.5$. We choose three equal deflection angles, $\delta_1 = \delta_2 = \delta_3 = 6.67^\circ$, for a total deflection of approximately $20^\circ$ (similar total turning to Problem 4.3, but distributed over more shocks).

**Assumptions:**
*   Steady, two-dimensional, planar flow.
*   Ideal gas with constant specific heats, $\gamma = 1.4$.
*   Shocks occur sequentially: Oblique Shock 1 $\to$ Oblique Shock 2 $\to$ Oblique Shock 3 $\to$ Normal Shock.

**Step-by-Step Calculation (Hand-Calculable):**

1.  **Analyze First Oblique Shock (Region 1 $\to$ Region 2):**
    *   $M_1 = 2.5$, $\delta_1 = 6.67^\circ$
    *   Using $\theta$-$\beta$-$M$ relation (tables/solver): $\beta_1 \approx 29.46^\circ$
    *   $M_{n1} = M_1 \sin\beta_1 = 2.5 \sin(29.46^\circ) \approx 1.230$
    *   $P_{02}/P_{01} \approx 0.9981$
    *   $M_{n2} \approx 0.824$
    *   $M_2 = M_{n2} / \sin(\beta_1 - \delta_1) = 0.824 / \sin(22.79^\circ) \approx 2.128$
    *   $	heta_2 = 6.67^\circ$

2.  **Analyze Second Oblique Shock (Region 2 $\to$ Region 3):**
    *   $M_2 = 2.128$, $\delta_2 = 6.67^\circ$
    *   Using $\theta$-$\beta$-$M$ relation: $\beta_2 \approx 33.90^\circ$
    *   $M_{n2} = M_2 \sin\beta_2 = 2.128 \sin(33.90^\circ) \approx 1.186$
    *   $P_{03}/P_{02} \approx 0.9989$
    *   $M_{n3} \approx 0.851$
    *   $M_3 = M_{n3} / \sin(\beta_2 - \delta_2) = 0.851 / \sin(27.23^\circ) \approx 1.859$
    *   $	heta_3 = 6.67^\circ + 6.67^\circ = 13.34^\circ$

3.  **Analyze Third Oblique Shock (Region 3 $\to$ Region 4):**
    *   $M_3 = 1.859$, $\delta_3 = 6.67^\circ$
    *   Using $\theta$-$\beta$-$M$ relation: $\beta_3 \approx 40.10^\circ$
    *   $M_{n3} = M_3 \sin\beta_3 = 1.859 \sin(40.10^\circ) \approx 1.197$
    *   $P_{04}/P_{03} \approx 0.9987$
    *   $M_{n4} \approx 0.844$
    *   $M_4 = M_{n4} / \sin(\beta_3 - \delta_3) = 0.844 / \sin(33.43^\circ) \approx 1.532$
    *   $	heta_4 = 13.34^\circ + 6.67^\circ = 20.01^\circ$

4.  **Analyze Normal Shock (Region 4 $\to$ Region 5):**
    *   $M_4 = 1.532$
    *   $P_{05}/P_{04} \approx 0.9185$ (from normal shock tables/calculation)
    *   $M_5 \approx 0.689$ (Subsonic)

5.  **Calculate Overall Total Pressure Recovery ($\\eta_{PR}$):**
    $$ \eta_{PR} = \frac{P_{05}}{P_{01}} = \frac{P_{02}}{P_{01}} \times \frac{P_{03}}{P_{02}} \times \frac{P_{04}}{P_{03}} \times \frac{P_{05}}{P_{04}} $$ 
    $$ \eta_{PR} \approx (0.9981) \times (0.9989) \times (0.9987) \times (0.9185) \approx 0.9149 $$ 

**Result and Comparison:**
The diffuser design using three $6.67^\circ$ deflection oblique shocks followed by a normal shock achieves an overall stagnation pressure recovery of approximately $\mathbf{0.915}$ or **91.5%**.

*   **Comparison:**
    *   Single Oblique Shock (Prob 4.2, $\delta=10^\circ$): $\eta_{PR} \approx 69.6\%$
    *   Two Oblique Shocks (Prob 4.3, $\delta=10^\circ+10^\circ$): $\eta_{PR} \approx 84.2\%$
    *   Three Oblique Shocks (Prob 4.4, $\delta=6.67^\circ \times 3$): $\eta_{PR} \approx 91.5\%$

This clearly demonstrates that increasing the number of weaker oblique shocks used for compression significantly improves the total pressure recovery of the supersonic diffuser, bringing the flow to a lower Mach number before the final, lossy normal shock.

**Equations Used:**
*   Oblique Shock Relations ($\theta$-$\beta$-$M$, $M_n = M \sin\beta$, $M_2(M_{n1}, \beta, \delta)$)
*   Normal Shock Relations ($M_2(M_1)$, $P_{02}/P_{01}(M_1)$)
*   Overall Pressure Recovery: $\eta_{PR} = P_{0, final}/P_{0, initial}$
