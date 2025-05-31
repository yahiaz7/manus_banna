# Problem 1.1: Coding of Gas Dynamics Procedures

This problem requires coding procedures for fundamental gas dynamics processes: Normal Shock, Oblique Shock, Prandtl-Meyer Angle, and Prandtl-Meyer Flow, referencing Appendix A for structure and variable keys. While the problem suggests specific software (Maple, Mathematica, Matlab), the core task involves understanding and implementing the underlying aerodynamic equations, which are hand-calculable in principle.

We will outline the governing equations and logic for each procedure based on standard compressible flow theory (assuming an ideal gas with constant specific heats, typically $\gamma = 1.4$ for air) and the structure provided in Appendix A.

**Assumptions:**
*   Ideal gas
*   Constant specific heats ($\gamma = 1.4$ for air, unless otherwise specified)
*   Adiabatic flow for shock and isentropic flow processes

**Nomenclature based on Appendix A and standard usage:**
*   $M$: Mach number
*   $P$: Static pressure
*   $T$: Static temperature
*   $\rho$: Density
*   $P_0$ (or $P_t$): Stagnation (total) pressure
*   $T_0$ (or $T_t$): Stagnation (total) temperature
*   $\rho_0$ (or $\rho_t$): Stagnation (total) density
*   $A$: Area
*   $A^*$: Area at sonic conditions (M=1)
*   $v$: Velocity
*   $a$: Speed of sound
*   $\nu$: Prandtl-Meyer function (angle)
*   $\theta$: Flow deflection angle
*   $\beta$: Wave angle (Oblique shock or Mach wave)
*   Subscripts 1 and 2 denote conditions upstream and downstream of a wave/process, respectively.
*   `PPT` likely refers to $P/P_0$
*   `TTT` likely refers to $T/T_0$
*   `RRT` likely refers to $\rho/\rho_0$
*   `AAS` likely refers to $A/A^*$
*   `MS` likely refers to $M^*$ (Mach number relative to sonic speed $a^*$)
*   `C` likely refers to Crocco number $v/v_{max}$
*   `NU` refers to Prandtl-Meyer function $\nu(M)$
*   `DL` likely refers to $\delta$, the flow deflection angle $\theta$
*   `TH` likely refers to $\theta$, the flow deflection angle

## 1. Normal Shock Procedure (NSW)

This procedure calculates downstream conditions (2) given upstream conditions (1) across a normal shock wave. The upstream flow must be supersonic ($M_1 > 1$).

**Key Equations (Rankine-Hugoniot relations):**

*   **Mach Number:**
    $$ M_2^2 = \frac{M_1^2 + \frac{2}{\gamma - 1}}{\frac{2\gamma}{\gamma - 1}M_1^2 - 1} $$ 
    (Note: $M_2$ will always be subsonic, $M_2 < 1$)

*   **Static Pressure Ratio:**
    $$ \frac{P_2}{P_1} = 1 + \frac{2\gamma}{\gamma + 1}(M_1^2 - 1) $$ 

*   **Static Temperature Ratio:**
    $$ \frac{T_2}{T_1} = \frac{P_2}{P_1} \frac{\rho_1}{\rho_2} = \left[ 1 + \frac{2\gamma}{\gamma + 1}(M_1^2 - 1) \right] \frac{1 + \frac{\gamma - 1}{2}M_2^2}{1 + \frac{\gamma - 1}{2}M_1^2} = \frac{\left(1 + \frac{\gamma-1}{2}M_1^2\right) \left(\frac{2\gamma}{\gamma-1}M_1^2 - 1\right)}{\frac{(\gamma+1)^2}{2(\gamma-1)} M_1^2} $$ 

*   **Density Ratio (Velocity Ratio):**
    $$ \frac{\rho_2}{\rho_1} = \frac{V_1}{V_2} = \frac{(\gamma + 1)M_1^2}{(\gamma - 1)M_1^2 + 2} $$ 

*   **Stagnation Pressure Ratio (Entropy Increase):**
    $$ \frac{P_{02}}{P_{01}} = \left[ \frac{(\gamma + 1)M_1^2}{(\gamma - 1)M_1^2 + 2} \right]^{\frac{\gamma}{\gamma - 1}} \left[ \frac{\gamma + 1}{2\gamma M_1^2 - (\gamma - 1)} \right]^{\frac{1}{\gamma - 1}} $$ 
    (Note: $P_{02} < P_{01}$ due to entropy increase across the shock)

*   **Stagnation Temperature Ratio:**
    $$ \frac{T_{02}}{T_{01}} = 1 $$ (Adiabatic flow)

