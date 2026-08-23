"""Figure 2 — prevalence bifurcation for chi_hat=2.5, delta=1."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(exist_ok=True)
CHI = 2.5
DELTA = 1.0
KAPPA_C = CHI**2/4


def h(u, kappa):
    return 1 - CHI*u + kappa*u**(1+DELTA)


def theta(kappa):
    return CHI**2/(4*kappa)

u = np.linspace(0, 3, 1000)
fig, ax = plt.subplots(figsize=(9, 6))
for kappa in [1.0, KAPPA_C, 2.0]:
    ax.plot(u, h(u, kappa), label=f"kappa={kappa:.4f}; Theta={theta(kappa):.6f}")
ax.axhline(0, linewidth=1)
ax.scatter([0.5, 2.0, 0.8], [0, 0, 0], zorder=5)
ax.set_xlabel("Dimensionless state u")
ax.set_ylabel("h(u) = 1 - chi*u + kappa*u^(1+delta)")
ax.set_title("TSP 1.0 — Figure 2: prevalence bifurcation")
ax.legend()
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(OUT / "figure_2_bifurcation.png", dpi=300)
fig.savefig(OUT / "figure_2_bifurcation.pdf")
print(f"Figure 2 generated. kappa_c={KAPPA_C:.6f}")
