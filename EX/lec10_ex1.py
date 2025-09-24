import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Initial conditions
m = 0.1       
g = 9.8       
c = 0.1       
v0 = 40.0     

theta = (45.0/180.0)*np.pi
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)

def traj_no_drag(t,state):
    x, y, vx, vy = state
    dxdt = vx
    dydt = vy
    dvxdt = 0
    dvydt = -g
    return [dxdt, dydt, dvxdt, dvydt]

def traj_with_drag(t,state):
    x, y, vx, vy = state
    dxdt = vx
    dydt = vy
    dvxdt = -(c/m) * vx 
    dvydt = -g - (c/m) * vy
    return [dxdt, dydt, dvxdt, dvydt]

state0 = [0, 0, vx0, vy0]
t_span =(0, 10)
t_eval = np.linspace(0, 10, 200)

# Solve ODEs
sol_no_drag = solve_ivp(traj_no_drag, t_span, state0, t_eval=t_eval)
sol_with_drag = solve_ivp(traj_with_drag, t_span, state0, t_eval=t_eval)

x_no_drag, y_no_drag = sol_no_drag.y[0], sol_no_drag.y[1]
x_drag, y_drag       = sol_with_drag.y[0], sol_with_drag.y[1]

# Mask for y>=0
mask_no_drag   = y_no_drag >= 0
mask_with_drag = y_drag >= 0

plt.figure(figsize=(8,6))
plt.plot(x_no_drag[mask_no_drag], y_no_drag[mask_no_drag], label="No Air Resistance")
plt.plot(x_drag[mask_with_drag], y_drag[mask_with_drag], label="With Air Resistance")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Projectile Motion with and without Air Resistance")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,6))
plt.plot(x_no_drag, y_no_drag, label="No Air Resistance")
plt.plot(x_drag, y_drag, label="With Air Resistance")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Projectile Motion with and without Air Resistance")
plt.legend()
plt.grid(True)
plt.show()
