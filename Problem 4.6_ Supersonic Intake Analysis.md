# Problem 4.6: Supersonic Intake Analysis

**Problem Statement:**
Analyze the performance of the two-shock external compression intake designed in Problem 4.5 ($M_1=3.0$, $\delta_1=8^\circ$, $\delta_2=12^\circ$, followed by a normal shock). Calculate the overall static pressure ratio $P_{final}/P_1$ and the overall static temperature ratio $T_{final}/T_1$ across the intake. Assume air with $\gamma = 1.4$.

**Approach:**
Using the results and intermediate values calculated in Problem 4.5, we will determine the static pressure and temperature ratios across each shock and multiply them to find the overall ratios.

**Assumptions:**
*   Steady, two-dimensional, planar flow.
*   Ideal gas with constant specific heats, $\gamma = 1.4$.
*   Shocks occur sequentially: Oblique Shock 1 $\to$ Oblique Shock 2 $\to$ Normal Shock.
*   Final state refers to conditions immediately downstream of the terminal normal shock.

**Step-by-Step Calculation (Hand-Calculable):**

*Recall results from Problem 4.5:*
*   Region 1: $M_1 = 3.0$
*   Region 2: $M_2 \approx 2.437$ (after $\delta_1=8^\circ$)
*   Region 3: $M_3 \approx 1.943$ (after $\delta_2=12^\circ$)
*   Region 4: $M_4 \approx 0.587$ (after normal shock)
*   Normal component for Shock 1: $M_{n1} \approx 1.334$
*   Normal component for Shock 2: $M_{n2} \approx 1.384$

1.  **Calculate Static Pressure Ratios:**
    *   Across Shock 1 ($M_{n1} \approx 1.334$):
        $$ \frac{P_2}{P_1} = 1 + \frac{2\gamma}{\gamma + 1}(M_{n1}^2 - 1) = 1 + \frac{2.8}{2.4}(1.334^2 - 1) \approx 1 + 1.167(1.779 - 1) \approx 1.909 $$ 
    *   Across Shock 2 ($M_{n2} \approx 1.384$):
        $$ \frac{P_3}{P_2} = 1 + \frac{2\gamma}{\gamma + 1}(M_{n2}^2 - 1) = 1 + \frac{2.8}{2.4}(1.384^2 - 1) \approx 1 + 1.167(1.915 - 1) \approx 2.068 $$ 
    *   Across Normal Shock ($M_3 \approx 1.943$):
        $$ \frac{P_4}{P_3} = 1 + \frac{2\gamma}{\gamma + 1}(M_3^2 - 1) = 1 + \frac{2.8}{2.4}(1.943^2 - 1) \approx 1 + 1.167(3.775 - 1) \approx 4.238 $$ 
    *   Overall Static Pressure Ratio:
        $$ \frac{P_4}{P_1} = \frac{P_2}{P_1} \times \frac{P_3}{P_2} \times \frac{P_4}{P_3} \approx (1.909) \times (2.068) \times (4.238) \approx \mathbf{16.72} $$ 

2.  **Calculate Static Temperature Ratios:**
    *   Across Shock 1 ($M_{n1} \approx 1.334$):
        $$ \frac{T_2}{T_1} = \frac{\left(1 + \frac{\gamma-1}{2}M_{n1}^2\right) \left(\frac{2\gamma}{\gamma-1}M_{n1}^2 - 1\right)}{\frac{(\gamma+1)^2}{2(\gamma-1)} M_{n1}^2} \approx \frac{(1+0.2(1.334^2))(7(1.334^2)-1)}{6(1.334^2)} \approx \frac{(1.356)(11.451)}{10.672} \approx 1.212 $$ 
    *   Across Shock 2 ($M_{n2} \approx 1.384$):
        $$ \frac{T_3}{T_2} \approx \frac{(1+0.2(1.384^2))(7(1.384^2)-1)}{6(1.384^2)} \approx \frac{(1.383)(12.408)}{11.492} \approx 1.244 $$ 
    *   Across Normal Shock ($M_3 \approx 1.943$):
        $$ \frac{T_4}{T_3} \approx \frac{(1+0.2(1.943^2))(7(1.943^2)-1)}{6(1.943^2)} \approx \frac{(1.755)(25.427)}{22.652} \approx 1.642 $$ 
    *   Overall Static Temperature Ratio:
        $$ \frac{T_4}{T_1} = \frac{T_2}{T_1} \times \frac{T_3}{T_2} \times \frac{T_4}{T_3} \approx (1.212) \times (1.244) \times (1.642) \approx \mathbf{2.478} $$ 

**Result:**
For the analyzed intake ($M_1=3.0$, $\delta_1=8^\circ$, $\delta_2=12^\circ$, normal shock):
*   The overall static pressure ratio is $P_4/P_1 \approx \mathbf{16.72}$.
*   The overall static temperature ratio is $T_4/T_1 \approx \mathbf{2.48}$.

**Equations Used:**
*   Oblique Shock Relations ($P_2/P_1(M_{n1})$, $T_2/T_1(M_{n1})$)
*   Normal Shock Relations ($P_2/P_1(M_1)$, $T_2/T_1(M_1)$)
*   Overall Ratios obtained by multiplication.
