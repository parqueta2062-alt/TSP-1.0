"""Figure 1 — canonical TSP 1.0 trajectories."""
from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

OUT = Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(exist_ok=True)


def rhs(t, y):
    u = y[0]
    return [u - 2.5*u*u + u**3]


def exact_tau_c(u0):
    F = math.log(u0) - (4/3)*math.log(u0-0.5) + (1/3)*math.log(u0-2)
    return -F


fig, ax = plt.subplots(figsize=(9, 6))
for u0 in [0.2, 0.8, 1.8, 2.0, 2.2, 3.0]:
    if u0 == 2.0:
        t = np.linspace(0, 3, 400)
        u = np.full_like(t, 2.0)
    elif u0 > 2.0:
        tc = exact_tau_c(u0)
        # Stop just before the mathematical divergence.
        t_end = tc * 0.995
        sol = solve_ivp(rhs, (0, t_end), [u0], dense_output=True, rtol=1e-10, atol=1e-12, max_step=tc/1000)
        t = np.linspace(0, t_end, 600)
        u = sol.sol(t)[0]
    else:
        t = np.linspace(0, 3, 600)
        sol = solve_ivp(rhs, (0, 3), [u0], t_eval=t, rtol=1e-10, atol=1e-12, max_step=0.005)
        u = sol.y[0]
    label = f"u0={u0:g}"
    if u0 > 2:
        label += f"; tau_c={exact_tau_c(u0):.6f}"
    ax.plot(t, u, label=label)

ax.axhline(0.5, linestyle="--", linewidth=1, label="stable attractor u*=0.5")
ax.axhline(2.0, linestyle=":", linewidth=1, label="unstable separatrix u*=2")
ax.set_xlim(0, 3)
ax.set_ylim(0, 4)
ax.set_xlabel("Dimensionless time tau")
ax.set_ylabel("Dimensionless state u(tau)")
ax.set_title("TSP 1.0 — Figure 1: canonical dynamics")
ax.legend(fontsize=8)
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(OUT / "figure_1_trajectories.png", dpi=300)
fig.savefig(OUT / "figure_1_trajectories.pdf")
print("Figure 1 generated.")
print(f"tau_c(2.2)={exact_tau_c(2.2):.6f}; tau_c(3.0)={exact_tau_c(3.0):.6f}")