**Procedure Logic (based on Appendix A `NSW(N,v)`):**
Appendix A isn't fully detailed for NSW, but typically, you'd provide an input like $M_1$ (Case N=1, v=M1) and calculate $M_2$, $P_2/P_1$, $T_2/T_1$, $\rho_2/\rho_1$, $P_{02}/P_{01}$. Other cases (N) might involve providing $P_2/P_1$ or $M_2$ and finding $M_1$ and other ratios, which requires solving the equations implicitly.

## 2. Oblique Shock Procedure (OSW)

This procedure calculates conditions across an oblique shock wave formed when supersonic flow ($M_1 > 1$) is turned into itself by an angle $\theta$. The shock wave makes an angle $\beta$ with the upstream flow direction.

**Key Equations:**

*   Relate to Normal Shock: The normal component of the Mach number upstream ($M_{n1}$) determines the shock properties.
    $$ M_{n1} = M_1 \sin\beta $$ 
The normal component downstream ($M_{n2}$) is found using the normal shock relation for $M_{n1}$:
    $$ M_{n2}^2 = \frac{M_{n1}^2 + \frac{2}{\gamma - 1}}{\frac{2\gamma}{\gamma - 1}M_{n1}^2 - 1} = \frac{(M_1 \sin\beta)^2 + \frac{2}{\gamma - 1}}{\frac{2\gamma}{\gamma - 1}(M_1 \sin\beta)^2 - 1} $$ 
*   **Downstream Mach Number ($M_2$):** The tangential component of Mach number is conserved ($M_{t1} = M_{t2}$). 
    $$ M_{t1} = M_1 \cos\beta $$ 
    $$ M_2 = \frac{M_{n2}}{\sin(\beta - \theta)} $$ 
    Alternatively, using $M_2^2 = M_{n2}^2 + M_{t2}^2 = M_{n2}^2 + (M_1 \cos\beta)^2$. 

*   **Static Pressure Ratio:** Same as normal shock based on $M_{n1}$.
    $$ \frac{P_2}{P_1} = 1 + \frac{2\gamma}{\gamma + 1}(M_{n1}^2 - 1) = 1 + \frac{2\gamma}{\gamma + 1}(M_1^2 \sin^2\beta - 1) $$ 

*   **Static Temperature Ratio:** Same as normal shock based on $M_{n1}$.
    $$ \frac{T_2}{T_1} = \frac{\left(1 + \frac{\gamma-1}{2}M_{n1}^2\right) \left(\frac{2\gamma}{\gamma-1}M_{n1}^2 - 1\right)}{\frac{(\gamma+1)^2}{2(\gamma-1)} M_{n1}^2} $$ 

*   **Density Ratio:** Same as normal shock based on $M_{n1}$.
    $$ \frac{\rho_2}{\rho_1} = \frac{(\gamma + 1)M_{n1}^2}{(\gamma - 1)M_{n1}^2 + 2} $$ 

*   **Stagnation Pressure Ratio:** Same as normal shock based on $M_{n1}$.
    $$ \frac{P_{02}}{P_{01}} = \left[ \frac{(\gamma + 1)M_{n1}^2}{(\gamma - 1)M_{n1}^2 + 2} \right]^{\frac{\gamma}{\gamma - 1}} \left[ \frac{\gamma + 1}{2\gamma M_{n1}^2 - (\gamma - 1)} \right]^{\frac{1}{\gamma - 1}} $$ 

*   **Theta-Beta-Mach Relation ($	heta$-$\beta$-$M$):** Relates deflection angle $\theta$, shock angle $\beta$, and upstream Mach number $M_1$. 
    $$ \tan\theta = 2 \cot\beta \frac{M_1^2 \sin^2\beta - 1}{M_1^2 (\gamma + \cos(2\beta)) + 2} $$ 
    This equation is crucial. Given two variables (e.g., $M_1$, $\theta$), the third ($\beta$) can be found. For a given $M_1$ and $\theta$, there can be two possible $\beta$ values (weak and strong shock solutions), or no solution if $\theta$ exceeds $\theta_{max}$ for that $M_1$. There is also a minimum $\beta = \mu_1 = \arcsin(1/M_1)$ (Mach angle).

**Procedure Logic (based on Appendix A `OSW(N,v1,v2)`):**
Appendix A lists 11 cases. Examples:
*   Case N=7 ($M_1$, $\theta$ given): Solve $\theta$-$\beta$-$M$ for $\beta$ (usually the weak solution is physically relevant unless specified). Then calculate $M_2$, $P_2/P_1$, $T_2/T_1$, $P_{02}/P_{01}$.
*   Case N=9 ($\beta$, $\theta$ given): Solve $\theta$-$\beta$-$M$ for $M_1$. Then calculate $M_2$, etc.
*   Case N=1 ($M_1$, $\beta$ given): Calculate $\theta$ from $\theta$-$\beta$-$M$. Then calculate $M_2$, etc.

