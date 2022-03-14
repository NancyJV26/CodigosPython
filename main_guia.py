#%%
import pandas as pd
import seaborn as sns

sldb = pd.read_csv('synergy_logistics_database.csv', index_col=0, parse_dates=[5])
# %%
sldb
# %%
"""
Analisis para las 10 rutas mas demandadas
"""
rutas = sldb.groupby(by=['direction', 'origin', 'destination', 'transport_mode'])
# %%
rutas.sum()
# rutas.groups
# %%
rutas['total_value'].describe().sort_values(by='count', ascending=False)
# %%
suma = rutas.sum()['total_value']
rutas = rutas['total_value'].describe()
rutas['suma_total'] = suma
rutas = rutas.reset_index()
# %%
rutas
# %%
exports = rutas[rutas['direction'] == 'Exports']
exports
# %%
"""
Analisis de exports, primero veamos las 10 rutas mas demandadas
"""
total_value_exports = exports.suma_total.sum()


def resultados(df, m):
    total_value = df.suma_total.sum()
    total_usos = df['count'].sum()
    porcentaje = (total_value / total_value_exports)*10000
    porcentaje = int(porcentaje) / 100
    print(f'Las 10 rutas {m} aportan {porcentaje}%, en un total de: {total_usos} servicios')

mas_demandadas = exports.sort_values(by='count', ascending=False).head(10)
mayor_valor = exports.sort_values(by='suma_total', ascending=False).head(10)

resultados(mas_demandadas, 'mas demandadas')
resultados(mayor_valor, 'con mayor valor')
# Prueba escogiendo el top 15 en su lugar.
# %%
