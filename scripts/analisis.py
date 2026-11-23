import pandas as pd, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Serie nueva (2016-2024) — oficial, comparable, metodología 2018
nueva = pd.DataFrame({
    'Anio': [2016, 2018, 2020, 2022, 2024],
    'pobreza': [43.2, 41.9, 43.9, 36.3, 29.6],
    'pobreza_extrema': [7.2, 7.0, 8.5, 7.1, 5.3],
    'pobreza_moderada': [36.0, 34.9, 35.4, 29.3, 24.2],
    'vul_carencias': [25.3, 26.4, 23.7, 29.4, 32.2],
    'vul_ingresos': [7.6, 8.0, 8.9, 7.2, 5.8],
    'no_pobre': [24.0, 23.7, 23.5, 27.1, 32.5],
    'emisor': ['CONEVAL','CONEVAL','CONEVAL','CONEVAL','INEGI'],
})
nueva['pob_millones'] = [52.2, 51.9, 55.7, 46.8, 38.5]

# Serie vieja (2008-2014) — metodología 2010, NO comparable con la nueva
vieja = pd.DataFrame({
    'Anio': [2008, 2010, 2012, 2014],
    'pobreza': [44.4, 46.1, 45.5, 46.2],
    'pobreza_extrema': [11.0, 11.3, 9.8, 9.5],
})

nueva.to_csv('data/pobreza_nueva_2016_2024.csv', index=False, encoding='utf-8')
vieja.to_csv('data/pobreza_vieja_2008_2014.csv', index=False, encoding='utf-8')

# ---- gráfico 1: tendencia con quiebres marcados ----
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.plot(vieja['Anio'], vieja['pobreza'], color='#7f7f7f', lw=2, marker='o', ls='--', label='Serie vieja (met. 2010)')
ax.plot(nueva['Anio'], nueva['pobreza'], color='#1f77b4', lw=2.5, marker='o', label='Serie nueva (met. 2018)')
# marcar quiebres
ax.axvspan(2014.5, 2016.5, color='gray', alpha=0.15)
ax.text(2015.5, 47.5, 'cambio\nmetodología\n2016 ENIGH', ha='center', fontsize=7, color='gray')
ax.axvline(2023, color='#d62728', ls=':', lw=1.5)
ax.text(2023.1, 30, '2024 = INEGI\n(1.ª vez)', fontsize=8, color='#d62728')
ax.annotate('COVID', xy=(2020, 43.9), xytext=(2019, 47), fontsize=8,
            arrowprops=dict(arrowstyle='->', color='gray'))
ax.set_ylabel('% de la población'); ax.set_title('Pobreza multidimensional en México, 2008-2024')
ax.set_ylim(25, 49); ax.grid(alpha=0.3); ax.legend(fontsize=8)
plt.tight_layout(); plt.savefig('results/pobreza_tendencia.png', dpi=120); plt.close()

# ---- gráfico 2: composición (el "descenso" es sobre todo por ingresos) ----
fig, ax = plt.subplots(figsize=(10, 5.5))
comp = nueva[['pobreza_moderada','pobreza_extrema','vul_carencias','vul_ingresos','no_pobre']]
comp.index = nueva['Anio']
comp.plot(kind='bar', stacked=True, ax=ax, width=0.7,
          color=['#d62728','#a30000','#ff7f0e','#2ca02c','#1f77b4'])
ax.set_ylabel('% de la población'); ax.set_title('Composición de la población por situación (2016-2024)')
ax.legend(bbox_to_anchor=(1.05, 1), fontsize=8)
ax.axhline(100, color='gray', lw=0.5)
plt.tight_layout(); plt.savefig('results/pobreza_composicion.png', dpi=120); plt.close()

# ---- hallazgos numéricos ----
print('=== POBREZA MULTIDIMENSIONAL MÉXICO ===')
print(nueva.to_string(index=False))
print()
print('=== Cambios clave ===')
print(f"  2020->2022: pobreza {nueva.pobreza.iloc[2]}% -> {nueva.pobreza.iloc[3]}% (rebote post-COVID + transferencias)")
print(f"  2022->2024: pobreza {nueva.pobreza.iloc[3]}% -> {nueva.pobreza.iloc[4]}%  (PERO emisor cambia: CONEVAL -> INEGI)")
print(f"  Vulnerables por carencias: {nueva.vul_carencias.iloc[3]}% -> {nueva.vul_carencias.iloc[4]}%  (SUBE mientras pobreza BAJA)")
print(f"  No pobres: {nueva.no_pobre.iloc[3]}% -> {nueva.no_pobre.iloc[4]}%")
