# Problem 3.8: Flow in Corner Duct

**Problem Statement:**
Consider supersonic flow ($M_1 = 3.0$) entering a duct that has a sharp $90^\circ$ corner. Describe the flow pattern, including the types of waves formed and the resulting flow conditions in different regions. Assume air with $\gamma = 1.4$.

**Scenario:**
A uniform supersonic flow ($M_1=3.0$) approaches a sharp internal $90^\circ$ corner formed by two perpendicular walls.

**Approach:**
The sharp corner forces the supersonic flow to turn abruptly. This cannot happen isentropically. The flow pattern will involve shock waves originating from the corner.

**Flow Pattern Description:**

1.  **Initial Flow (Region 1):** Uniform supersonic flow with $M_1 = 3.0$, parallel to the initial wall (let's assume horizontal).

2.  **Corner Interaction:** When the flow encounters the sharp $90^\circ$ corner, it cannot turn smoothly. A complex shock wave pattern forms, originating from the corner vertex.

3.  **Reflected Shock Pattern:** The most common pattern involves an oblique shock wave originating from the corner, reflecting off the opposite wall. However, for a sharp $90^\circ$ internal corner with high Mach number flow, a simple reflection is often insufficient to turn the flow parallel to the second wall. A more complex pattern, often involving a Mach reflection, is likely.

    *   **Simplified View (Oblique Shock):** If we first consider the flow interacting with the vertical wall, it would need to turn $90^\circ$. This turn angle is far too large for an attached oblique shock to exist for $M_1=3.0$. The maximum deflection angle for $M=3.0$ is $\theta_{max} \approx 34^\circ$. Therefore, the shock must detach, forming a strong, curved **bow shock** standing off some distance from the corner.

    *   **Detailed Corner Flow:** The flow right at the corner is complex. An oblique shock will form from the corner, propagating outwards. Let's analyze the interaction with the horizontal wall first, turning upwards towards the vertical wall.
        *   An oblique shock (Shock 1) forms at the corner, propagating upwards and away from the horizontal wall. This shock turns the flow upwards by some angle $\delta_1$. The flow behind this shock (Region 2) has $M_2 < M_1$.
        *   Simultaneously, the flow must turn parallel to the vertical wall. This requires another shock (Shock 2) originating from the corner, propagating horizontally away from the vertical wall, turning the flow parallel to the vertical wall by $\delta_2$. The flow behind this shock (Region 3) has $M_3 < M_1$.
        *   These two shocks (and potentially expansion waves if the corner geometry is slightly different) interact. A slip line will likely form downstream, separating flow that passed through Shock 1 from flow that passed through Shock 2.
        *   **Mach Reflection Possibility:** Given the large turning angle ($90^\circ$) and high Mach number ($M=3.0$), it's highly probable that regular reflection of shocks cannot occur. Instead, a **Mach reflection** pattern is expected near the corner. This involves an incident shock, a reflected shock, a Mach stem (a normal or near-normal shock section), and a slip line, all meeting at a triple point.

4.  **Resulting Flow:**
    *   The flow downstream of the complex shock structure near the corner will be highly non-uniform.
    *   There will be regions of subsonic flow (especially behind the Mach stem if formed).
    *   Significant stagnation pressure losses will occur due to the strong shock waves.
    *   The flow will eventually adjust to be parallel to the duct walls far downstream, but likely with reduced Mach number and non-uniform properties.

**Hand-Calculable Aspects (Simplified Analysis):**
While the full pattern is complex, we can analyze parts:
*   **Maximum Deflection:** As noted, $\theta_{max}(M=3.0) \approx 34^\circ$. A single oblique shock cannot turn the flow $90^\circ$.
*   **Normal Shock:** If a normal shock (Mach stem) forms, the conditions behind it can be calculated. For $M_1=3.0$:
    *   $M_2 \approx 0.475$ (Subsonic)
    *   $P_2/P_1 \approx 10.33$
    *   $T_2/T_1 \approx 2.679$
    *   $P_{02}/P_{01} \approx 0.328$

**Conclusion:**
Supersonic flow ($M=3.0$) encountering a sharp $90^\circ$ internal corner results in a complex flow pattern dominated by strong shock waves. Due to the large required turning angle exceeding the maximum possible deflection for an attached oblique shock, a detached **bow shock** or a complex interaction involving **Mach reflection** near the corner is expected. The flow downstream will be non-uniform, involve significant stagnation pressure loss, and likely contain regions of subsonic flow.

**Equations Used (for reference):**
*   Oblique Shock Relations ($\theta$-$\beta$-$M$)
*   Normal Shock Relations (Rankine-Hugoniot)
*   Maximum Deflection Angle Calculation

*(Note: A precise description and calculation require advanced gas dynamics analysis or computational fluid dynamics (CFD) simulation due to the complexity of the shock interactions and potential Mach reflection.)*
