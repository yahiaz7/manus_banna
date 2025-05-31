# Problem 3.5: Supersonic Nozzle Design (Method of Characteristics)

**Problem Statement:**
Design a two-dimensional, planar supersonic nozzle using the method of characteristics (MOC). The nozzle should produce a uniform parallel flow at an exit Mach number $M_e = 2.0$. The throat half-height is $y_t = h_t/2 = 0.5 \, cm$. Determine the number of characteristic lines required, calculate the coordinates of the nozzle contour, and plot the contour and characteristic net. Assume $\gamma = 1.4$.

**Approach:**
We will use the method of characteristics for irrotational, isentropic, supersonic flow to design a minimum length nozzle contour.

**Key Concepts & Equations:**
*   **Prandtl-Meyer Function:** $\nu(M) = \sqrt{\frac{\gamma+1}{\gamma-1}} \arctan\left( \sqrt{\frac{\gamma-1}{\gamma+1}(M^2-1)} \right) - \arctan\left( \sqrt{M^2-1} \right)$
*   **Mach Angle:** $\mu = \arcsin(1/M)$
*   **Characteristic Compatibility Relations:**
    *   Along Right-Running ($C_+$) characteristics: $K_+ = \theta - \nu(M) = \text{constant}$
    *   Along Left-Running ($C_-$) characteristics: $K_- = \theta + \nu(M) = \text{constant}$
    *   $	heta$ is the local flow angle relative to the x-axis.
*   **Characteristic Slopes:**
    *   $C_+$ slope: $dy/dx = \tan(\theta + \mu)$
    *   $C_-$ slope: $dy/dx = \tan(\theta - \mu)$
*   **Minimum Length Nozzle Design:** The flow expands from $M=1$ at the throat through a centered Prandtl-Meyer expansion fan originating at the throat corner. The nozzle contour is shaped to cancel the expansion waves reflected from the centerline, producing uniform parallel flow ($\\theta=0$) at the desired exit Mach number $M_e$.
*   **Maximum Turning Angle:** The expansion fan turns the flow up to a maximum angle $\theta_{max} = \nu(M_e) / 2$.

**Step-by-Step Calculation (Hand-Calculable Parameters):**

1.  **Calculate Prandtl-Meyer Angle at Exit ($M_e = 2.0$, $\\gamma = 1.4$):**
    From standard tables or calculation (see Problem 3.3 example or use a calculator):
    $$ \nu(M=2.0) \approx 26.38^\circ $$ 

2.  **Calculate Maximum Wall Turning Angle:**
    For a minimum length nozzle producing parallel exit flow:
    $$ \theta_{max} = \frac{\nu(M_e)}{2} = \frac{26.38^\circ}{2} = 13.19^\circ $$ 
    This is the angle the nozzle wall makes with the axis immediately downstream of the throat corner.

3.  **Calculate Exit Area Ratio and Height:**
    We need the isentropic area ratio $A_e / A^*$ for $M_e = 2.0$.
    From standard tables or calculation (see Problem 3.4):
    $$ \frac{A_e}{A^*} \approx 1.6875 $$ 
    For a 2D planar nozzle, the area ratio is equal to the height ratio: $A_e/A^* = h_e/h_t = (2y_e)/(2y_t) = y_e/y_t$.
    $$ y_e = y_t \times \frac{A_e}{A^*} = (0.5 \, cm) \times 1.6875 = 0.84375 \, cm $$ 
    The exit half-height is $y_e = 0.84375 \, cm$.

4.  **Number of Characteristic Lines:**
    The number of lines ($N$) used in the characteristic network determines the resolution and accuracy of the calculated contour. This is a choice based on desired precision. For a hand-calculation sketch or a basic numerical implementation, choosing $N=4$ to $N=10$ characteristics in the initial fan is typical.
    *   Let's choose $N=5$ characteristics for illustration. This divides the fan angle $\theta_{max} = 13.19^\circ$ into 5 intervals.
    *   Angle step: $\Delta\theta = 13.19^\circ / 5 = 2.638^\circ$.
    *   The characteristics leaving the corner correspond to flow angles $\theta_k = k \times \Delta\theta$ for $k=0, 1, ..., 5$. These angles are $0^\circ, 2.638^\circ, 5.276^\circ, 7.914^\circ, 10.552^\circ, 13.19^\circ$.
    *   These are also the Prandtl-Meyer angles $\nu_k$ along these initial characteristics (since $K_+=0$ for the initial fan originating from $\theta=0, \nu=0$).
    *   We would need to find the Mach number $M_k$ corresponding to each $\nu_k$.

