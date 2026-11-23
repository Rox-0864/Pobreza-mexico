import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Pobreza en México — ¿dato real?", page_icon="📊", layout="wide")

@st.cache_data
def cargar():
    nueva = pd.read_csv("data/pobreza_nueva_2016_2024.csv")
    vieja = pd.read_csv("data/pobreza_vieja_2008_2014.csv")
    return nueva, vieja

nueva, vieja = cargar()

st.title("📊 Pobreza en México — ¿el descenso es un dato real?")
st.caption("Pobreza multidimensional 2008–2024 · CONEVAL → INEGI")

st.markdown("""
**La pregunta de fondo:** los reportes recientes dicen que la pobreza bajó de 36.3% (2022)
a **29.6% (2024)**. ¿Hasta qué punto es un descenso real y hasta qué punto un cambio de
medición? La respuesta corta: **es ambas cosas**, y el dato de 2024 viene de **otra
institución** (INEGI, no CONEVAL).
""")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Pobreza 2022 (CONEVAL)", "36.3%")
c2.metric("Pobreza 2024 (INEGI)", "29.6%", delta="−6.7 pts")
c3.metric("Vulnerables por carencias", "32.2%", delta="+2.8 pts", delta_color="inverse")
c4.metric("Quién mide desde 2024", "INEGI")

st.markdown("---")

# 1. Tendencia
st.header("1 · La tendencia (con los quiebres marcados)")
fig = go.Figure()
fig.add_trace(go.Scatter(x=vieja["Anio"], y=vieja["pobreza"], mode="lines+markers",
                         name="Serie vieja (met. 2010)", line=dict(color="#7f7f7f", width=2, dash="dash")))
fig.add_trace(go.Scatter(x=nueva["Anio"], y=nueva["pobreza"], mode="lines+markers",
                         name="Serie nueva (met. 2018)", line=dict(color="#1f77b4", width=3)))
fig.add_vline(x=2023, line_dash="dot", line_color="#d62728",
              annotation_text="2024 = INEGI (1.ª vez)", annotation_position="top left")
fig.add_annotation(x=2020, y=43.9, text="COVID", showarrow=True, arrowhead=2,
                   ax=0, ay=-25)
fig.update_layout(height=420, margin=dict(l=0, r=0, t=10, b=0),
                  yaxis_title="% de la población", yaxis=dict(range=[25, 49]))
st.plotly_chart(fig, use_container_width=True)
st.info("Dos series, dos metodologías y un cambio de institución: 2008-2014 (met. 2010), "
        "2016-2024 (met. 2018) y **2024 medido por INEGI** tras la extinción del CONEVAL "
        "(reforma constitucional dic-2024).")

st.markdown("---")

# 2. Composición
st.header("2 · El descenso es por ingreso, no por derechos")
comp = nueva[["pobreza_moderada", "pobreza_extrema", "vul_carencias", "vul_ingresos", "no_pobre"]].copy()
comp.index = nueva["Anio"]
colores = {"pobreza_moderada": "#d62728", "pobreza_extrema": "#a30000",
           "vul_carencias": "#ff7f0e", "vul_ingresos": "#2ca02c", "no_pobre": "#1f77b4"}
fig2 = go.Figure()
for col in ["pobreza_extrema", "pobreza_moderada", "vul_carencias", "vul_ingresos", "no_pobre"]:
    fig2.add_trace(go.Bar(x=comp.index, y=comp[col], name=col, marker_color=colores[col]))
fig2.update_layout(height=420, margin=dict(l=0, r=0, t=10, b=0),
                   barmode="stack", yaxis_title="% de la población")
st.plotly_chart(fig2, use_container_width=True)
st.warning("**La señal rara:** la pobreza baja, pero los **vulnerables por carencias sociales suben** "
           "(29.4% → 32.2%). La gente sale de 'pobre' sobre todo por **ingreso** (transferencias, "
           "pensiones, remesas, salario mínimo), no porque mejoraron sus derechos sociales (salud, "
           "seguridad social, educación).")

st.markdown("---")

# 3. Veredicto
st.header("3 · Veredicto")
st.markdown("""
| Componente | ¿Real o artefacto? |
|---|---|
| Caída 2020 → 2022 (43.9% → 36.3%) | **Mayormente real**: rebote post-COVID + transferencias + remesas + salario mínimo |
| Caída 2022 → 2024 (36.3% → 29.6%) | **Mixta**: real en ingreso, pero **medida por otra institución (INEGI)** con encuesta modificada |
| Mejora en carencias sociales | **Débil**: los vulnerables por carencias *subieron*; la mejora es de ingreso, no de derechos |
| Comparabilidad 2024 vs 2022 | **Cuestionada**: cambio de emisor + cambios en ENIGH + ajustes en indicadores (agua, salud) |
""")
st.caption("Fuentes: comunicados CONEVAL e INEGI (2008-2024), EQUIDE-IBERO, IMCO. "
           "Reproducible: `scripts/analisis.py` · datos en `data/`.")
