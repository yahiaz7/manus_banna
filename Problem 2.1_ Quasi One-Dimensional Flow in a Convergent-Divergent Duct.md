# Problem 2.1: Quasi One-Dimensional Flow in a Convergent-Divergent Duct

**Problem Statement:**
Consider a symmetric convergent-divergent nozzle with area per unit width given by $A(x) = 11.9774x^2 - 15.4774x + 6$, for $0 \le x \le 1$. Assume the flow is air ($\\gamma = 1.4$).
Tasks:
1. Plot the nozzle contour $A(x)$ versus $x$.
2. Find the limiting values of the back pressure ratio $P_{\infty} / P_0$.
3. Write a computer program (or outline the calculation logic) to calculate and plot:
    a. Mach number $M$ versus $x$.
    b. Static pressure ratio $P / P_0$ versus $x$.
    c. Mass flow rate parameter (e.g., $\\dot{m} \\sqrt{RT_0}/(P_0 A^*)$), $M_{Inlet}$, $M_{Throat}$, $M_{Exit}$, $P_{Exit} / P_0$ versus the back pressure ratio $P_{\infty} / P_0$.
Use $x$ steps of 0.05 and the provided list of $P_{\infty} / P_0$ values.

**Assumptions:**
*   Quasi-one-dimensional flow.
*   Steady flow.
*   Adiabatic flow.
*   Ideal gas with constant specific heats ($\\gamma = 1.4$).
*   $P_0$ and $T_0$ are the stagnation conditions in the reservoir upstream of the nozzle inlet.
*   $P_{\infty}$ is the ambient back pressure into which the nozzle exhausts.

**1. Nozzle Geometry Analysis:**

*   **Area Function:** $A(x) = 11.9774x^2 - 15.4774x + 6$
*   **Throat Location:** Find $x$ where $dA/dx = 0$.
    $dA/dx = 2(11.9774)x - 15.4774 = 23.9548x - 15.4774$
    $dA/dx = 0 \implies x_{throat} = 15.4774 / 23.9548 \approx 0.6461$
*   **Throat Area ($A^*$):**
    $A_{throat} = A(0.6461) = 11.9774(0.6461)^2 - 15.4774(0.6461) + 6$
    $A_{throat} \approx 11.9774(0.4174) - 15.4774(0.6461) + 6 \approx 5.000 - 10.000 + 6 = 1.000$
    We take the throat area as the reference sonic area, $A^* = 1.0$ (units of area per unit width).
*   **Inlet Area ($x=0$):**
    $A_{inlet} = A(0) = 6.0$
    Area Ratio: $A_{inlet}/A^* = 6.0 / 1.0 = 6.0$
*   **Exit Area ($x=1$):**
    $A_{exit} = A(1) = 11.9774(1)^2 - 15.4774(1) + 6 = 11.9774 - 15.4774 + 6 = 2.5$
    Area Ratio: $A_{exit}/A^* = 2.5 / 1.0 = 2.5$

**Nozzle Contour Plot:**
The area $A(x)$ will be calculated for $x = 0, 0.05, 0.10, ..., 1.0$. A plot of $A(x)$ vs $x$ shows the convergent-divergent shape.
*(Data points and plot will be generated programmatically below)*

**2. Limiting Back Pressure Ratios ($P_{\infty} / P_0$):**
These ratios define different flow regimes through the nozzle. We use the isentropic flow relations and normal shock relations.

*   **Isentropic Flow Relations:**
    $$ \frac{A}{A^*} = \frac{1}{M} \left[ \frac{2}{\gamma+1} \left( 1 + \frac{\gamma-1}{2} M^2 \right) \right]^{\frac{\gamma+1}{2(\gamma-1)}} $$ 
    $$ \frac{P}{P_0} = \left( 1 + \frac{\gamma-1}{2} M^2 \right)^{-\frac{\gamma}{\gamma-1}} $$ 
