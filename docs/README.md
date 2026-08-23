# Documentación TSP 1.0

La jerarquía científica del lanzamiento es:

1. **Documento Base — Principios Fundamentales:** define qué propone la TSP.
2. **Parte II — Formulación y Demostración Matemática:** formaliza y comprueba propiedades del modelo mínimo.
3. **Resumen Ejecutivo:** documento breve de entrada al paquete científico.
4. **Este repositorio:** reproduce cálculos y figuras de la Parte II.
5. **Zenodo:** depósito permanente y DOI de la versión archivada.
6. **jesuspaz.science:** presentación pública oficial.

## Alcance

El repositorio no amplía TSP 1.0. Reproduce la formulación matemática cerrada el 23 de agosto de 2026. Las aplicaciones físicas concretas, extensiones espaciales y futuras contrastaciones deben mantenerse separadas del núcleo TSP 1.0.

## Resultados de referencia

```text
Caso canónico: chi=2.5, kappa=1, delta=1
Puntos fijos: 0, 0.5, 2.0
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

Estos valores son los que debe reproducir `src/verify_results.py`.
