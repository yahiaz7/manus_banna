# Problem 4.3: Diffuser with Two Oblique Shocks

**Problem Statement:**
Design a two-dimensional supersonic diffuser using two oblique shocks followed by a normal shock to decelerate flow from $M_1=2.5$ to subsonic speed. Calculate the overall total pressure recovery. Compare the result with the single oblique shock design (Problem 4.2). Assume air with $\gamma = 1.4$.

**Approach:**
We will design an inlet with two wedge sections, each deflecting the flow by the same angle, followed by a terminal normal shock. The goal is to achieve higher pressure recovery compared to using only one oblique shock.

**Design Choice:**
Let's choose two deflection angles, $\delta_1 = 10^\circ$ and $\delta_2 = 10^\circ$, for a total deflection of $20^\circ$ before the normal shock. The initial Mach number is $M_1 = 2.5$.

**Assumptions:**
*   Steady, two-dimensional, planar flow.
*   Ideal gas with constant specific heats, $\gamma = 1.4$.
*   Shocks occur sequentially: Oblique Shock 1 $\to$ Oblique Shock 2 $\to$ Normal Shock.

**Step-by-Step Calculation (Hand-Calculable):**

1.  **Analyze First Oblique Shock (Region 1 $\to$ Region 2):**
    *   Upstream Mach number: $M_1 = 2.5$
    *   Deflection angle: $\delta_1 = 10^\circ$
    *   From Problem 4.2 calculations (or standard oblique shock analysis):
        *   Weak shock wave angle: $\beta_1 \approx 32.10^\circ$
        *   Normal component: $M_{n1} = M_1 \sin\beta_1 \approx 1.3285$
        *   Mach number after shock: $M_2 \approx 2.051$
        *   Flow angle: $\theta_2 = \delta_1 = 10^\circ$
        *   Stagnation pressure ratio: $P_{02}/P_{01} \approx 0.9928$

2.  **Analyze Second Oblique Shock (Region 2 $\to$ Region 3):**
    *   Upstream Mach number (relative to shock): $M_2 = 2.051$
    *   Deflection angle: $\delta_2 = 10^\circ$
    *   Find the weak oblique shock wave angle $\beta_2$ using the $\theta$-$\beta$-$M$ relation for $M_2=2.051, \delta_2=10^\circ$. Using tables or a solver:
        *   Weak shock wave angle: $\beta_2 \approx 38.05^\circ$ (relative to flow direction in Region 2)
    *   Calculate the normal component of the upstream Mach number (for this shock):
        $$ M_{n2} = M_2 \sin\beta_2 = 2.051 \sin(38.05^\circ) \approx 2.051 \times 0.6163 \approx 1.264 $$ 
    *   Calculate the Mach number after the second oblique shock ($M_3$). First find $M_{n3}$ from the normal shock relation using $M_{n2}$:
        $$ M_{n3}^2 = \frac{M_{n2}^2 + 5}{7M_{n2}^2 - 1} = \frac{(1.264)^2 + 5}{7(1.264)^2 - 1} = \frac{1.598 + 5}{11.184 - 1} = \frac{6.598}{10.184} \approx 0.6479 $$ 
        $$ M_{n3} = \sqrt{0.6479} \approx 0.8049 $$ 
        Now find $M_3$ using the relation $M_3 = M_{n3} / \sin(\beta_2 - \delta_2)$:
        $$ M_3 = \frac{0.8049}{\sin(38.05^\circ - 10^\circ)} = \frac{0.8049}{\sin(28.05^\circ)} \approx \frac{0.8049}{0.4702} \approx 1.712 $$ 
    *   Flow angle after second shock: $\theta_3 = \theta_2 + \delta_2 = 10^\circ + 10^\circ = 20^\circ$.
    *   Calculate the stagnation pressure ratio across the second oblique shock ($P_{03}/P_{02}$) using the normal component $M_{n2}=1.264$. From standard normal shock tables or calculation:
        $$ \frac{P_{03}}{P_{02}} \approx 0.9968 $$ 

3.  **Analyze Normal Shock (Region 3 $\to$ Region 4):**
    *   The flow entering the normal shock has Mach number $M_3 = 1.712$.
    *   Calculate the stagnation pressure ratio across the normal shock ($P_{04}/P_{03}$) using $M_3=1.712$. From standard normal shock tables or calculation:
        $$ \frac{P_{04}}{P_{03}} \approx 0.8508 $$ 
    *   The Mach number after the normal shock ($M_4$) is:
        $$ M_4^2 = \frac{M_3^2 + 5}{7M_3^2 - 1} = \frac{(1.712)^2 + 5}{7(1.712)^2 - 1} \approx 0.4064 $$ 
        $$ M_4 = \sqrt{0.4064} \approx 0.637 $$ (Subsonic).

4.  **Calculate Overall Total Pressure Recovery ($\\eta_{PR}$):**
    The overall recovery is the product of the recoveries across each shock:
    $$ \eta_{PR} = \frac{P_{04}}{P_{01}} = \frac{P_{02}}{P_{01}} \times \frac{P_{03}}{P_{02}} \times \frac{P_{04}}{P_{03}} $$ 
    $$ \eta_{PR} \approx (0.9928) \times (0.9968) \times (0.8508) \approx 0.8422 $$ 

**Result and Comparison:**
The diffuser design using two $10^\circ$ deflection oblique shocks followed by a normal shock achieves an overall stagnation pressure recovery of approximately $\mathbf{0.842}$ or **84.2%**.

This is significantly higher than the recovery of the single $10^\circ$ oblique shock plus normal shock diffuser from Problem 4.2, which was $\approx 69.6\%$. This demonstrates the advantage of using multiple, weaker oblique shocks for supersonic compression to minimize stagnation pressure losses compared to a single stronger oblique shock or a single normal shock.

**Equations Used:**
*   Oblique Shock Relations ($\theta$-$\beta$-$M$, $M_n = M \sin\beta$, $M_2(M_{n1}, \beta, \delta)$)
*   Normal Shock Relations ($M_2(M_1)$, $P_{02}/P_{01}(M_1)$)
*   Overall Pressure Recovery: $\eta_{PR} = P_{0, final}/P_{0, initial}$
