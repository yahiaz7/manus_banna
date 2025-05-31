# Problem 3.2: Wave Interaction - Hodograph/Physical Plane

**Problem Statement:**
Sketch the interaction of two shock waves in the physical plane and the hodograph plane.

**Scenario:**
Consider a symmetric scenario where a uniform supersonic flow ($M_1 > 1$) encounters two opposing wedges of equal angle $\delta$, or equivalently, the leading edge of a symmetric diamond airfoil at zero angle of attack. This generates two symmetric oblique shock waves (Shock 1 and Shock 2) which intersect downstream.

**1. Physical Plane Sketch:**

*   **Region 1:** Uniform supersonic flow with Mach number $M_1$, pressure $P_1$, temperature $T_1$, flowing horizontally (angle $\theta_1 = 0$).
*   **Wedges/Corners:** Two surfaces deflect the flow inwards by an angle $\delta$. Shock 1 originates from the upper corner, Shock 2 from the lower corner.
*   **Shock Waves 1 & 2:** These are oblique shocks, making an angle $\beta$ with the initial flow direction. They are symmetric.
*   **Region 2:** Flow downstream of Shock 1. The flow is deflected downwards by angle $\delta$ ($\\theta_2 = -\delta$). The Mach number is $M_2 < M_1$, pressure $P_2 > P_1$, temperature $T_2 > T_1$, stagnation pressure $P_{02} < P_{01}$.
*   **Region 3:** Flow downstream of Shock 2. The flow is deflected upwards by angle $\delta$ ($\\theta_3 = +\delta$). By symmetry, $M_3 = M_2$, $P_3 = P_2$, $T_3 = T_2$, $P_{03} = P_{02}$.
*   **Intersection Point (P):** Shocks 1 and 2 intersect at point P.
*   **Transmitted Waves:** From point P, two transmitted waves emerge. Since the flow entering the interaction from Region 2 and Region 3 must be turned back towards the centerline to satisfy pressure and flow direction continuity downstream, these transmitted waves are typically also oblique shocks (Shock 1' and Shock 2').
    *   Shock 1' interacts with flow from Region 3.
    *   Shock 2' interacts with flow from Region 2.
*   **Slip Line (SL):** Also originating from point P, a slip line separates the flow that passed through (Shock 1 $\to$ Shock 2') from the flow that passed through (Shock 2 $\to$ Shock 1'). Across the slip line, static pressure and flow direction are equal ($P_4 = P_5$, $\theta_4 = \theta_5$), but velocity magnitude, temperature, density, Mach number, and stagnation pressure are generally different ($V_4 \neq V_5$, $T_4 \neq T_5$, $\rho_4 \neq \rho_5$, $M_4 \neq M_5$, $P_{04} \neq P_{05}$). The slip line is a contact discontinuity.
*   **Region 4:** Flow downstream of Shock 2'. Flow angle $\theta_4 = 0$ (by symmetry).
*   **Region 5:** Flow downstream of Shock 1'. Flow angle $\theta_5 = 0$ (by symmetry).
*   **Symmetry:** The entire interaction pattern is symmetric about the centerline.

*(A visual sketch would show the initial flow, the wedges, the converging incident shocks, the intersection point, the diverging transmitted shocks, and the horizontal slip line downstream.)*

**2. Hodograph Plane Sketch:**

The hodograph plane plots velocity components, typically $u$ (horizontal) and $v$ (vertical). A point represents the tip of the velocity vector originating from the origin.

*   **Point 1:** Represents the velocity vector $\mathbf{V}_1$ of the initial flow. $u_1 = V_1$, $v_1 = 0$. Magnitude $V_1 = M_1 a_1$.
*   **$M_1$ Shock Polar:** Draw the shock polar curve corresponding to the upstream Mach number $M_1$. All possible states downstream of an oblique shock originating from state 1 lie on this curve.
*   **Point 2:** Shock 1 deflects the flow by $\theta_2 = -\delta$. Find the point on the $M_1$ polar where the line from the origin makes an angle $-\delta$ with the u-axis. This is point 2, representing $\mathbf{V}_2$. $V_2 < V_1$.
*   **Point 3:** Shock 2 deflects the flow by $\theta_3 = +\delta$. Find the point on the $M_1$ polar where the line from the origin makes an angle $+\delta$ with the u-axis. This is point 3, representing $\mathbf{V}_3$. By symmetry, $V_3 = V_2$.
*   **$M_2$ Shock Polar:** From point 2, draw the shock polar corresponding to Mach number $M_2$. States downstream of a shock originating from state 2 lie on this polar.
*   **$M_3$ Shock Polar:** From point 3, draw the shock polar corresponding to Mach number $M_3 (=M_2)$. States downstream of a shock originating from state 3 lie on this polar.
*   **Points 4 & 5:** The flow in regions 4 and 5 must have the same pressure ($P_4=P_5$) and the same flow direction ($\\theta_4 = \theta_5 = 0$ due to symmetry). Point 4 must lie on the $M_2$ polar, and point 5 must lie on the $M_3$ polar. Both points must lie on the horizontal axis ($v=0$) because the final flow direction is horizontal.
    *   Find point 4 on the $M_2$ polar such that the flow is turned from $\theta_2 = -\delta$ back to $\theta_4 = 0$. This corresponds to a turn of $+\delta$.
    *   Find point 5 on the $M_3$ polar such that the flow is turned from $\theta_3 = +\delta$ back to $\theta_5 = 0$. This corresponds to a turn of $-\delta$.
    *   By symmetry, points 4 and 5 will lie on the u-axis and satisfy $P_4=P_5$. They represent the velocity vectors $\mathbf{V}_4$ and $\mathbf{V}_5$. Generally, $V_4 = V_5$ only if the incident shocks were weak (isentropic compressions). For finite shocks, $V_4$ and $V_5$ might differ slightly, but the pressure and direction match.

*(A visual sketch in the u-v plane would show the origin, point 1 on the u-axis, the $M_1$ shock polar passing through points 2 and 3 (symmetric about the u-axis), the $M_2$ and $M_3$ polars originating from points 2 and 3 respectively, and points 4 and 5 located at the intersection of these polars with the u-axis.)*

**Key Concepts Illustrated:**
*   **Physical Plane:** Shows the geometric pattern of waves and regions.
*   **Hodograph Plane:** Maps velocity states and uses shock polars to graphically solve for downstream conditions across oblique shocks. The intersection of polars represents conditions satisfying multiple wave constraints.
*   **Slip Line:** Represents the boundary between fluid particles that have passed through different sequences of shocks, resulting in different thermodynamic states (temperature, density, entropy, stagnation pressure) but matched static pressure and flow direction.
