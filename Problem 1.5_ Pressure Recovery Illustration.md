# Problem 1.5: Pressure Recovery Illustration

This problem asks to illustrate the phenomenon of pressure recovery using two examples: internal flow in a Venturi and external flow over a cylinder.

**Concept of Pressure Recovery:**
Pressure recovery refers to the process where the static pressure of a fluid increases as its velocity decreases. This occurs when kinetic energy is converted back into potential energy in the form of pressure. This process is governed by Bernoulli's principle for ideal, inviscid flows, but in real flows, it is affected by viscous losses and flow separation.

**(a) Internal Flow in a Venturi:**

A Venturi meter consists of a converging section, a narrow throat, and a diverging section (diffuser).

1.  **Converging Section:** As the fluid enters the converging section, the area decreases. To maintain mass continuity, the fluid velocity increases. According to Bernoulli's equation ($P + \frac{1}{2} \rho v^2 = \text{constant}$ for inviscid, incompressible flow along a streamline), the increase in velocity (kinetic energy) is accompanied by a decrease in static pressure.
2.  **Throat:** The area is minimum, velocity is maximum, and static pressure is minimum at the throat.
3.  **Diverging Section (Diffuser):** As the fluid enters the diverging section, the area increases. The flow decelerates, converting kinetic energy back into pressure energy. This results in an increase in static pressure along the diverging section – this is **pressure recovery**.

**Illustration:**
*   **Ideal Flow (Inviscid):** In an ideal Venturi, the pressure would recover back to the initial inlet pressure if the exit area equals the inlet area and the flow remains attached and frictionless. The pressure profile would be symmetric (a drop followed by an equal rise).
*   **Real Flow (Viscous):** In a real Venturi, the diverging section acts as a diffuser. Diffusers are susceptible to adverse pressure gradients (pressure increasing in the flow direction), which can cause the boundary layer to thicken and potentially separate from the wall. Friction along the walls also causes irreversible losses.
    *   Due to friction and potential separation, the pressure recovery in the diverging section is always less than ideal. The exit static pressure will be lower than the inlet static pressure, even if the areas are the same.
    *   The efficiency of pressure recovery depends on the diffuser angle (gentle angles minimize separation but increase friction length) and the flow conditions (Reynolds number).

*Sketch Concept:* A plot of static pressure vs. distance along the Venturi axis would show: Pressure decreasing from inlet to throat, then increasing from throat towards the exit, but the final exit pressure is lower than the inlet pressure due to losses.

**(b) External Flow over a Cylinder:**

Consider uniform flow approaching a cylinder perpendicular to its axis.

1.  **Approach Flow & Stagnation Point:** As the fluid approaches the front of the cylinder, it decelerates along the stagnation streamline, reaching zero velocity at the front stagnation point. Here, kinetic energy is fully converted to pressure energy, and the static pressure reaches the stagnation pressure ($P_0$), which is the maximum pressure on the cylinder surface.
2.  **Flow Acceleration:** As the flow moves from the stagnation point around the curved surface towards the top/bottom, the effective flow area initially decreases (streamlines bunch together). The flow accelerates, and the static pressure drops, reaching a minimum value typically near the point of maximum thickness (90 degrees from the stagnation point for potential flow).
3.  **Flow Deceleration & Pressure Recovery:** Past the point of maximum thickness (top/bottom), the flow path effectively diverges. The fluid begins to decelerate along the rear surface of the cylinder. In an ideal (potential) flow, this deceleration would lead to an increase in static pressure, recovering back to the freestream pressure at the rear stagnation point. This ideal pressure recovery would result in zero net pressure drag (d'Alembert's Paradox).

**Illustration:**
*   **Ideal Flow (Potential Flow):** Pressure is high at the front stagnation point, decreases to a minimum at the sides (top/bottom), and recovers symmetrically to a high value at the rear stagnation point. The pressure distribution is symmetric front-to-back.
*   **Real Flow (Viscous):** The flow experiences an adverse pressure gradient on the rear half of the cylinder (pressure increasing in the flow direction). Viscosity causes a boundary layer to form.
    *   This adverse pressure gradient causes the boundary layer to slow down, thicken, and eventually **separate** from the surface, typically before reaching the rear stagnation point (separation point depends on Reynolds number).
    *   Flow separation creates a wide, low-pressure wake region behind the cylinder.
    *   Because the flow separates, the pressure on the rear surface does not recover significantly. The pressure remains low in the separated wake region.
    *   The asymmetry in pressure distribution (high pressure on the front, low pressure on the rear) results in a significant net force opposing the motion – this is **pressure drag** (or form drag).
    *   Therefore, in real flow over a cylinder, **pressure recovery on the rear surface is poor** due to flow separation, leading to substantial drag.

*Sketch Concept:* A plot of pressure coefficient ($C_p$) around the cylinder surface vs. angle would show: $C_p=1$ at the front stagnation point (0 deg), decreasing to negative values on the sides (around +/- 90 deg), and then *failing* to recover back to $C_p=1$ at the rear (180 deg) due to separation, instead staying at a low (negative) $C_p$ value over much of the rear surface.
