#%%
"""
Importamos pandas y sldb
"""
import pandas as pd
sldb = pd.read_csv('synergy_logistics_database.csv', index_col=0, parse_dates=[5])

# %%
"""
Analisis para las 10 rutas
"""
rutas = sldb.groupby(['direction','origin', 'destination', 'transport_mode'])
suma = rutas.sum()['total_value']
rutas = rutas['total_value'].describe()

rutas['suma_total'] = suma
rutas = rutas.reset_index()
# %%
"""
Analisis para exportaciones: Top 10 rutas por demanda y por ganancias
"""
exportaciones = rutas[ rutas['direction'] == 'Exports']
most_used = exportaciones.sort_values(by='count', ascending=False).head(10)

valor_total_exportaciones = exportaciones['suma_total'].sum()
valor_total_top = most_used.suma_total.sum()
total_usos = most_used['count'].sum()
porcentaje = (valor_total_top / valor_total_exportaciones) * 10000
porcentaje = int(porcentaje) / 100

print(f'Las 10 rutas mas demandadas aportan {porcentaje}% de las ganancias, en un total de {total_usos} servicios')

# %%
"""
Analisis para exportaciones: Top 10 rutas por demanda y por ganancias
"""
exportaciones = rutas[ rutas['direction'] == 'Exports']
importaciones = rutas[rutas['direction'] == 'Imports']

def sol1(df, top=10):
    suma_total_df = df['suma_total'].sum()
    most_used = df.sort_values(by='suma_total', ascending=False).head(top)
    suma_total_top = most_used.suma_total.sum()

    total_usos = most_used['count'].sum()
    porcentaje = (suma_total_top / suma_total_df) * 10000
    porcentaje = int(porcentaje) / 100
    print(f'Las {top} rutas mas demandadas aportan {porcentaje}% de las ganancias, en un total de {total_usos} servicios')

# %%