## 3. Prandtl-Meyer Angle Procedure (PMA)

This procedure calculates the Prandtl-Meyer function $\nu(M)$, which represents the angle through which a sonic flow ($M=1$) must be turned isentropically to reach Mach number $M$. It's used for isentropic supersonic expansions or compressions.

**Key Equation:**
$$ \nu(M) = \sqrt{\frac{\gamma+1}{\gamma-1}} \arctan\left( \sqrt{\frac{\gamma-1}{\gamma+1}(M^2-1)} \right) - \arctan\left( \sqrt{M^2-1} \right) $$ 
(Note: $\nu$ is typically calculated in radians, convert to degrees if needed. $\nu(1) = 0$. Requires $M \ge 1$.)

**Procedure Logic (based on Appendix A `PMA(N,v)`):**
*   Case N=1 ($M$ given): Calculate $\nu(M)$ using the formula.
*   Case N=2 ($\nu$ given): Solve the equation implicitly for $M$. This usually requires a numerical root-finding method.

## 4. Prandtl-Meyer Flow Procedure (PMF)

This procedure relates conditions before (1) and after (2) an isentropic supersonic turn (expansion or compression) through an angle $\Delta\theta$. The flow must be supersonic ($M_1, M_2 \ge 1$).

**Key Equations:**

*   **Angle Relationship:**
    *   Expansion turn: $\theta_2 = \theta_1 + \Delta\theta \implies \nu(M_2) = \nu(M_1) + \Delta\theta$
    *   Compression turn: $\theta_2 = \theta_1 - \Delta\theta \implies \nu(M_2) = \nu(M_1) - \Delta\theta$
    (Here $\Delta\theta$ is the magnitude of the turn angle, assumed positive. $\theta_1, \theta_2$ are flow angles relative to some reference.)

*   **Isentropic Relations:** Since the process is isentropic, stagnation conditions are constant ($P_{02}=P_{01}$, $T_{02}=T_{01}$). Static properties are related through the isentropic flow equations based on $M_1$ and $M_2$:
    $$ \frac{P_2}{P_1} = \frac{P_2/P_{02}}{P_1/P_{01}} = \frac{(1 + \frac{\gamma-1}{2}M_1^2)^{\frac{\gamma}{\gamma-1}}}{(1 + \frac{\gamma-1}{2}M_2^2)^{\frac{\gamma}{\gamma-1}}} $$ 
    $$ \frac{T_2}{T_1} = \frac{T_2/T_{02}}{T_1/T_{01}} = \frac{1 + \frac{\gamma-1}{2}M_1^2}{1 + \frac{\gamma-1}{2}M_2^2} $$ 
    $$ \frac{\rho_2}{\rho_1} = \frac{\rho_2/\rho_{02}}{\rho_1/\rho_{01}} = \frac{(1 + \frac{\gamma-1}{2}M_1^2)^{\frac{1}{\gamma-1}}}{(1 + \frac{\gamma-1}{2}M_2^2)^{\frac{1}{\gamma-1}}} $$ 

**Procedure Logic (based on Appendix A `PMF(N,v1,v2)`):**
Appendix A lists 6 cases. Examples:
*   Case N=1 ($M_1$, $\Delta\theta$ given): Calculate $\nu(M_1)$ using PMA. Calculate $\nu(M_2) = \nu(M_1) \pm \Delta\theta$. Solve for $M_2$ from $\nu(M_2)$ (implicitly, using PMA logic for N=2). Calculate $P_2/P_1$, $T_2/T_1$ using isentropic relations.
*   Case N=3 ($M_1$, $M_2$ given): Calculate $\nu(M_1)$ and $\nu(M_2)$ using PMA. Find $\Delta\theta = |\nu(M_2) - \nu(M_1)|$. Calculate $P_2/P_1$, $T_2/T_1$.
*   Case N=2 ($M_1$, $P_2/P_1$ given): Use the isentropic pressure ratio formula to solve for $M_2$. Calculate $\nu(M_1)$ and $\nu(M_2)$ using PMA. Find $\Delta\theta = |\nu(M_2) - \nu(M_1)|$. Calculate $T_2/T_1$.

These outlines provide the fundamental equations and logic required to implement the gas dynamics procedures requested in Problem 1.1, focusing on the hand-calculable aspects. Python code implementing these procedures can be provided separately if desired.


