# TSP 1.0 — Executive Summary
## Theory of Structural Prevalence

**Entry document to the TSP 1.0 scientific package**  
**Author:** Jesus Paz · **Formal presentation scheduled:** 28 August 2026

## 1. Problem and proposal

The Theory of Structural Prevalence (TSP) is a phenomenological proposal investigating whether organized physical systems of different kinds can share the same dynamic logic: the accumulated history of a structure conditions its future trajectories, and certain configurations acquire a greater capacity for persistence and reinforcement.

TSP is not intended to replace Quantum Mechanics or General Relativity. It proposes a common framework of structural organization that must be tested through concrete physical realizations.

**ACCUMULATED HISTORY → STRUCTURAL MEMORY → PREFERRED TRAJECTORIES → PREVALENCE**

## 2. Minimal mathematical formulation

The first TSP 1.0 mathematical realization represents the competition among structural growth, environmental containment and self-reinforcement through

$$
\frac{du}{d\tau}=u-\hat\chi u^2+\hat\kappa u^{2+\delta},\qquad \hat\chi>0,\;\hat\kappa>0,\;\delta>0.
$$

Here $u$ is the normalized structural state, $\hat\chi$ represents effective containment or saturation, and $\hat\kappa$ the intensity of self-reinforcement. The equation formalizes a minimal mechanism; it is not yet identified with a universal physical system.

## 3. Canonical result: stabilization, threshold and prevalence

For $\delta=1$, $\hat\chi=2.5$ and $\hat\kappa=1$:

$$
\frac{du}{d\tau}=u-2.5u^2+u^3=u(u-0.5)(u-2).
$$

Three fixed points appear: $u_0^*=0$ (unstable), $u_1^*=0.5$ (stable attractor), and $u_2^*=2$ (unstable separatrix).

$$
u_0<2\Rightarrow u\to0.5\quad|\quad u_0=2\Rightarrow\text{THRESHOLD}\quad|\quad u_0>2\Rightarrow\text{PREVALENCE}.
$$

For $u_0>2$, the solution reaches mathematical finite-time divergence. This divergence marks the limit of validity of the effective continuous description; it does not by itself imply an infinite physical magnitude.

## 4. General prevalence criterion

The general analysis leads to the **Prevalence Control Invariant**:

$$
\Theta=\frac{\delta^\delta}{(1+\delta)^{1+\delta}}\frac{\hat\chi^{1+\delta}}{\hat\kappa}.
$$

| Condition | Dynamics |
|---|---|
| $\Theta>1$ | Containment: positive attractor + separatrix |
| $\Theta=1$ | Critical state: saddle-node bifurcation |
| $\Theta<1$ | Global prevalence: positive fixed points disappear |

Within the TSP dynamical family studied, this criterion establishes when the topology of the system itself changes.

## 5. Active structural memory

To represent accumulated history explicitly, a minimal memory variable is introduced:

$$
\frac{dm}{d\tau}=u-\lambda m,
$$

whose solution contains the previous trajectory of $u$. Memory becomes dynamically active through

$$
\hat\kappa_{eff}=\hat\kappa(1+\alpha m),
$$

$$
\frac{du}{d\tau}=u-\hat\chi u^2+\hat\kappa(1+\alpha m)u^{2+\delta}.
$$

The effective invariant becomes

$$
\Theta_{eff}=\frac{\Theta_0}{1+\alpha m},
$$

and, for $\Theta_0>1$, a memory threshold appears:

$$
m_c=\frac{\Theta_0-1}{\alpha}.
$$

In the canonical case, $\Theta_0=1.5625$ and $\alpha=1$ give $m_c=0.5625$. At the same current value $u=1$, $m=0$ produces $du/d\tau=-0.5$, whereas $m=0.7$ produces $du/d\tau=+0.2$.

**SAME OBSERVABLE $u$ + DIFFERENT INCORPORATED MEMORY ⇒ DIFFERENT EVOLUTION**

## 6. Quantitative prediction and falsifiability

In the asymptotic prevalence regime, where the superlinear term dominates,

$$
\frac{dS}{dt}\approx\omega\kappa S^{2+\delta},
$$

which gives

$$
t_c=\frac{1}{\omega\kappa(1+\delta)S_0^{1+\delta}}
\quad\Rightarrow\quad
t_c\propto S_0^{-(1+\delta)}.
$$

This is a prediction of this realization of the model under its asymptotic assumptions. To test it physically, $S$, $\omega$, $\kappa$ and $\delta$ must first be defined in a concrete system. If $\delta$ were freely adjusted after observing the data, the test would lose strength.

## 7. What is established and what remains open

| TSP 1.0 establishes within the model | TSP 1.0 does not yet demonstrate |
|---|---|
| Attractors, separatrices and prevalence regimes | Physical universality across scales |
| General $\Theta$ criterion and critical bifurcation | Unique correspondence of parameters with real physical quantities |
| Asymptotic critical-time law | Experimental validation of the law in a concrete domain |
| Minimal active structural-memory model | That every physical system possesses memory in an operational sense |

## 8. Scientific status of TSP 1.0

TSP 1.0 should be presented as a **formalized phenomenological proposal pending physical validation**. Part II provides an explicit, reproducible mathematical core susceptible to testing; the universality proposed by the Base Document remains a research hypothesis.

**CONCEPTUAL PROPOSAL + REPRODUCIBLE FORMALISM → PHYSICAL TESTING**

## 9. Official package and next stage

The TSP 1.0 package is organized into: (1) Base Document — Fundamental Principles; (2) Mathematical Formulation and Demonstration; and (3) Publication, Presentation and Dissemination. The launch coordinates the scientific deposit in Zenodo, the reproducible technical repository in GitHub, and the public presentation at jesuspaz.science.

The scientific stage after TSP 1.0 will be to select one concrete physical realization, operationally define its variables and parameters, formulate the prediction before testing, and compare it with experimental data or independent simulations.