*   **Normal Shock Relations:**
    $$ M_2^2 = \frac{M_1^2 + \frac{2}{\gamma - 1}}{\frac{2\gamma}{\gamma - 1}M_1^2 - 1} $$ 
    $$ \frac{P_2}{P_1} = 1 + \frac{2\gamma}{\gamma + 1}(M_1^2 - 1) $$ 
    $$ \frac{P_{02}}{P_{01}} = \left[ \frac{(\gamma + 1)M_1^2}{(\gamma - 1)M_1^2 + 2} \right]^{\frac{\gamma}{\gamma - 1}} \left[ \frac{\gamma + 1}{2\gamma M_1^2 - (\gamma - 1)} \right]^{\frac{1}{\gamma - 1}} $$ 

*   **Calculations for Exit Area Ratio $A_{exit}/A^* = 2.5$ ($\\gamma=1.4$):**
    Solving the $A/A^*$ equation for $M$ when $A/A^*=2.5$ yields two isentropic solutions:
    *   Subsonic: $M_{exit, sub} \approx 0.240$
    *   Supersonic: $M_{exit, sup} \approx 2.441$

*   **Regime Boundaries:**
    a.  **No Flow:** $P_{\infty} / P_0 = 1$. $M=0$ everywhere.
    b.  **Subsonic Flow:** $1 > P_{\infty} / P_0 > (P/P_0)_{isen, sub}$. Flow is subsonic throughout, accelerates in convergent part, decelerates in divergent part. $M_{throat} < 1$. $\\dot{m}$ increases as $P_{\infty}/P_0$ decreases.
        The upper limit for choked flow (lower limit for purely subsonic flow) occurs when $M_{exit} = M_{exit, sub} \approx 0.240$. The corresponding pressure ratio is:
        $P_{exit}/P_0 = (1 + 0.2 \times 0.240^2)^{-3.5} \approx (1.0115)^{-3.5} \approx 0.9609$
        So, subsonic flow occurs for $1 > P_{\infty} / P_0 > 0.9609$.
    c.  **Choked Flow - Shock in Nozzle:** $(P/P_0)_{isen, sub} > P_{\infty} / P_0 > (P/P_0)_{shock\ at\ exit}$. Flow is choked ($M_{throat}=1$), $\\dot{m}$ is maximum and constant. Flow becomes supersonic in the divergent section, then passes through a normal shock wave *inside* the nozzle. The flow downstream of the shock is subsonic and decelerates further to the exit, matching $P_{exit} = P_{\infty}$.
    d.  **Choked Flow - Shock at Exit:** $P_{\infty} / P_0 = (P/P_0)_{shock\ at\ exit}$. As above, but the normal shock stands exactly at the exit plane ($x=1$). The Mach number just before the shock is $M_1 = M_{exit, sup} \approx 2.441$. The pressure ratio across this shock is:
        $P_2/P_1 = P_{\infty}/P_{exit, isen\ sup} = 1 + \frac{2(1.4)}{1.4+1}(2.441^2 - 1) = 1 + \frac{2.8}{2.4}(5.958 - 1) \approx 1 + 1.1667(4.958) \approx 6.784$
        The isentropic pressure ratio for $M=2.441$ is $P_{exit, isen\ sup}/P_0 = (1 + 0.2 \times 2.441^2)^{-3.5} \approx (2.1916)^{-3.5} \approx 0.0639$
        So, the back pressure ratio for a shock at the exit is:
        $(P_{\infty} / P_0)_{shock\ at\ exit} = (P_{\infty}/P_{exit, isen\ sup}) \times (P_{exit, isen\ sup}/P_0) \approx 6.784 \times 0.0639 \approx 0.4336$
        So, shock is inside the nozzle for $0.9609 > P_{\infty} / P_0 > 0.4336$.
    e.  **Choked Flow - Overexpanded:** $(P/P_0)_{shock\ at\ exit} > P_{\infty} / P_0 > (P/P_0)_{design}$. Flow is choked, $\\dot{m}$ is max. Flow is isentropic and supersonic up to the exit ($M_{exit} \approx 2.441$, $P_{exit}/P_0 \approx 0.0639$). Since $P_{exit} < P_{\infty}$, the flow adjusts to the higher back pressure through oblique shock waves outside the nozzle exit. The nozzle is overexpanded.
    f.  **Choked Flow - Design Condition (Isentropic Supersonic):** $P_{\infty} / P_0 = (P/P_0)_{design}$. Flow is choked, $\\dot{m}$ is max. Flow is isentropic supersonic throughout the divergent section. $M_{exit} \approx 2.441$, $P_{exit}/P_0 \approx 0.0639$. $P_{exit} = P_{\infty}$.
        $(P_{\infty} / P_0)_{design} \approx 0.0639$
    g.  **Choked Flow - Underexpanded:** $(P/P_0)_{design} > P_{\infty} / P_0 \ge 0$. Flow is choked, $\\dot{m}$ is max. Flow is isentropic supersonic up to the exit ($M_{exit} \approx 2.441$, $P_{exit}/P_0 \approx 0.0639$). Since $P_{exit} > P_{\infty}$, the flow adjusts to the lower back pressure through expansion waves outside the nozzle exit. The nozzle is underexpanded.

