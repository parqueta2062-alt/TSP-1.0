# TSP 1.0 — Theory of Structural Prevalence

Reproducible technical repository for **TSP 1.0**, associated with the first mathematical formulation of the Theory of Structural Prevalence.

**Author:** Jesus Paz  
**Formal presentation:** 28 August 2026

## Scope

This repository reproduces the mathematical and numerical results of Part II of TSP 1.0. It does not by itself constitute validation of physical universality. Mapping the model to concrete physical systems, estimating parameters from data, and independent empirical testing are subsequent stages.

## Canonical model

The minimal dynamical family is

```text
du/dτ = u - χ̂ u² + κ̂ u^(2+δ)
```

with `χ̂ > 0`, `κ̂ > 0`, and `δ > 0` for the general bifurcation analysis developed in TSP 1.0.

Canonical case:

```text
δ = 1
χ̂ = 2.5
κ̂ = 1

du/dτ = u - 2.5u² + u³ = u(u - 0.5)(u - 2)
```

Fixed points: `u*=0`, `u*=0.5`, and `u*=2.0`.

- `u0 < 2` → convergence toward `u*=0.5`.
- `u0 = 2` → unstable separatrix.
- `u0 > 2` → prevalence regime and mathematical finite-time divergence.

Exact critical times used in Figure 1:

```text
τc(2.2) ≈ 0.455526
τc(3.0) ≈ 0.123109
```

## Prevalence Control Invariant

```text
Θ = [δ^δ/(1+δ)^(1+δ)] · [χ̂^(1+δ)/κ̂]
```

Classification:

- `Θ > 1` → positive attractor + separatrix.
- `Θ = 1` → saddle-node bifurcation.
- `Θ < 1` → no positive fixed points; global prevalence within the minimal model.

For `χ̂=2.5`, `δ=1`:

```text
κ̂c = 1.5625
```

## Minimal structural-memory extension

```text
dm/dτ = u - λm
κ̂eff = κ̂(1 + αm)
du/dτ = u - χ̂u² + κ̂(1+αm)u^(2+δ)
```

The effective invariant is

```text
Θeff = Θ0/(1+αm)
mc = (Θ0-1)/α
```

For the canonical case with `α=1`, `Θ0=1.5625`:

```text
mc = 0.5625
```

Figure 3 compares `u0=1` with `m0=0` and `m0=0.7`, using `λ=2`.

The variable `m` explicitly carries history-dependent information. In the enlarged state space `(u,m)`, the coupled dynamics can be represented as Markovian; the extension therefore models structural memory without claiming that it proves fundamental non-Markovianity.

## Reproduction

Requires Python 3.10+.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
python src/verify_results.py
python src/figure_1_trajectories.py
python src/figure_2_bifurcation.py
python src/figure_3_structural_memory.py
```

Figures are saved in `figures/`.

## Repository structure

```text
TSP-1.0/
├── README.md
├── CITATION.cff
├── requirements.txt
├── src/
│   ├── verify_results.py
│   ├── figure_1_trajectories.py
│   ├── figure_2_bifurcation.py
│   └── figure_3_structural_memory.py
├── figures/
│   └── README.md
└── docs/
    └── README.md
```

## Scientific status

TSP 1.0 is a **formalized phenomenological proposal pending physical validation**. This repository makes its mathematical core reproducible: attractors and separatrices, the topological transition classified by `Θ`, the asymptotic scaling law in the dominant regime, and a minimal active-memory extension.

It does not yet demonstrate that these mechanisms are universal in nature, nor does it uniquely identify the model parameters with physical observables across different systems.

The asymptotic prediction of the minimal prevalence regime is

```text
tc ∝ S0^(-(1+δ))
```

A meaningful physical test requires `S`, `ω`, `χ`, `κ`, and `δ` to be operationally defined for a concrete system, with `δ` constrained independently rather than freely selected after fitting.

## Language policy

**English is the primary scientific and archival language of the TSP 1.0 GitHub/Zenodo release.** Spanish material may be maintained separately as complementary dissemination material.

## Versioning and archival

This repository is connected to Zenodo. The first archival DOI for TSP 1.0 will be generated only from an approved GitHub release after the repository contents and metadata have passed final review.

## Previous TSP record

An earlier English-language TSP preprint was deposited in Zenodo in May 2026. TSP 1.0 is being prepared as a distinct revised formulation, with a clearer separation between conceptual principles, mathematical formalization, reproducibility, and subsequent empirical validation.

## Official documentation

The definitive Zenodo DOI and official TSP 1.0 presentation page at `jesuspaz.science` will be added when the release is frozen.
