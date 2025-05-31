# Table for Problem 1.4: Discussion of Loss Measures

| Loss Measure                  | Description                                                                 | Formulation (Examples)                                                                 | Application Context                     |
|-------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------|
| **Total Pressure Loss**       | Decrease in stagnation pressure due to irreversibilities (friction, shocks). | $\Delta P_0 = P_{0,in} - P_{0,out}$                                                    | Diffusers, Nozzles, Ducts, Shocks       |
| **Total Pressure Recovery**   | Ratio of outlet to inlet stagnation pressure. Measures efficiency.          | $\eta_{PR} = P_{0,out} / P_{0,in}$                                                     | Diffusers (Inlets)                      |
| **Entropy Increase**          | Fundamental measure of irreversibility based on the Second Law.             | $\Delta S = S_{out} - S_{in} > 0$ (for irreversible processes)                        | All irreversible flows (Shocks, Friction) |
| **Isentropic Efficiency**     | Ratio of actual work/energy transfer to the ideal (isentropic) equivalent.  | $\eta_{isen, comp} = \frac{h_{0,out,isen} - h_{0,in}}{h_{0,out,actual} - h_{0,in}}$ (Compressor) | Turbomachinery (Compressors, Turbines)  |
| **Nozzle Velocity Coefficient** | Ratio of actual exit velocity to ideal (isentropic) exit velocity.          | $C_v = V_{e,actual} / V_{e,isen}$                                                      | Nozzles                                 |
| **Nozzle Efficiency**         | Ratio of actual exit kinetic energy to ideal exit kinetic energy.           | $\eta_{nozzle} = V_{e,actual}^2 / V_{e,isen}^2 = C_v^2$                               | Nozzles                                 |
| **Discharge Coefficient**     | Ratio of actual mass flow rate to ideal mass flow rate.                     | $C_d = \dot{m}_{actual} / \dot{m}_{ideal}$                                           | Nozzles, Orifices                       |
| **Friction Factor (f)**       | Dimensionless parameter characterizing wall friction losses in ducts.       | Darcy: $h_L = f \frac{L}{D} \frac{V^2}{2g}$; Fanning: $f_{Fanning} = f_{Darcy}/4$       | Duct Flow (Fanno Flow)                  |
| **Drag Coefficient ($C_D$)**  | Dimensionless measure of aerodynamic drag caused by shape and friction.     | $C_D = Drag / (0.5 \rho V^2 A_{ref})$                                                 | External Aerodynamics, Inlet Spillage |