*   **Summary of Limiting Values:** $1.0$ (no flow), $0.9609$ (choked flow starts), $0.4336$ (shock at exit), $0.0639$ (design supersonic exit).

**3. Calculation Logic and Plots:**

*(The detailed calculations for all specified $x$ and $P_{\infty}/P_0$ values require a program. The logic is outlined here, and results/plots will be generated programmatically.)*

**a, b. $M(x)$ and $P(x)/P_0$ for various $P_{\infty}/P_0$:**

*   **Case 1: Unchoked Subsonic Flow ($1 \ge P_{\infty}/P_0 > 0.9609$)**
    *   Assume a mass flow rate $\\dot{m}$ (or $\\dot{m}$-parameter). Since $P_{\infty}$ is fixed, $P_{exit}=P_{\infty}$. Use $P_{exit}/P_0$ to find $M_{exit}$ (subsonic) from the isentropic relation.
    *   Calculate $A_{exit}/A^*$ corresponding to this $M_{exit}$. Note: This $A^*$ is hypothetical as flow is not choked.
    *   The actual mass flow parameter is determined by the condition $A_{exit}/A^*_{hypo} = (A_{exit}/A_{throat}) \times (A_{throat}/A^*_{hypo})$. This requires iteration to find the correct $\\dot{m}$ (or $M_{throat}$) that satisfies $P_{exit}=P_{\infty}$.
    *   Alternatively, iterate on $M_{throat} < 1$. For a chosen $M_{throat}$, calculate $A_{throat}/A^*$ and thus $A^*$. Then for each $x$, calculate $A(x)/A^*$ and find $M(x)$ (subsonic branch) and $P(x)/P_0$. Adjust $M_{throat}$ until $P(x=1) = P_{\infty}$.
    *   $M(x)$ increases to $M_{throat}$ then decreases to $M_{exit}$. $P(x)/P_0$ decreases to $P_{throat}/P_0$ then increases to $P_{exit}/P_0$.

