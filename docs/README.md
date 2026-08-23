# TSP 1.0 Documentation

The scientific hierarchy of the release is:

1. **Base Document — Fundamental Principles:** defines what TSP proposes.
2. **Part II — Mathematical Formulation and Demonstration:** formalizes and verifies properties of the minimal model.
3. **Executive Summary:** concise entry document to the scientific package.
4. **This repository:** reproduces calculations and figures from Part II.
5. **Zenodo:** permanent archive and DOI for the approved release.
6. **jesuspaz.science:** official public presentation.

## Scope

This repository does not expand TSP 1.0. It reproduces the mathematical formulation closed on 23 August 2026. Concrete physical applications, spatial extensions, and future empirical tests must remain separate from the TSP 1.0 mathematical core.

## Reference results

```text
Canonical case: chi=2.5, kappa=1, delta=1
Fixed points: 0, 0.5, 2.0
Theta0: 1.5625
kappa_c: 1.5625
tau_c(2.2): 0.455526
tau_c(3.0): 0.123109
alpha: 1
lambda: 2
m_c: 0.5625
du/dtau(u=1,m=0): -0.5
du/dtau(u=1,m=0.7): +0.2
```

These are the reference values that `src/verify_results.py` must reproduce.
