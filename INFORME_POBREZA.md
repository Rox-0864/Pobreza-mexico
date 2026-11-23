# Informe — Pobreza en México: ¿el descenso es un dato real?

> Análisis crítico de la evolución de la pobreza multidimensional (2008–2024) y
> de hasta qué punto el descenso reportado es un cambio real o un artefacto de
> medición.

---

## 1. La serie oficial

Pobreza multidimensional (% de la población):

| Año | Pobreza | Extrema | Emisor |
|---|---|---|---|
| 2008 | 44.4 | 11.0 | CONEVAL |
| 2010 | 46.1 | 11.3 | CONEVAL |
| 2012 | 45.5 | 9.8 | CONEVAL |
| 2014 | 46.2 | 9.5 | CONEVAL |
| 2016 | 43.2 | 7.2 | CONEVAL |
| 2018 | 41.9 | 7.0 | CONEVAL |
| 2020 | 43.9 | 8.5 | CONEVAL |
| 2022 | 36.3 | 7.1 | CONEVAL |
| **2024** | **29.6** | **5.3** | **INEGI** |

> La serie 2008–2014 usa la metodología de 2010; la de 2016–2024 la de 2018.
> No son estrictamente comparables entre sí.

---

## 2. El hallazgo central: cambió el emisor (CONEVAL → INEGI)

El descenso más celebrado (36.3% en 2022 → 29.6% en 2024) cruza un **cambio
institucional profundo**:

1. **Reforma constitucional** publicada el 20 de diciembre de 2024.
2. Leyes secundarias en vigor el **17 de julio de 2025**.
3. **Extinción del CONEVAL** (que midió la pobreza de 2008 a 2022) y
   **transferencia de la función al INEGI**, que midió 2024 por primera vez.

El INEGI afirma seguir los mismos lineamientos del CONEVAL, pero expertos
(EQUIDE-IBERO, IMCO, academia) señalaron **ajustes técnicos** que rompen la
comparabilidad:

- Cambios en la **ENIGH 2024** (la encuesta fuente).
- Cambios en cómo se miden indicadores específicos (acceso al **agua** y a la
  **salud**), no justificados explícitamente.
- La reforma de enero de 2026 da al INEGI **discreción para definir los
  criterios**, sin obligarlo a usar los indicadores previos.

---

## 3. La segunda señal: el descenso es por ingreso, no por derechos

La pobreza bajó, pero los **"vulnerables por carencias sociales" subieron**
(29.4% → 32.2% en 2022–2024). Es decir, la gente no dejó de tener carencias
(educación, salud, seguridad social); dejó de ser "pobre" porque su **ingreso**
subió por encima de la línea, empujado por:

- **Transferencias monetarias** (pensiones y programas sociales), +14.3% real 2022–2024.
- **Remesas** récord (~60 mil M USD/año).
- **Salario mínimo** (incremento real acumulado muy grande desde 2018).

Esto es un cambio **real** de ingreso, pero **no** una mejora estructural de los
derechos sociales. Y al cambiar el emisor y la encuesta en el mismo ejercicio, la
magnitud exacta del descenso es incierta.

---

## 4. Veredicto

El descenso de la pobreza es **parcialmente real y parcialmente artefacto**:

- **Real**: el ingreso de los hogares de menores recursos subió de forma
  verificable (transferencias + remesas + salario mínimo) y hubo un rebote
  post-COVID. La caída 2020→2022 es sólida.
- **Artefacto**: el dato de 2024 (29.6%) proviene de **otra institución** (INEGI)
  con una **encuesta modificada**, y mide una mejora que es **casi exclusivamente
  de ingreso**, mientras las carencias sociales se mantienen o se reclasifican
  (vulnerables por carencias al alza).

En otras palabras: es el mismo patrón que la pesca (CONAPESCA→estados, 2018) y que
el maguey pulquero (cambio de unidad): **un quiebre de dato que parece un cambio
de la realidad**.

---

## 5. Reproducir

```bash
python scripts/analisis.py      # datos + gráficos
streamlit run app.py            # dashboard
```

Datos en `data/`; gráficos en `results/`. Fuentes: comunicados CONEVAL e INEGI
(2008–2024), EQUIDE-IBERO, IMCO.
