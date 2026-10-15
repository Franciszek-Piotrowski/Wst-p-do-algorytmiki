import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
plt.style.use('ggplot')


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


def analyze_horizon(dt, t_max, state0):
    t_e, state_e = euler_method(lorenz, state0, t_max, dt)
    state_exact = odeint(lorenz, state0, t_e)

    e_t = np.linalg.norm(state_e - state_exact, axis=1)

    exact_norm = np.linalg.norm(state_exact, axis=1)
    threshold = 0.02 * exact_norm

    exceed_indices = np.where(e_t > threshold)[0]

    if len(exceed_indices) > 0:
        horizon = t_e[exceed_indices[0]]
    else:
        horizon = t_max

    return t_e, e_t, threshold, horizon


t_max = 25.0
xyz0 = [1.0, 1.0, 1.0]
dt_list = [0.005, 0.01, 0.02, 0.03]

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Wyznaczanie horyzontu obserwacji dla układu Lorenza (błąd > 2%)', fontsize=16)
axes = axes.flatten()

for i, dt in enumerate(dt_list):
    t_e, e_t, threshold, horizon = analyze_horizon(dt, t_max, xyz0)

    axes[i].plot(t_e, e_t, 'r-', linewidth=1.5, label='Błąd e(t)')
    axes[i].plot(t_e, threshold, 'b--', linewidth=1.5, label='Próg 2%')

    if horizon < t_max:
        axes[i].axvline(x=horizon, color='k', linestyle=':', linewidth=2, label=f'Horyzont = {horizon:.2f} s')
    else:
        axes[i].axvline(x=t_max, color='g', linestyle=':', linewidth=2, label='Brak przekroczenia')

    axes[i].set_title(f'Krok dt = {dt}')
    axes[i].set_xlabel('Czas [s]')
    axes[i].set_ylabel('Błąd')

    max_y = max(threshold) * 5 if horizon < t_max else max(threshold) * 2
    axes[i].set_ylim(0, max_y)
    axes[i].legend()

plt.tight_layout()
plt.savefig('horyzont_4_wykresy.png', dpi=150)
