# Problem 2.6: Pipes in Parallel

**Problem Statement:**
A horizontal pipe carries water ($\\rho = 1000 \, kg/m^3$) at a rate of $\\dot{m}_{total} = 25 \, kg/s$. At a junction, the flow divides into three parallel pipes (details below). Determine:
(a) the head lost to friction ($h_L$)
(b) the flow rate of water through each parallel pipe ($Q_1, Q_2, Q_3$), neglecting minor losses.

**Given:**
*   Fluid: Water, $\rho = 1000 \, kg/m^3$
*   Total Mass Flow Rate: $\dot{m}_{total} = 25 \, kg/s$
*   Pipe 1: $L_1 = 15 \, m$, $D_1 = 25 \, mm = 0.025 \, m$, $f_1 = 0.005$
*   Pipe 2: $L_2 = 12 \, m$, $D_2 = 50 \, mm = 0.050 \, m$, $f_2 = 0.0075$
*   Pipe 3: $L_3 = 20 \, m$, $D_3 = 30 \, mm = 0.030 \, m$, $f_3 = 0.01$
*   Gravitational acceleration: $g = 9.81 \, m/s^2$
*   Assumptions: Horizontal pipes, neglect minor losses.

**Approach:**
For parallel pipes, the head loss across each branch is identical ($h_{L1} = h_{L2} = h_{L3} = h_L$). The total flow rate is the sum of the individual flow rates ($Q_{total} = Q_1 + Q_2 + Q_3$). We use the Darcy-Weisbach equation to relate head loss and flow rate in each pipe: $h_{Li} = \frac{8 f_i L_i}{g \pi^2 D_i^5} Q_i^2 = K_i Q_i^2$.

**Step-by-Step Calculation:**

1.  **Calculate Total Volumetric Flow Rate ($Q_{total}$):**
    $$ Q_{total} = \frac{\dot{m}_{total}}{\rho} = \frac{25 \, kg/s}{1000 \, kg/m^3} = 0.025 \, m^3/s $$ 

2.  **Calculate Resistance Coefficients ($K_i = \frac{8 f_i L_i}{g \pi^2 D_i^5}$):**
    Use $g \pi^2 \approx 96.82$.
    $$ K_1 = \frac{8 (0.005)(15)}{(96.82)(0.025)^5} = \frac{0.6}{96.82 \times 9.7656 \times 10^{-9}} \approx \frac{0.6}{9.455 \times 10^{-7}} \approx 634580 \, s^2/m^5 $$ 
    $$ K_2 = \frac{8 (0.0075)(12)}{(96.82)(0.050)^5} = \frac{0.72}{96.82 \times 3.125 \times 10^{-7}} \approx \frac{0.72}{3.0256 \times 10^{-5}} \approx 23800 \, s^2/m^5 $$ 
    $$ K_3 = \frac{8 (0.01)(20)}{(96.82)(0.030)^5} = \frac{1.6}{96.82 \times 2.43 \times 10^{-8}} \approx \frac{1.6}{2.3526 \times 10^{-6}} \approx 679970 \, s^2/m^5 $$ 

3.  **Relate Total Flow Rate to Head Loss:**
    Since $h_L = K_i Q_i^2$, we have $Q_i = \sqrt{h_L / K_i}$.
    $$ Q_{total} = Q_1 + Q_2 + Q_3 = \sqrt{\frac{h_L}{K_1}} + \sqrt{\frac{h_L}{K_2}} + \sqrt{\frac{h_L}{K_3}} = \sqrt{h_L} \left( \frac{1}{\sqrt{K_1}} + \frac{1}{\sqrt{K_2}} + \frac{1}{\sqrt{K_3}} \right) $$ 
    Calculate the sum of reciprocals of square roots:
    $$ \frac{1}{\sqrt{K_1}} = \frac{1}{\sqrt{634580}} \approx 0.001255 \, m^{2.5}/s $$ 
    $$ \frac{1}{\sqrt{K_2}} = \frac{1}{\sqrt{23800}} \approx 0.006481 \, m^{2.5}/s $$ 
    $$ \frac{1}{\sqrt{K_3}} = \frac{1}{\sqrt{679970}} \approx 0.001213 \, m^{2.5}/s $$ 
    $$ \sum \frac{1}{\sqrt{K_i}} = 0.001255 + 0.006481 + 0.001213 = 0.008949 \, m^{2.5}/s $$ 

4.  **Calculate Head Loss ($h_L$):**
    $$ Q_{total} = \sqrt{h_L} \left( \sum \frac{1}{\sqrt{K_i}} \right) $$ 
    $$ 0.025 \, m^3/s = \sqrt{h_L} (0.008949 \, m^{2.5}/s) $$ 
    $$ \sqrt{h_L} = \frac{0.025}{0.008949} \approx 2.7936 \, m^{0.5} $$ 
    $$ h_L = (2.7936)^2 \approx 7.804 \, m $$ 

5.  **Calculate Individual Flow Rates ($Q_i = \sqrt{h_L / K_i}$):**
    $$ Q_1 = \sqrt{\frac{7.804}{634580}} = \sqrt{1.2298 \times 10^{-5}} \approx 0.003507 \, m^3/s $$ 
    $$ Q_2 = \sqrt{\frac{7.804}{23800}} = \sqrt{3.2790 \times 10^{-4}} \approx 0.018108 \, m^3/s $$ 
    $$ Q_3 = \sqrt{\frac{7.804}{679970}} = \sqrt{1.1477 \times 10^{-5}} \approx 0.003388 \, m^3/s $$ 

**Results:**
(a) The head lost to friction is $h_L \approx \mathbf{7.80 \, m}$.
(b) The flow rates through the parallel pipes are:
    *   $Q_1 \approx \mathbf{0.00351 \, m^3/s}$
    *   $Q_2 \approx \mathbf{0.01811 \, m^3/s}$
    *   $Q_3 \approx \mathbf{0.00339 \, m^3/s}$

**Check:** $Q_1 + Q_2 + Q_3 \approx 0.00351 + 0.01811 + 0.00339 = 0.02501 \, m^3/s$, which matches $Q_{total}$ within rounding precision.

**Equations Used:**
*   Total Volumetric Flow Rate: $Q_{total} = \dot{m}_{total} / \rho$
*   Head Loss (Darcy-Weisbach): $h_{Li} = f_i \frac{L_i}{D_i} \frac{V_i^2}{2g}$
*   Head Loss vs Flow Rate: $h_{Li} = K_i Q_i^2$, where $K_i = \frac{8 f_i L_i}{g \pi^2 D_i^5}$
*   Parallel Flow Condition: $h_{L1} = h_{L2} = h_{L3} = h_L$
*   Continuity: $Q_{total} = Q_1 + Q_2 + Q_3$
*   Derived Relation: $Q_{total} = \sqrt{h_L} \sum (1/\sqrt{K_i})$
*   Individual Flow Rate: $Q_i = \sqrt{h_L / K_i}$
