# Problem 2.5: Pipes in Series

**Problem Statement:**
Calculate the pressure losses in the shown pipeline (pipe 1 followed by pipe 2 with a sudden contraction between them).

**Given:**
*   Flow Rate: $Q = 1.25 \times 10^{-4} \, m^3/s$
*   Pipe 1: Length $L_1 = 4 \, m$, Diameter $D_1 = 13 \, mm = 0.013 \, m$
*   Pipe 2: Length $L_2 = 4 \, m$, Diameter $D_2 = 8 \, mm = 0.008 \, m$
*   Fluid Density: $\rho = 850 \, kg/m^3$
*   Fluid Kinematic Viscosity: $\nu = 1.95 \times 10^{-5} \, m^2/s$
*   Gravitational acceleration: $g = 9.81 \, m/s^2$

**Diagram Interpretation:**
The diagram shows flow entering pipe 1, passing through a sudden contraction into pipe 2, and then exiting pipe 2.

**Objective:** Calculate the total pressure loss $\Delta P_{total}$.

**Approach:**
The total pressure loss is the sum of pressure losses due to friction in each pipe section (major losses) and the pressure loss due to the sudden contraction (minor loss).
Total Head Loss $h_{L, total} = h_{L1} + h_{m, contraction} + h_{L2}$
Total Pressure Loss $\Delta P_{total} = \rho g h_{L, total}$

**Step-by-Step Calculation:**

1.  **Calculate Areas:**
    $A_1 = \frac{\pi D_1^2}{4} = \frac{\pi (0.013 \, m)^2}{4} \approx 1.3273 \times 10^{-4} \, m^2$
    $A_2 = \frac{\pi D_2^2}{4} = \frac{\pi (0.008 \, m)^2}{4} \approx 5.0265 \times 10^{-5} \, m^2$

2.  **Calculate Velocities:**
    $V_1 = \frac{Q}{A_1} = \frac{1.25 \times 10^{-4} \, m^3/s}{1.3273 \times 10^{-4} \, m^2} \approx 0.94176 \, m/s$
    $V_2 = \frac{Q}{A_2} = \frac{1.25 \times 10^{-4} \, m^3/s}{5.0265 \times 10^{-5} \, m^2} \approx 2.4868 \, m/s$

3.  **Calculate Reynolds Numbers:**
    $Re_1 = \frac{V_1 D_1}{\nu} = \frac{(0.94176 \, m/s)(0.013 \, m)}{1.95 \times 10^{-5} \, m^2/s} \approx \frac{0.012243}{1.95 \times 10^{-5}} \approx 627.8$
    $Re_2 = \frac{V_2 D_2}{\nu} = \frac{(2.4868 \, m/s)(0.008 \, m)}{1.95 \times 10^{-5} \, m^2/s} \approx \frac{0.019894}{1.95 \times 10^{-5}} \approx 1020.2$

4.  **Determine Flow Regimes:**
    Since $Re_1 \approx 628 < 2300$ and $Re_2 \approx 1020 < 2300$, the flow is **laminar** in both pipe sections.

5.  **Calculate Friction Factors (Laminar Flow):**
    $f_1 = \frac{64}{Re_1} = \frac{64}{627.8} \approx 0.10194$
    $f_2 = \frac{64}{Re_2} = \frac{64}{1020.2} \approx 0.06273$

6.  **Calculate Major Head Losses (Darcy-Weisbach Equation):**
    $h_{L1} = f_1 \frac{L_1}{D_1} \frac{V_1^2}{2g} = (0.10194) \frac{4 \, m}{0.013 \, m} \frac{(0.94176 \, m/s)^2}{2(9.81 \, m/s^2)}$
    $h_{L1} \approx (0.10194)(307.69) \frac{0.8869}{19.62} \approx (31.367)(0.04520) \approx 1.4178 \, m$

    $h_{L2} = f_2 \frac{L_2}{D_2} \frac{V_2^2}{2g} = (0.06273) \frac{4 \, m}{0.008 \, m} \frac{(2.4868 \, m/s)^2}{2(9.81 \, m/s^2)}$
    $h_{L2} \approx (0.06273)(500) \frac{6.184}{19.62} \approx (31.365)(0.31519) \approx 9.8858 \, m$

7.  **Calculate Minor Head Loss (Sudden Contraction):**
    The head loss for a sudden contraction is given by $h_m = K_L \frac{V_2^2}{2g}$, where $K_L$ depends on the area ratio $A_2/A_1 = (D_2/D_1)^2$.
    $A_2/A_1 = (0.008/0.013)^2 \approx (0.6154)^2 \approx 0.3787$
    From standard fluid mechanics references (e.g., White, Munson), for laminar flow or turbulent flow, the loss coefficient $K_L$ for a sudden contraction with $A_2/A_1 \approx 0.38$ is approximately $K_L \approx 0.33$ (based on the downstream velocity $V_2$).
    $h_{m, contraction} = K_L \frac{V_2^2}{2g} \approx (0.33) \frac{(2.4868 \, m/s)^2}{2(9.81 \, m/s^2)}$
    $h_{m, contraction} \approx (0.33)(0.31519 \, m) \approx 0.1040 \, m$

8.  **Calculate Total Head Loss:**
    $h_{L, total} = h_{L1} + h_{m, contraction} + h_{L2}$
    $h_{L, total} \approx 1.4178 \, m + 0.1040 \, m + 9.8858 \, m \approx 11.4076 \, m$

9.  **Calculate Total Pressure Loss:**
    $\Delta P_{total} = \rho g h_{L, total}$
    $\Delta P_{total} = (850 \, kg/m^3)(9.81 \, m/s^2)(11.4076 \, m)$
    $\Delta P_{total} \approx (8338.5)(11.4076) \approx 95118 \, Pa$

**Result:**
The total pressure loss in the pipeline is approximately **95118 Pa** or **95.1 kPa**.

**Equations Used:**
*   Area: $A = \pi D^2 / 4$
*   Velocity: $V = Q / A$
*   Reynolds Number: $Re = VD / \nu$
*   Laminar Friction Factor: $f = 64 / Re$
*   Major Head Loss (Darcy-Weisbach): $h_L = f (L/D) (V^2 / 2g)$
*   Minor Head Loss (Contraction): $h_m = K_L (V_2^2 / 2g)$ (with empirical $K_L$)
*   Total Head Loss: $h_{L, total} = \sum h_L + \sum h_m$
*   Total Pressure Loss: $\Delta P_{total} = \rho g h_{L, total}$
