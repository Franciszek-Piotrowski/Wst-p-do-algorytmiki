import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp
import os

# Ścieżka do folderu projektowego
current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'

# --- PARAMETRY UKŁADU ---
g = 9.81
L = 1.0
omega = np.sqrt(g / L)

# Warunki początkowe
X0_VAL = 0.15
V0_VAL = 0.0

t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# --- 1. ROZWIĄZANIE DOKŁADNE (Analityczne wyznaczenie jawne) ---
t_sym = sp.symbols('t', real=True)
C1, C2 = sp.symbols('C1 C2')

# Jawna postać rozwiązania ogólnego dla równania harmonicznego
x_general = C1 * sp.cos(omega * t_sym) + C2 * sp.sin(omega * t_sym)
v_general = x_general.diff(t_sym)

# Układ równań dla warunków początkowych t = 0
eq1 = sp.Eq(x_general.subs(t_sym, 0), X0_VAL)
eq2 = sp.Eq(v_general.subs(t_sym, 0), V0_VAL)

# Wyznaczenie stałych całkowania
constants = sp.solve([eq1, eq2], (C1, C2))

# Podstawienie stałych do rozwiązania ogólnego
x_exact_expr = x_general.subs(constants)

# Konwersja na funkcję NumPy
x_exact_func = sp.lambdify(t_sym, x_exact_expr, 'numpy')
x_exact = x_exact_func(t_eval)

# --- 2. ROZWIĄZANIE NUMERYCZNE (SciPy) ---
def pendulum_ode(t_val, y):
    return [y[1], -(g / L) * y[0]]

sol_num = solve_ivp(pendulum_ode, t_span, [X0_VAL, V0_VAL], t_eval=t_eval, method='RK45', rtol=1e-8)
x_num = sol_num.y[0]

# --- 3. METRYKI BŁĘDU ---
error = x_exact - x_num
mae = np.mean(np.abs(error))
mse = np.mean(error**2)

print(f"--- WYNIKI ANALIZY BŁĘDÓW ---")
print(f"Mean Absolute Error (MAE): {mae:.2e}")
print(f"Mean Squared Error (MSE): {mse:.2e}")

# --- 4. WIZUALIZACJA I ZAPIS BEZ WYŚWIETLANIA OKIEN ---
plt.style.use('ggplot')

# Wykres 1: Porównanie rozwiązań
fig1, ax1 = plt.subplots(figsize=(8, 4), tight_layout=True)
ax1.plot(t_eval, x_exact, 'r-', label='Dokładne (SymPy)', linewidth=2)
ax1.plot(t_eval, x_num, 'b--', label='Przybliżone (SciPy)', linewidth=1.5)
ax1.set_xlabel('Czas t [s]')
ax1.set_ylabel('Kąt odchylenia x(t) [rad]')
ax1.set_title('Porównanie rozwiązania dokładnego i przybliżonego')
ax1.legend()
ax1.grid(True)

plt.savefig(os.path.join(current_dir, 'wykres_porownanie.png'), dpi=300)
plt.close(fig1)

# Wykres 2: Błąd w każdym kroku
fig2, ax2 = plt.subplots(figsize=(8, 3), tight_layout=True)
ax2.plot(t_eval, error, 'g-', label='Błąd chwilowy')
ax2.set_xlabel('Czas t [s]')
ax2.set_ylabel('Błąd [rad]')
ax2.set_title('Wykres błędu w kolejnych krokach czasu')
ax2.legend()
ax2.grid(True)

plt.savefig(os.path.join(current_dir, 'wykres_bledu.png'), dpi=300)
plt.close(fig2)

print(f"\n[SUKCES] Wykresy zapisane w folderze jako .png")