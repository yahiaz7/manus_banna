# Problems 1.6 - 1.10: Duct Geometry Changes

Problems [6] through [10] in Section 1 are listed as headings without specific questions. Based on the context of "Review of Internal Flows" and the preceding problems discussing losses and pressure recovery, these likely refer to standard internal flow elements involving area changes. We will discuss the key flow phenomena and loss characteristics associated with each.

**General Concepts:**
Changes in duct cross-sectional area cause changes in fluid velocity and pressure. These changes are associated with energy losses (conversion of mechanical energy to heat) due to friction and flow separation, especially in diffusing (area increasing) sections or abrupt changes.

## [6] Gradual Enlargement (Diffuser)

*   **Description:** A duct section where the cross-sectional area increases gradually in the direction of flow.
*   **Function:** To decelerate the flow and increase static pressure (pressure recovery).
*   **Flow Phenomena:** As the area increases, the flow slows down (for subsonic flow). This creates an adverse pressure gradient (pressure increasing downstream). The boundary layer is sensitive to this gradient and can thicken significantly or separate if the divergence angle is too large.
*   **Losses:** Losses arise from wall friction and potential flow separation (form drag/turbulence in separated regions). Diffuser efficiency ($\\eta_D$) quantifies the effectiveness of pressure recovery compared to an ideal isentropic process. Losses are minimized by using a small divergence angle (typically < 7-10 degrees total angle) to prevent separation, but this increases the diffuser length and thus wall friction losses. There is an optimal angle for maximum pressure recovery.
*   **Loss Coefficient ($K_L$):** Depends strongly on the divergence angle and area ratio. $K_L$ is minimized at small angles but increases sharply if separation occurs at larger angles.

## [7] Gradual Contraction (Nozzle)

*   **Description:** A duct section where the cross-sectional area decreases gradually in the direction of flow.
*   **Function:** To accelerate the flow and decrease static pressure.
*   **Flow Phenomena:** As the area decreases, the flow accelerates (for subsonic flow). This creates a favorable pressure gradient (pressure decreasing downstream). Favorable gradients tend to stabilize the boundary layer, making separation unlikely.
*   **Losses:** Losses are primarily due to wall friction. Because the flow is accelerating and separation is generally avoided, losses in gradual contractions (nozzles) are typically much lower than in gradual enlargements (diffusers) of similar geometry.
*   **Loss Coefficient ($K_L$):** Generally small, mainly dependent on the length and surface finish.

## [8] Sudden Enlargement

*   **Description:** An abrupt increase in duct cross-sectional area.
*   **Function:** Sometimes used for mixing or energy dissipation, but generally represents a significant source of loss in pipe systems.
*   **Flow Phenomena:** As the flow exits the smaller pipe into the larger one, it cannot follow the sharp corner. The jet expands, forming a separated region with recirculating eddies in the corner. Intense mixing and turbulence occur as the jet expands to fill the larger pipe downstream.
*   **Losses:** Significant head loss occurs due to the turbulent dissipation of kinetic energy in the separated region and subsequent mixing. This loss can be calculated using momentum and energy balances (Borda-Carnot equation for incompressible flow).
*   **Loss Coefficient ($K_L$):** Can be calculated theoretically for incompressible flow based on the area ratio ($A_1/A_2$): $K_L = (1 - A_1/A_2)^2$, based on the upstream velocity ($v_1$). This loss is often substantial.

## [9] Sudden Contraction

*   **Description:** An abrupt decrease in duct cross-sectional area.
*   **Function:** Often unavoidable in pipe systems but represents a source of loss.
*   **Flow Phenomena:** As the flow approaches the smaller pipe entrance, the streamlines converge. The flow separates from the sharp corner, forming a vena contracta (minimum flow area) slightly downstream of the entrance to the smaller pipe. After the vena contracta, the flow expands again to fill the smaller pipe, accompanied by turbulent mixing and energy dissipation.
*   **Losses:** Losses occur primarily due to the turbulent dissipation during the expansion downstream of the vena contracta.
*   **Loss Coefficient ($K_L$):** Depends on the area ratio ($A_2/A_1$). For incompressible flow, $K_L$ (based on downstream velocity $v_2$) is typically around 0.5 for a sharp-edged entrance ($A_1 \gg A_2$) and decreases as the area ratio approaches 1 or if the entrance is rounded.

## [10]

*   **Description:** This item appears only as the number "[10]" in the problem sheet text, with no associated title or question.
*   **Action:** No action can be taken as no problem or topic is specified.

These descriptions cover the fundamental aspects of flow through these common duct geometry changes and their associated loss mechanisms.
