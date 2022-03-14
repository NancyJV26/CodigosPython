#%%
import pandas  as pd
import seaborn as sns

synergy_csv = 'synergy.csv'
sldf = pd.read_csv(synergy_csv, parse_dates=[5], index_col=0)

# %%
"""
https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot
Este grafico cuenta las ocurrencias de cada categoria en un grafico de barras
Nos es util en este caso para rapidamente saber donde tenemos mas datos o cual
es el medio de transporte que se ha utilizado mas
"""
ax = sns.countplot(x='transport_mode', data=sldf)
# %%
"""
Podemos hacer un analisis de cada medio de transporte tambien por a;o, primero
tenemos que agrupar todos los datos por a;o y medio de transporte
"""
transportes_anuales = sldf.groupby(by=['year', 'transport_mode'])
valor_anual_transporte = transportes_anuales['total_value'].agg(pd.Series.sum)

info_transp_anual = pd.DataFrame()
info_transp_anual['valor_total'] = valor_anual_transporte
info_transp_anual['frecuencia'] = transportes_anuales['total_value'].describe()['count']
# %%
"""
https://seaborn.pydata.org/generated/seaborn.lineplot.html
Grafico lineal donde vemos la frecuencia de uso de cada medio de transporte a;o
tras a;o.
"""
sns.lineplot(x='year', y='frecuencia', hue='transport_mode', data=info_transp_anual)
# %%
"""
Intentemos hacer el mismo grafico pero dividiendo los datos no solo por a;o,
sino tambien por mes, necesitamos antes que nada una columna nueva con esta info
"""
sldf['month'] = sldf['date'].dt.month
# El resto de pasos son similares a los anteriores
transportes_a_m = sldf.groupby(['year', 'month', 'transport_mode'])
valor_a_m_transporte = transportes_a_m['total_value'].agg(pd.Series.sum)

info_transp_a_m = pd.DataFrame()
info_transp_a_m['valor_total'] = valor_a_m_transporte
info_transp_a_m['frecuencia'] = transportes_a_m['total_value'].describe()['count']
# %%
sns.lineplot(x='ano_mes', y='frecuencia', hue='transport_mode', data=info_transp_a_m)
# %%
