import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

V0 = 5.0   
R = 10.0   
L = 2.0    
I0 = 0.0   
alpha = R/L

def dIdt(t, I):
    return (V0 - R*I) / L

t_span = (0, 2)
t_eval = np.linspace(t_span[0], t_span[1], 200)
sol = solve_ivp(dIdt, t_span, [I0], t_eval=t_eval)

plt.figure(figsize=(7,5))
plt.plot(sol.t, sol.y[0], 'b', label='SciPy solve_ivp')
plt.axhline(V0/R, color='gray', linestyle='--', alpha=0.7, label='Steady state')
plt.xlabel('Time t [s]')
plt.ylabel('Current I(t) [A]')
plt.title('RL Circuit Step Response')
plt.legend()
plt.grid(True)
plt.show()
