# Problem 3.1: Governing Equations and Waves (Multiple Choice)

This problem consists of multiple-choice questions related to governing equations and wave phenomena in compressible flow. The answers and justifications are provided below.

**(Note: The actual multiple-choice options were not provided in the PDF text extraction or visible during the browser review. The following answers are based on typical questions related to these topics.)**

**Assumed Question 1: Governing Equations for Inviscid, Compressible Flow**

*   **Likely Correct Answer:** The set comprising the Continuity Equation, the Euler Equations (Momentum), the Energy Equation, and the Equation of State.
*   **Justification:**
    *   **Continuity Equation:** Represents conservation of mass. For steady flow, $\nabla \cdot (\rho \mathbf{V}) = 0$.
    *   **Euler Equations:** Represent conservation of momentum for an inviscid fluid. $\rho (\mathbf{V} \cdot \nabla) \mathbf{V} = -\nabla P$. (Ignoring body forces).
    *   **Energy Equation:** Represents conservation of energy. For adiabatic flow, the steady flow energy equation often simplifies to $h + \frac{1}{2}V^2 = h_0 = \text{constant}$ (where $h$ is specific enthalpy, $h_0$ is stagnation enthalpy).
    *   **Equation of State:** Relates thermodynamic properties. For an ideal gas, $P = \rho R T$.
    *   **Why others are incorrect:** The Navier-Stokes equations include viscous terms and are used for *viscous* compressible flow. Simplified forms like potential flow equations have additional assumptions (e.g., irrotationality).

**Assumed Question 2: Characteristics of Wave Types**

*   **Likely Correct Answer Statement (Example):** "Oblique shock waves cause a decrease in stagnation pressure and an increase in entropy, while Prandtl-Meyer expansion waves are isentropic."
*   **Justification:**
    *   **Mach Waves:** Infinitesimal disturbances propagating at the Mach angle $\mu = \arcsin(1/M)$ in supersonic flow ($M \ge 1$). They are isentropic and cause negligible changes in flow properties.
    *   **Prandtl-Meyer Expansion Waves:** A continuous series of Mach waves that turn a supersonic flow around a convex corner, causing the Mach number to increase and static pressure, temperature, and density to decrease. The process is isentropic ($P_0$ and $S$ remain constant).
    *   **Shock Waves (Normal or Oblique):** Formed by the coalescence of compression waves or when supersonic flow is abruptly turned into itself (concave corner or deflection). They involve finite, discontinuous changes in properties. The process is non-isentropic, resulting in an increase in entropy ($S_2 > S_1$) and a decrease in stagnation pressure ($P_{02} < P_{01}$). Static pressure, temperature, and density increase across the shock, while Mach number decreases (becoming subsonic after a normal shock, or lower supersonic/subsonic after an oblique shock).

**Assumed Question 3: Property Changes Across Waves**

*   **Likely Correct Answer Statement (Example):** "Across a normal shock wave, static pressure increases, static temperature increases, density increases, Mach number decreases, and stagnation pressure decreases."
*   **Justification:**
    *   **Normal Shock:** Governed by Rankine-Hugoniot relations. For $M_1 > 1$: $M_2 < 1$, $P_2/P_1 > 1$, $T_2/T_1 > 1$, $\rho_2/\rho_1 > 1$, $P_{02}/P_{01} < 1$, $S_2 > S_1$.
    *   **Oblique Shock:** Similar qualitative changes in static properties ($P, T, \rho$ increase) and entropy ($S$ increases, $P_0$ decreases) based on the normal component $M_{n1} = M_1 \sin\beta$. The downstream Mach number $M_2$ is less than $M_1$ but can still be supersonic if the shock is weak.
    *   **Expansion Wave:** Governed by Prandtl-Meyer function and isentropic relations. For an expansion turn: $M_2 > M_1$, $P_2/P_1 < 1$, $T_2/T_1 < 1$, $\rho_2/\rho_1 < 1$, $P_{02}/P_{01} = 1$, $S_2 = S_1$.

**Conclusion:**
To definitively answer Problem 3.1, the specific multiple-choice questions and options from the original PDF are required. The justifications above cover the fundamental principles needed to evaluate such questions.