*   **Case 2: Choked Flow ($P_{\infty}/P_0 \le 0.9609$)**
    *   Flow is choked, $M_{throat}=1$ at $x_{throat}=0.6461$. $A^* = A_{throat} = 1.0$. Mass flow rate is maximum and constant.
    *   For each $x$, calculate $A(x)/A^* = A(x)$.
    *   Use the isentropic relation $A/A^*$ vs $M$ to find $M(x)$. For $x < x_{throat}$, use the subsonic root ($M<1$). For $x > x_{throat}$, use the supersonic root ($M>1$).
    *   Calculate the isentropic pressure ratio $P_{isen}(x)/P_0$ using $M(x)$.
    *   **Check for Shock:** Compare $P_{isen}(x=1)/P_0$ with the target $P_{\infty}/P_0$.
        *   If $P_{\infty}/P_0 \ge P_{isen}(x=1)/P_0$ (specifically, $0.9609 \ge P_{\infty}/P_0 > 0.4336$): A normal shock occurs inside the nozzle at some location $x_s > x_{throat}$.
            *   Find $x_s$ such that the flow state downstream of the shock ($M_2, P_{02}$) evolves isentropically to match $P_{\infty}$ at $x=1$. This requires iteration:
                1. Guess shock location $x_s$. Find $M_1 = M_{isen, sup}(x_s)$.
                2. Calculate post-shock $M_2$ and $P_{02}/P_{01}$ using normal shock relations.
                3. Calculate the required $P(x=1)/P_{02} = (P_{\infty}/P_0) / (P_{02}/P_{01})$.
                4. Find the subsonic $M_{exit}$ corresponding to this pressure ratio.
                5. Calculate $(A/A^*)_{exit\ req} = A_{exit} / A^*_{downstream}$ required for this $M_{exit}$. Note $A^*_{downstream} = A^* \times (P_{01}/P_{02})$.
                6. Check if $A(x=1) / A^*_{downstream}$ matches the value calculated from $M_{exit}$. Adjust $x_s$ and repeat until converged.
            *   For $x < x_s$, $M(x)$ and $P(x)/P_0$ follow the isentropic subsonic/supersonic solution.
            *   For $x > x_s$, $M(x)$ and $P(x)/P_0$ follow the isentropic subsonic solution based on $P_{02}$ and $A^*_{downstream}$.
        *   If $P_{\infty}/P_0 < 0.4336$: No shock inside the nozzle. Flow is isentropic supersonic up to the exit. $M(x)$ and $P(x)/P_0$ follow the isentropic solution calculated earlier. $M_{exit} \approx 2.441$, $P_{exit}/P_0 \approx 0.0639$. The adjustment to $P_{\infty}$ occurs outside the nozzle (over/under-expanded). Exception: If $P_{\infty}/P_0 = 0.4336$, shock is at exit.

**c. Plots vs $P_{\infty}/P_0$:**

*   **Mass Flow ($\\dot{m}$ parameter):** Calculate $\\dot{m} \\sqrt{RT_0}/(P_0 A^*)$.
    *   For $1 \ge P_{\infty}/P_0 > 0.9609$: Mass flow increases as $P_{\infty}/P_0$ decreases. Calculate using $M_{throat}$ found in Case 1 above. $\\dot{m} \\frac{\\sqrt{RT_0}}{P_0 A(x)} = \\sqrt{\\gamma} M(x) (1 + \\frac{\\gamma-1}{2} M(x)^2)^{-\\frac{\\gamma+1}{2(\\gamma-1)}}$. Evaluate at throat.
    *   For $P_{\infty}/P_0 \le 0.9609$: Flow is choked. Mass flow is constant and maximum. $\\dot{m}_{choked} \\frac{\\sqrt{RT_0}}{P_0 A^*} = \\sqrt{\\gamma} (\\frac{2}{\\gamma+1})^{\\frac{\\gamma+1}{2(\\gamma-1)}} \approx 0.6847$ for $\\gamma=1.4$.
*   **$M_{Inlet}$:** Find $M(x=0)$ for each $P_{\infty}/P_0$. Use $A_{inlet}/A^*=6.0$. For choked flow, $M_{inlet}$ is constant (subsonic root for $A/A^*=6.0$, approx 0.098). For unchoked flow, $M_{inlet}$ depends on $M_{throat}$.
*   **$M_{Throat}$:** Find $M(x=x_{throat})$ for each $P_{\infty}/P_0$. $M_{throat}=1$ for choked flow ($P_{\infty}/P_0 \le 0.9609$). $M_{throat}<1$ for unchoked flow.
*   **$M_{Exit}$:** Find $M(x=1)$ for each $P_{\infty}/P_0$. Varies depending on regime (subsonic, shock location, supersonic).
*   **$P_{Exit}/P_0$:** Find $P(x=1)/P_0$ for each $P_{\infty}/P_0$. For regimes with no shock inside or at exit, $P_{exit}$ is determined by isentropic flow. If shock is inside/at exit, $P_{exit}=P_{\infty}$. If over/under-expanded, $P_{exit}$ is the isentropic supersonic value ($0.0639$).

*(Detailed data tables and plots for M(x), P(x)/P0, and parameters vs. P_inf/P0 will be generated programmatically based on this logic.)*
