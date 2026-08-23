"""Independent numerical/algebraic checks for the published TSP 1.0 examples."""
import math
import numpy as np

CHI = 2.5
KAPPA = 1.0
DELTA = 1.0


def f(u, chi=CHI, kappa=KAPPA, delta=DELTA):
    return u - chi*u**2 + kappa*u**(2+delta)


def theta(chi, kappa, delta):
    return (delta**delta / (1+delta)**(1+delta)) * chi**(1+delta) / kappa


def tau_c(u0):
    if u0 <= 2:
        raise ValueError("tau_c formula here is for the canonical prevalence branch u0 > 2")
    F = math.log(u0) - (4/3)*math.log(u0-0.5) + (1/3)*math.log(u0-2)
    return -F


roots = np.roots([1.0, -2.5, 1.0, 0.0])
roots = np.sort(np.real_if_close(roots))
assert np.allclose(roots, [0.0, 0.5, 2.0], atol=1e-12)
assert math.isclose(theta(2.5, 1.0, 1.0), 1.5625, rel_tol=0, abs_tol=1e-12)
assert math.isclose(theta(2.5, 1.5625, 1.0), 1.0, rel_tol=0, abs_tol=1e-12)
assert math.isclose(theta(2.5, 2.0, 1.0), 0.78125, rel_tol=0, abs_tol=1e-12)
assert math.isclose(tau_c(2.2), 0.455526, abs_tol=1e-6)
assert math.isclose(tau_c(3.0), 0.123109, abs_tol=1e-6)

# Memory test at the same observable u=1.
def memory_du(u, m, alpha=1.0):
    return u - CHI*u**2 + KAPPA*(1+alpha*m)*u**3

assert math.isclose(memory_du(1.0, 0.0), -0.5, abs_tol=1e-12)
assert math.isclose(memory_du(1.0, 0.7), 0.2, abs_tol=1e-12)
mc = (theta(2.5, 1.0, 1.0)-1.0)/1.0
assert math.isclose(mc, 0.5625, abs_tol=1e-12)

print("TSP 1.0 verification: PASS")
print(f"fixed points: {roots.tolist()}")
print(f"Theta canonical: {theta(2.5,1.0,1.0):.6f}")
print(f"kappa_c: {2.5**2/4:.6f}")
print(f"tau_c(2.2): {tau_c(2.2):.6f}")
print(f"tau_c(3.0): {tau_c(3.0):.6f}")
print(f"m_c: {mc:.6f}")
print(f"du/dtau at u=1,m=0: {memory_du(1,0):.6f}")
print(f"du/dtau at u=1,m=0.7: {memory_du(1,0.7):.6f}")
