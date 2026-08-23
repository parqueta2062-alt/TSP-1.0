# TSP 1.0 — Release Notes

**Release tag:** `v1.0.0`  
**Target formal release date:** 28 August 2026  
**Author:** Jesus Paz

## Scope

TSP 1.0 is the first frozen public package of the Theory of Structural Prevalence organized as a reproducible phenomenological formulation.

This release contains:

- the Base Document — Fundamental Principles;
- the Mathematical Formulation and Demonstration;
- the Executive Summary;
- the canonical nonlinear model and its fixed-point analysis;
- the Prevalence Control Invariant `Theta` and the saddle-node criterion;
- the asymptotic finite-time scaling law;
- the minimal active structural-memory extension;
- reproducible numerical verification code;
- reproducible scripts for Figures 1–3;
- final English-language figure previews and documentation;
- citation metadata for long-term archival.

## Scientific status

TSP 1.0 is a **formalized phenomenological proposal pending physical validation**. The release establishes the internal mathematical behavior of the stated model and its reproducible numerical examples. It does not claim that physical universality across scales has already been empirically demonstrated.

## Reference results

```text
Canonical parameters: chi_hat=2.5, kappa_hat=1, delta=1
Fixed points: 0, 0.5, 2.0
Theta0: 1.5625
kappa_c: 1.5625
tau_c(2.2): 0.4555262785
tau_c(3.0): 0.1231086872
alpha: 1
lambda: 2
m_c: 0.5625
du/dtau(u=1,m=0): -0.5
du/dtau(u=1,m=0.7): +0.2
```

## Reproducibility

Install dependencies from `requirements.txt`, then run:

```bash
python src/verify_results.py
python src/figure_1_trajectories.py
python src/figure_2_bifurcation.py
python src/figure_3_structural_memory.py
```

The verification script must report `PASS`, and the figure scripts regenerate the figure products from the versioned equations and parameters.

## Archival

The repository is connected to Zenodo. When the approved GitHub release `v1.0.0` is created, Zenodo is expected to preserve the release and assign the archival DOI for the software package.

## Previous TSP record

An earlier English-language TSP preprint was deposited in Zenodo in May 2026. TSP 1.0 is a distinct revised formulation with a clearer separation between conceptual principles, mathematical formalization, reproducibility, and future empirical validation.
