# Problem 3.3: Standing Normal Shock (Appendix D)

**Problem Statement:**
This problem likely requires the calculation of properties across a standing normal shock wave, using the relations typically found in gas dynamics tables (referred to here as Appendix D).

**Scenario:**
Consider a steady, one-dimensional flow of an ideal gas (e.g., air, $\\gamma = 1.4$) encountering a normal shock wave. The flow upstream of the shock (Region 1) is supersonic ($M_1 > 1$). The flow downstream (Region 2) is subsonic ($M_2 < 1$).

**Governing Equations (Rankine-Hugoniot Relations):**
These equations relate the properties in Region 2 to those in Region 1. They were previously listed in Problem 1.1.

*   **Mach Number:**
    $$ M_2^2 = \frac{M_1^2 + \frac{2}{\gamma - 1}}{\frac{2\gamma}{\gamma - 1}M_1^2 - 1} $$ 
*   **Static Pressure Ratio:**
    $$ \frac{P_2}{P_1} = 1 + \frac{2\gamma}{\gamma + 1}(M_1^2 - 1) $$ 
*   **Static Temperature Ratio:**
    $$ \frac{T_2}{T_1} = \frac{\left(1 + \frac{\gamma-1}{2}M_1^2\right) \left(\frac{2\gamma}{\gamma-1}M_1^2 - 1\right)}{\frac{(\gamma+1)^2}{2(\gamma-1)} M_1^2} = \frac{P_2}{P_1} \frac{\rho_1}{\rho_2} $$ 
*   **Density Ratio (Velocity Ratio):**
    $$ \frac{\rho_2}{\rho_1} = \frac{V_1}{V_2} = \frac{(\gamma + 1)M_1^2}{(\gamma - 1)M_1^2 + 2} $$ 
*   **Stagnation Pressure Ratio (Entropy Increase):**
    $$ \frac{P_{02}}{P_{01}} = \left[ \frac{(\gamma + 1)M_1^2}{(\gamma - 1)M_1^2 + 2} \right]^{\frac{\gamma}{\gamma - 1}} \left[ \frac{\gamma + 1}{2\gamma M_1^2 - (\gamma - 1)} \right]^{\frac{1}{\gamma - 1}} $$ 
*   **Stagnation Temperature Ratio:**
    $$ \frac{T_{02}}{T_{01}} = 1 $$ (Adiabatic flow)

**Example Calculation (Hand-Calculable):**
Let the upstream Mach number be $M_1 = 2.0$ and assume air with $\\gamma = 1.4$.

*   **$M_2$:**
    $$ M_2^2 = \frac{2.0^2 + \frac{2}{1.4 - 1}}{\frac{2(1.4)}{1.4 - 1}(2.0^2) - 1} = \frac{4 + \frac{2}{0.4}}{\frac{2.8}{0.4}(4) - 1} = \frac{4 + 5}{7(4) - 1} = \frac{9}{28 - 1} = \frac{9}{27} = \frac{1}{3} $$ 
    $$ M_2 = \sqrt{1/3} \approx 0.577 $$ 
*   **$P_2/P_1$:**
    $$ \frac{P_2}{P_1} = 1 + \frac{2(1.4)}{1.4 + 1}(2.0^2 - 1) = 1 + \frac{2.8}{2.4}(4 - 1) = 1 + \frac{7}{6}(3) = 1 + 3.5 = 4.5 $$ 
*   **$\rho_2/\rho_1$:**
    $$ \frac{\rho_2}{\rho_1} = \frac{(1.4 + 1)(2.0^2)}{(1.4 - 1)(2.0^2) + 2} = \frac{2.4(4)}{0.4(4) + 2} = \frac{9.6}{1.6 + 2} = \frac{9.6}{3.6} = \frac{96}{36} = \frac{8}{3} \approx 2.667 $$ 
*   **$T_2/T_1$:**
    $$ \frac{T_2}{T_1} = \frac{P_2}{P_1} \frac{\rho_1}{\rho_2} = (4.5) \left( \frac{3}{8} \right) = \frac{13.5}{8} = 1.6875 $$ 
*   **$P_{02}/P_{01}$:**
    $$ \frac{P_{02}}{P_{01}} = \left[ \frac{8}{3} \right]^{\frac{1.4}{0.4}} \left[ \frac{2.4}{2(1.4)(4) - 0.4} \right]^{\frac{1}{0.4}} = \left[ \frac{8}{3} \right]^{3.5} \left[ \frac{2.4}{11.2 - 0.4} \right]^{2.5} $$ 
    $$ \frac{P_{02}}{P_{01}} = (2.667)^{3.5} \left[ \frac{2.4}{10.8} \right]^{2.5} = (2.667)^{3.5} \left[ \frac{1}{4.5} \right]^{2.5} \approx (25.66)(0.0233) \approx 0.7209 $$ 

**Use of Appendix D (Normal Shock Tables):**
Gas dynamics textbooks typically include tables (like the assumed Appendix D) that list these ratios ($M_2, P_2/P_1, T_2/T_1, \rho_2/\rho_1, P_{02}/P_{01}$) pre-calculated for various upstream Mach numbers $M_1$ (usually for $\\gamma = 1.4$). These tables allow for quick lookup of the downstream conditions without performing the hand calculations for standard values of $M_1$. They are generated using the Rankine-Hugoniot equations shown above.

**Conclusion:**
The properties across a standing normal shock are determined by the upstream Mach number $M_1$ and the specific heat ratio $\\gamma$. The Rankine-Hugoniot equations provide the means to calculate these changes, and standard tables (like Appendix D) offer convenient pre-calculated values.
