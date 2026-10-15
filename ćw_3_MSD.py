import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

matplotlib.style.use('ggplot')



matplotlib.style.use('ggplot')



def lotka_volterra(xy, t):
    x, y = xy
    a, b, c, d = 1.2, 0.6, 0.3, 0.8
    dx_dt = (a - b * y) * x
    dy_dt = (c * x - d) * y
    return np.array([dx_dt, dy_dt])


def lorenz(xyz, t):

    x, y, z = xyz
    sigma, beta, rho = 10.0, 8.0 / 3.0, 28.0
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return np.array([dx_dt, dy_dt, dz_dt])




def euler_method(f, state0, t_max, dt):
    n_steps = int(np.ceil(t_max / dt))
    t = np.linspace(0, t_max, n_steps + 1)
    state = np.zeros((n_steps + 1, len(state0)))
    state[0] = state0

    for i in range(n_steps):
        state[i + 1] = state[i] + dt * f(state[i], t[i])

    return t, state


def calculate_error(t_euler, state_euler, f, state0):

    state_exact = odeint(f, state0, t_euler)
    error = np.mean(np.abs(state_euler - state_exact))
    return error



print("--- LOTKA-VOLTERRA ---")
t_max_lv = 25
xy0 = [2.0, 1.0]
dt_values_lv = [0.3, 0.1, 0.01]

fig_lv_euler, axes_lv_euler = plt.subplots(3, 1, figsize=(12, 12))
fig_lv_euler.suptitle('Układ Lotki-Volterry zamodelowany przy pomocy metody Eulera', fontsize=16)

for i, dt in enumerate(dt_values_lv):
    t_e, state_e = euler_method(lotka_volterra, xy0, t_max_lv, dt)
    error = calculate_error(t_e, state_e, lotka_volterra, xy0)
    print(f"Błąd dla Eulera (dt={dt}): {error:.4f}")

    axes_lv_euler[i].plot(t_e, state_e[:, 0], color='tab:red', alpha=0.8, label='Ofiary')
    axes_lv_euler[i].plot(t_e, state_e[:, 1], color='tab:blue', alpha=0.8, label='Drapieżniki')
    axes_lv_euler[i].set_title(f'dt = {dt}')
    axes_lv_euler[i].set_xlim(0, t_max_lv)

plt.tight_layout()
plt.savefig('lotka_volterra_euler.png', dpi=150)

t_ode_lv = np.linspace(0, t_max_lv, 10000)
state_ode_lv = odeint(lotka_volterra, xy0, t_ode_lv)

plt.figure(figsize=(12, 6))
plt.plot(t_ode_lv, state_ode_lv[:, 0], color='tab:red', label='Ofiary')
plt.plot(t_ode_lv, state_ode_lv[:, 1], color='tab:blue', label='Drapieżniki')
plt.title('Układ Lotki-Volterry (odeint)')
plt.xlabel('Czas')
plt.ylabel('Populacja')
plt.legend()
plt.xlim(0, t_max_lv)
plt.tight_layout()
plt.savefig('lotka_volterra_odeint.png', dpi=150)


print("\n--- LORENZ ---")
t_max_lz = 25
xyz0 = [1.0, 1.0, 1.0]
dt_values_lz = [0.03, 0.02, 0.01]

fig_lz_euler, axes_lz_euler = plt.subplots(3, 3, figsize=(15, 12))
fig_lz_euler.suptitle('Układ Lorenza zamodelowany przy pomocy metody Eulera', fontsize=16)

for i, dt in enumerate(dt_values_lz):
    t_e, state_e = euler_method(lorenz, xyz0, t_max_lz, dt)
    error = calculate_error(t_e, state_e, lorenz, xyz0)
    print(f"Błąd dla Eulera (dt={dt}): {error:.4f}")

    x, y, z = state_e[:, 0], state_e[:, 1], state_e[:, 2]

    axes_lz_euler[i, 0].plot(x, y, color='tab:red', linewidth=0.8)
    axes_lz_euler[i, 0].set_title(f'y(x) dla dt={dt}')
    axes_lz_euler[i, 1].plot(x, z, color='tab:red', linewidth=0.8)
    axes_lz_euler[i, 1].set_title(f'z(x) dla dt={dt}')
    axes_lz_euler[i, 2].plot(y, z, color='tab:red', linewidth=0.8)
    axes_lz_euler[i, 2].set_title(f'z(y) dla dt={dt}')

plt.tight_layout()
plt.savefig('lorenz_euler_2d.png', dpi=150)

t_ode_lz = np.linspace(0, t_max_lz, 10000)
state_ode_lz = odeint(lorenz, xyz0, t_ode_lz)
x_ode, y_ode, z_ode = state_ode_lz[:, 0], state_ode_lz[:, 1], state_ode_lz[:, 2]

fig_lz_ode, axes_lz_ode = plt.subplots(1, 3, figsize=(15, 5))
axes_lz_ode[0].plot(x_ode, y_ode, color='tab:red', linewidth=0.8)
axes_lz_ode[0].set_title('y(x) - odeint')
axes_lz_ode[1].plot(x_ode, z_ode, color='tab:red', linewidth=0.8)
axes_lz_ode[1].set_title('z(x) - odeint')
axes_lz_ode[2].plot(y_ode, z_ode, color='tab:red', linewidth=0.8)
axes_lz_ode[2].set_title('z(y) - odeint')
plt.tight_layout()
plt.savefig('lorenz_odeint_2d.png', dpi=150)

t_e_best, state_e_best = euler_method(lorenz, xyz0, t_max_lz, 0.01)

fig_3d = plt.figure(figsize=(16, 7))

ax1 = fig_3d.add_subplot(1, 2, 1, projection='3d')
ax1.plot(state_e_best[:, 0], state_e_best[:, 1], state_e_best[:, 2], color='tab:blue', linewidth=0.5)
ax1.set_title('Lorenz 3D - Euler (dt=0.01)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

ax2 = fig_3d.add_subplot(1, 2, 2, projection='3d')
ax2.plot(x_ode, y_ode, z_ode, color='tab:red', linewidth=0.5)
ax2.set_title('Lorenz 3D - odeint')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.tight_layout()
plt.savefig('lorenz_3d_comparison.png', dpi=150)