5.  **Calculation of Coordinates and Characteristic Net:**
    *   **Principle:** The method involves calculating the properties ($\\theta, M, \nu, \mu$) and coordinates $(x, y)$ at the intersection points of the $C_+$ and $C_-$ characteristics.
    *   **Starting Point:** Throat corner T = (0, 0.5 cm).
    *   **Initial Fan:** $N+1$ characteristics ($C_+$ lines) emanate from T with angles $\theta_k$ and Mach numbers $M_k$ (where $\nu(M_k)=\theta_k$). Along these lines, $K_+ = \theta_k - \nu_k = 0$.
    *   **Centerline Reflection:** These $C_+$ lines intersect the centerline ($y=0$, where $\theta=0$). At the intersection point $P_k$, the wave reflects as a $C_-$ characteristic. Along the reflected $C_-$ wave, $K_- = \theta + \nu = 0 + \nu(M_k) = \theta_k$.
    *   **Interior Points:** Calculate the intersection points $I_{kj}$ of the $k$-th reflected $C_-$ wave ($K_- = \theta_k$) and the $j$-th direct $C_+$ wave ($K_+ = 0$). At $I_{kj}$: $\theta = \theta_k / 2$ and $\nu = \theta_k / 2$. Find the corresponding $M$ and $\mu$. Calculate the coordinates $(x, y)$ by approximating segments as straight lines with slopes $\tan(\theta \pm \mu)$ averaged between points.
    *   **Wall Points:** The nozzle contour points $W_k$ are determined by the condition that waves reflecting off the wall must result in parallel exit flow. The first wall point is T. Subsequent points $W_k$ lie on the intersection of reflected $C_-$ characteristics and $C_+$ characteristics such that the flow angle $\theta$ at $W_k$ matches the wall slope required to turn the incident $C_-$ wave appropriately. For a minimum length nozzle, the wall points are chosen such that the final $C_-$ characteristic (originating from the reflection of the $\theta_{max}$ fan wave) becomes a straight line corresponding to the exit Mach wave angle $\mu_e = \arcsin(1/M_e)$. The flow along this final characteristic has $M=M_e$ and $\theta=0$.
    *   **Hand Calculation Feasibility:** Calculating the coordinates of numerous points by hand is extremely tedious and prone to error. This step is typically performed numerically.

6.  **Plotting:**
    *   Plot the calculated wall points $(x_W, y_W)$ to show the nozzle contour.
    *   Plot the network of $C_+$ and $C_-$ characteristics connecting the calculated intersection points.
    *   The plot should show the throat at $x=0$, the centerline $y=0$, the initial expansion fan, the reflected waves, the nozzle contour, and the final parallel flow region at the exit $x=L$.

**Summary of Hand-Calculable Results:**
*   Exit Mach Number: $M_e = 2.0$
*   Exit P-M Angle: $\nu(M_e) = 26.38^\circ$
*   Maximum Wall Angle (at throat): $\theta_{max} = 13.19^\circ$
*   Throat Half-Height: $y_t = 0.5 \, cm$
*   Exit Half-Height: $y_e = 0.84375 \, cm$
*   Number of Characteristics: User choice (e.g., $N=5$ lines in the fan).
*   The detailed coordinates and plot require numerical computation using the MOC algorithm.

**Equations Used:**
*   Prandtl-Meyer Function $\nu(M)$
*   Mach Angle $\mu(M)$
*   Characteristic Compatibility Relations: $K_+ = \theta - \nu$, $K_- = \theta + \nu$
*   Characteristic Slopes: $dy/dx = \tan(\theta \pm \mu)$
*   Isentropic Area Ratio $A/A^*(M)$
*   Geometric Relations for 2D Planar Flow: $A/A^* = y/y_t$
