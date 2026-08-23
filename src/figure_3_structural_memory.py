"""Figure 3 — minimal active structural-memory extension of TSP 1.0."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

OUT = Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(exist_ok=True)
CHI = 2.5
KAPPA = 1.0
DELTA = 1.0
ALPHA = 1.0
LAMBDA = 2.0


def rhs(t, y):
    u, m = y
    du = u - CHI*u**2 + KAPPA*(1 + ALPHA*m)*u**(2+DELTA)
    dm = u - LAMBDA*m
    return [du, dm]


def stop_at_u20(t, y):
    return 20-y[0]
stop_at_u20.terminal = True
stop_at_u20.direction = -1

fig, ax = plt.subplots(figsize=(9, 6))
for m0 in [0.0, 0.7]:
    sol = solve_ivp(rhs, (0, 10), [1.0, m0], rtol=1e-10, atol=1e-12, max_step=0.002, events=stop_at_u20, dense_output=True)
    t_end = sol.t[-1]
    t = np.linspace(0, t_end, 1000)
    u = sol.sol(t)[0]
    ax.plot(t, u, label=f"u0=1, m0={m0:g}")

ax.axhline(0.5, linestyle="--", linewidth=1, label="canonical attractor u*=0.5")
ax.set_xlabel("Dimensionless time tau")
ax.set_ylabel("Dimensionless state u(tau)")
ax.set_title("TSP 1.0 — Figure 3: structural memory changes future trajectory")
ax.set_ylim(0, 5)
ax.legend()
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(OUT / "figure_3_structural_memory.png", dpi=300)
fig.savefig(OUT / "figure_3_structural_memory.pdf")

# Instantaneous check at the shared observable state u=1.
def du_at(u, m):
    return u - CHI*u**2 + KAPPA*(1+ALPHA*m)*u**3

print("Figure 3 generated.")
print(f"du/dtau(u=1,m=0)={du_at(1,0):.6f}")
print(f"du/dtau(u=1,m=0.7)={du_at(1,0.7):.6f}")
