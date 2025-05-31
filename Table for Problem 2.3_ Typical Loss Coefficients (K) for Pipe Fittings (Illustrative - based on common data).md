# Table for Problem 2.3: Typical Loss Coefficients (K) for Pipe Fittings (Illustrative - based on common data)

| Fitting Type                  | K Value (Approximate Range) | Notes                                      |
|-------------------------------|-----------------------------|--------------------------------------------|
| **Entrances**                 |                             |                                            |
| - Sharp-edged (re-entrant)    | 0.8 - 1.0                   | Flow separates significantly               |
| - Sharp-edged (flush)         | 0.5                         |                                            |
| - Rounded (r/D > 0.15)        | 0.04 - 0.1                  | Smooth entry, minimal separation           |
| **Exits**                     |                             |                                            |
| - Sharp-edged                 | 1.0                         | All kinetic energy is lost                 |
| - Rounded                     | 1.0                         | Same as sharp-edged                        |
| **Bends & Elbows**            |                             | Depends on angle and radius (r/D)          |
| - 90° Smooth Bend (r/D=1)     | 0.3 - 0.4                   |                                            |
| - 90° Smooth Bend (r/D=2)     | 0.2 - 0.3                   | Larger radius reduces loss                 |
| - 90° Miter Bend (sharp)      | 1.1 - 1.3                   | High loss due to separation                |
| - 45° Smooth Bend (r/D=1)     | 0.15 - 0.2                  | Less turning, less loss                    |
| **Valves (Fully Open)**       |                             | Highly dependent on valve type             |
| - Gate Valve                  | 0.15 - 0.2                  | Relatively low loss when fully open        |
| - Globe Valve                 | 6 - 10                      | Tortuous path, high loss                   |
| - Angle Valve                 | 2 - 5                       |                                            |
| - Ball Valve                  | 0.05 - 0.1                  | Very low loss when fully open              |
| - Butterfly Valve             | 0.3 - 1.5                   | Depends on size and design                 |
| - Check Valve (Swing)         | 2 - 4                       |                                            |
| **Sudden Contraction**        |                             | Depends on area ratio ($A_2/A_1$)          |
| - $A_2/A_1 = 0.75$            | ~0.1                        |                                            |
| - $A_2/A_1 = 0.5$             | ~0.25                       |                                            |
| - $A_2/A_1 = 0.25$            | ~0.4                        |                                            |
| **Sudden Expansion**          |                             | $K = (1 - A_1/A_2)^2$                      |
| - $A_1/A_2 = 0.75$            | ~0.06                       | Based on downstream velocity head ($V_2^2/2g$) |
| - $A_1/A_2 = 0.5$             | ~0.25                       | Based on downstream velocity head ($V_2^2/2g$) |
| - $A_1/A_2 = 0.25$            | ~0.56                       | Based on downstream velocity head ($V_2^2/2g$) |

*Note: These values are approximate and can vary based on specific geometry, Reynolds number, and surface roughness. They are typically used with the head loss equation $h_L = K (V^2 / 2g)$. Appendix B in the original problem set would provide specific values to be used.*
