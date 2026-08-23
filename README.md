# TSP 1.0 — Teoría de la Prevalencia Estructural

Repositorio técnico reproducible de **TSP 1.0**, asociado a la primera formulación matemática de la Teoría de la Prevalencia Estructural.

**Autor:** Jesus Paz  
**Presentación formal prevista:** 28 de agosto de 2026

## Alcance

Este repositorio reproduce los resultados matemáticos y numéricos de la Parte II de TSP 1.0. No constituye por sí solo una validación de universalidad física. La correspondencia con sistemas físicos concretos, la estimación de parámetros a partir de datos y la contrastación independiente son etapas posteriores.

## Modelo canónico

La familia dinámica mínima es

```text
du/dτ = u - χ̂ u² + κ̂ u^(2+δ)
```

con `χ̂ > 0`, `κ̂ > 0` y `δ > 0` para el análisis general de bifurcación desarrollado en TSP 1.0.

Caso canónico:

```text
δ = 1
χ̂ = 2.5
κ̂ = 1

du/dτ = u - 2.5u² + u³ = u(u - 0.5)(u - 2)
```

Puntos fijos: `u*=0`, `u*=0.5` y `u*=2.0`.

- `u0 < 2` → convergencia hacia `u*=0.5`.
- `u0 = 2` → separatriz inestable.
- `u0 > 2` → régimen de prevalencia y divergencia matemática en tiempo finito.

Tiempos críticos exactos usados en la Figura 1:

```text
τc(2.2) ≈ 0.455526
τc(3.0) ≈ 0.123109
```

## Invariante de Control de Prevalencia

```text
Θ = [δ^δ/(1+δ)^(1+δ)] · [χ̂^(1+δ)/κ̂]
```

Clasificación:

- `Θ > 1` → atractor positivo + separatriz.
- `Θ = 1` → bifurcación silla-nodo.
- `Θ < 1` → sin puntos fijos positivos; prevalencia global dentro del modelo.

Para `χ̂=2.5`, `δ=1`:

```text
κ̂c = 1.5625
```

## Memoria estructural mínima

```text
dm/dτ = u - λm
κ̂eff = κ̂(1 + αm)
du/dτ = u - χ̂u² + κ̂(1+αm)u^(2+δ)
```

El invariante efectivo es

```text
Θeff = Θ0/(1+αm)
mc = (Θ0-1)/α
```

Para el caso canónico con `α=1`, `Θ0=1.5625`:

```text
mc = 0.5625
```

La Figura 3 compara `u0=1` con `m0=0` y `m0=0.7`, usando `λ=2`.

## Reproducción

Requiere Python 3.10+.

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

Las figuras se guardan en `figures/`.

## Estructura

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

## Estado científico

TSP 1.0 es una **propuesta fenomenológica formalizada pendiente de validación física**. Este repositorio permite reproducir el núcleo matemático presentado: atractores y separatrices, transición topológica mediante `Θ`, ley asintótica del régimen dominante y extensión mínima de memoria activa.

No demuestra todavía que estos mecanismos sean universales en la naturaleza ni identifica de forma única los parámetros del modelo con magnitudes físicas de todos los sistemas.

## Registro y documentación

Los enlaces definitivos al depósito Zenodo/DOI y a la página oficial en `jesuspaz.science` se incorporarán al congelar la versión pública TSP 1.0.
