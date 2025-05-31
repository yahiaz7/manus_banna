# Problem 4.2: Simple 2D Supersonic Diffuser Design

**Problem Statement:**
Design a simple two-dimensional supersonic diffuser (inlet) using a single oblique shock followed by a normal shock to decelerate flow from an initial Mach number $M_1=2.5$ to subsonic speed. Calculate the overall total pressure recovery $\eta_{PR} = P_{0, final}/P_{0, initial}$. Assume air with $\gamma = 1.4$.

**Approach:**
A simple external compression inlet design uses a wedge to generate an oblique shock, which decelerates the supersonic flow. This is followed by a normal shock to bring the flow to subsonic conditions. The efficiency (total pressure recovery) depends on the strength of these shocks.

**Design Choice:**
We need to choose a wedge angle $\delta$ (or equivalently, the initial flow deflection angle). A smaller angle results in a weaker oblique shock (higher $P_{02}/P_{01}$) but leaves a higher Mach number ($M_2$) entering the normal shock, which then causes larger losses ($P_{03}/P_{02}$ is lower). A larger angle gives a stronger oblique shock (lower $P_{02}/P_{01}$) but reduces $M_2$, leading to weaker normal shock losses (higher $P_{03}/P_{02}$). There is an optimal angle, but for a simple design illustration, let's choose a moderate deflection angle $\delta = 10^\circ$.

**Assumptions:**
*   Steady, two-dimensional, planar flow.
*   Ideal gas with constant specific heats, $\gamma = 1.4$.
*   The normal shock occurs immediately after the oblique shock has turned the flow by $\delta$. (In a real inlet, the normal shock position is critical, often near the cowl lip or throat).

**Step-by-Step Calculation (Hand-Calculable):**

1.  **Analyze Oblique Shock (Region 1 $\to$ Region 2):**
    *   Upstream Mach number: $M_1 = 2.5$
    *   Deflection angle: $\delta = 10^\circ$
    *   Find the weak oblique shock wave angle $\beta$ using the $\theta$-$\beta$-$M$ relation:
        $$ \tan\delta = 2 \cot\beta \frac{M_1^2 \sin^2\beta - 1}{M_1^2 (\gamma + \cos(2\beta)) + 2} $$ 
        Solving this (e.g., using charts, tables, or numerical solver) for $M_1=2.5, \delta=10^\circ, \gamma=1.4$ gives the weak shock solution $\beta \approx 32.10^\circ$.
    *   Calculate the normal component of the upstream Mach number:
        $$ M_{n1} = M_1 \sin\beta = 2.5 \sin(32.10^\circ) \approx 2.5 \times 0.5314 = 1.3285 $$ 
    *   Calculate the Mach number after the oblique shock ($M_2$). First find $M_{n2}$ from the normal shock relation using $M_{n1}$:
        $$ M_{n2}^2 = \frac{M_{n1}^2 + \frac{2}{\gamma - 1}}{\frac{2\gamma}{\gamma - 1}M_{n1}^2 - 1} = \frac{(1.3285)^2 + 5}{7(1.3285)^2 - 1} = \frac{1.765 + 5}{12.355 - 1} = \frac{6.765}{11.355} \approx 0.5957 $$ 
        $$ M_{n2} = \sqrt{0.5957} \approx 0.7718 $$ 
        Now find $M_2$ using the relation $M_2 = M_{n2} / \sin(\beta - \delta)$:
        $$ M_2 = \frac{0.7718}{\sin(32.10^\circ - 10^\circ)} = \frac{0.7718}{\sin(22.10^\circ)} \approx \frac{0.7718}{0.3762} \approx 2.051 $$ 
    *   Calculate the stagnation pressure ratio across the oblique shock ($P_{02}/P_{01}$) using the normal component $M_{n1}=1.3285$. From standard normal shock tables or calculation (see Problem 3.3):
        $$ \frac{P_{02}}{P_{01}} \approx 0.9928 $$ 

2.  **Analyze Normal Shock (Region 2 $\to$ Region 3):**
    *   The flow entering the normal shock has Mach number $M_2 = 2.051$.
    *   Calculate the stagnation pressure ratio across the normal shock ($P_{03}/P_{02}$) using $M_2=2.051$. From standard normal shock tables or calculation:
        $$ \frac{P_{03}}{P_{02}} \approx 0.7010 $$ 
    *   The Mach number after the normal shock ($M_3$) can also be found:
        $$ M_3^2 = \frac{M_2^2 + 5}{7M_2^2 - 1} = \frac{(2.051)^2 + 5}{7(2.051)^2 - 1} = \frac{4.2066 + 5}{7(4.2066) - 1} = \frac{9.2066}{29.446 - 1} = \frac{9.2066}{28.446} \approx 0.3236 $$ 
        $$ M_3 = \sqrt{0.3236} \approx 0.569 $$ (Subsonic, as expected).

3.  **Calculate Overall Total Pressure Recovery ($\\eta_{PR}$):**
    The overall recovery is the product of the recoveries across each shock:
    $$ \eta_{PR} = \frac{P_{03}}{P_{01}} = \frac{P_{02}}{P_{01}} \times \frac{P_{03}}{P_{02}} $$ 
    $$ \eta_{PR} \approx (0.9928) \times (0.7010) \approx 0.6959 $$ 

**Design Description and Result:**
The simple diffuser design uses a $10^\circ$ wedge to create an oblique shock ($\\beta \approx 32.1^\circ$), decelerating the flow from $M_1=2.5$ to $M_2=2.05$. This is followed by a normal shock which further decelerates the flow to $M_3 \approx 0.57$ (subsonic). The overall stagnation pressure recovery for this design is approximately $\mathbf{0.696}$ or **69.6%**.

**Equations Used:**
*   Oblique Shock Relations ($\theta$-$\beta$-$M$, $M_n = M \sin\beta$, $M_2(M_{n1}, \beta, \delta)$)
*   Normal Shock Relations ($M_2(M_1)$, $P_{02}/P_{01}(M_1)$)
*   Overall Pressure Recovery: $\eta_{PR} = P_{0, final}/P_{0, initial}$
