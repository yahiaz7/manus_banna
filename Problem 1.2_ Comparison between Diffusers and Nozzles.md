# Problem 1.2: Comparison between Diffusers and Nozzles

This problem asks for a comparison between diffusers and nozzles based on several criteria, presented in a table format.

**Fundamental Definitions:**
*   **Nozzle:** A device designed to accelerate a fluid flow, converting thermal or pressure energy into kinetic energy.
*   **Diffuser:** A device designed to decelerate a fluid flow (increase pressure), converting kinetic energy into pressure energy.

The behavior (acceleration/deceleration) depends on the Mach number regime (subsonic or supersonic) and the area change.

**Comparison Table:**

| Criterion                       | Nozzle                                                                                                | Diffuser                                                                                                    |
| :------------------------------ | :---------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **Function**                    | Increase fluid kinetic energy (velocity/Mach number) at the expense of pressure/thermal energy.       | Increase fluid pressure (pressure recovery) at the expense of kinetic energy.                               |
| **Action and Goal**             | Action: Accelerate flow. Goal: Generate thrust (e.g., rockets, jets), achieve high exit velocity.       | Action: Decelerate flow. Goal: Increase static pressure efficiently, reduce velocity for combustion/mixing. |
| **Flow Stability**              | Generally more stable, especially convergent sections. Supersonic nozzles can have complex shock structures (over/under-expanded). | Prone to flow separation and instabilities, especially with adverse pressure gradients. Requires careful design. |
| **Design Objectives**           | Maximize exit kinetic energy/thrust, minimize total pressure loss, achieve desired exit Mach number.    | Maximize static pressure recovery, minimize total pressure loss, achieve desired exit velocity/pressure.      |
| **Type (based on M_Inlet)**     | *Subsonic Inlet (M < 1):* Convergent area. *Supersonic Inlet (M > 1):* Divergent area.                 | *Subsonic Inlet (M < 1):* Divergent area. *Supersonic Inlet (M > 1):* Convergent area.                     |
| **Area Change (Primary Action)** | *Subsonic Flow:* Area decreases (Convergent). *Supersonic Flow:* Area increases (Divergent).           | *Subsonic Flow:* Area increases (Divergent). *Supersonic Flow:* Area decreases (Convergent).               |
| **Sketch (Typical)**            | Convergent or Convergent-Divergent (Laval) shape.                                                     | Divergent or Convergent-Divergent shape (often inlet part of engines).                                      |
| **Velocity/Mach Changes**       | Velocity/Mach number increases through the primary action section.                                    | Velocity/Mach number decreases through the primary action section.                                        |
| **Pressure/Temp/Density Changes** | Static Pressure, Temperature, and Density decrease through the primary action section.                  | Static Pressure, Temperature, and Density increase through the primary action section.                      |
| **Shock Waves**                 | Can occur in supersonic nozzles (e.g., over-expanded flow, start-up) or C-D nozzles if back pressure is incorrect. | Can occur in supersonic diffusers (required for deceleration, e.g., normal/oblique shocks in inlets).         |
| **Flow Separation**             | Less common in convergent sections. Can occur in divergent sections if expansion angle is too large or flow is over-expanded. | Major concern due to adverse pressure gradient. Limits diffuser angle and efficiency.                         |
| **Design Complexity**           | Convergent nozzles are simple. C-D nozzles require careful throat and contour design, especially for supersonic flow. | Generally more complex due to stability issues and boundary layer control needs. Supersonic diffusers are very complex. |
| **Efficiency (Isentropic)**     | Typically high (90-99%), measures effectiveness in converting pressure to kinetic energy ($\\eta_N$).     | Lower than nozzles (60-90%), measures effectiveness in pressure recovery ($\\eta_D$). Limited by separation/losses. |
| **Applications**                | Rocket engines, jet engine exhausts, wind tunnels (test section acceleration), turbines, flow measurement (Venturi). | Jet engine inlets, wind tunnels (settling chamber), compressors, ejectors, flow measurement (Venturi).      |

**Note on Area Change and Mach Number:**
The relationship between area change and velocity change reverses at Mach 1:
*   **Subsonic (M < 1):** dA > 0 $\implies$ dV < 0 (Diffuser); dA < 0 $\implies$ dV > 0 (Nozzle)
*   **Supersonic (M > 1):** dA > 0 $\implies$ dV > 0 (Nozzle); dA < 0 $\implies$ dV < 0 (Diffuser)
