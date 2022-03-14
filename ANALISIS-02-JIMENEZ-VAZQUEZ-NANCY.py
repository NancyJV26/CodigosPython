# -*- coding: utf-8 -*-
"""ANALISIS-02-JIMENEZ-VAZQUEZ-NANCY.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CES_UXdwePUpW95pFwciE2J4JnWzG4tI
"""

#Subir archivos de Synergy
from google.colab import files
files.upload()

#Bibliotecas que se ocupan
import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("synergy_logistics_database.csv")

exportacion = datos[datos['direction']== 'Exports']
importacion = datos[datos['direction']== 'Imports']
gtotal=datos['total_value'].sum()
gtotal

"""Parte 1: Rutas de Exportación e Importación

Top 10 Rutas de Exportación
"""

r_total = datos.groupby(['direction','origin','destination','transport_mode'])
suma = r_total.sum()['total_value']
r_total = r_total['total_value'].describe()
r_total['suma_t'] = suma
r_total = r_total.reset_index()

#rutas de exportaciones
r_exportacion = r_total[r_total['direction']=='Exports']
top_exportacion= r_exportacion.sort_values(by='count',ascending=False).head(10)
top_exportacion.to_excel('Toprutas_exportaciones.xlsx')
top_exportacion

"""Top 10 Rutas de Importación"""

r_importacion = r_total[r_total['direction']=='Imports']
top_importacion= r_importacion.sort_values(by='count',ascending=False).head(10)
top_importacion.to_excel('Toprutas_importaciones.xlsx')
top_importacion

"""Parte 2: Medio de Transporte Utilizado

Exportaciones
"""

t_exportacion=exportacion.groupby(['transport_mode'])
top_t_exportacion=t_exportacion.count()['total_value']
top_t_exportacion=top_t_exportacion.reset_index()
ganancia_exportacion=t_exportacion['total_value'].sum()
ganancia_exportacion=ganancia_exportacion.reset_index()
top_t_exportacion['ganancia_exportacion']=ganancia_exportacion['total_value']
top_t_exportacion['ganancia_exportacion*10e-9']=round((top_t_exportacion['ganancia_exportacion']*0.000000001),3)
top_t_exportacion=top_t_exportacion.sort_values('total_value',ascending=False).head()
t_g_exportacion=top_t_exportacion['ganancia_exportacion'].sum()
top_t_exportacion

x_values = top_t_exportacion['transport_mode']
y_values = top_t_exportacion['total_value']
plt.bar(x_values, y_values)
plt.title('Medio más Utilizado para Exportaciones')
ax = plt.subplot()                   
ax.set_xticks(x_values)             
ax.set_xticklabels(x_values)       
ax.set_xlabel('Medio de Transporte')  
ax.set_ylabel('Cantidad de Veces Utilizado')
plt.show()
plt.close('all')

x_values = top_t_exportacion['transport_mode']
y_values = top_t_exportacion['ganancia_exportacion*10e-9']
plt.bar(x_values, y_values)
plt.title('Ganancias de los Transporte por Exportaciones')
ax = plt.subplot()                   
ax.set_xticks(x_values)             
ax.set_xticklabels(x_values)       
ax.set_xlabel('Medio de Transporte')  
ax.set_ylabel('Ganancias (MM)')
plt.show()
plt.close('all')

"""Importaciones"""

t_importacion = importacion.groupby(['transport_mode'])
top_t_importacion = t_exportacion.count()['total_value']
top_t_importacion = top_t_importacion.reset_index()
ganancia_importacion=t_importacion['total_value'].sum()
ganancia_importacion=ganancia_importacion.reset_index()
top_t_importacion['ganancia_importacion']=ganancia_importacion['total_value']
top_t_importacion['ganancia_importacion*10e-9']=round((top_t_importacion['ganancia_importacion']*0.000000001),2)
t_g_importacion=top_t_importacion['ganancia_importacion'].sum()
top_t_importacion=top_t_importacion.sort_values('total_value',ascending=False).head()
top_t_importacion

x_values = top_t_importacion['transport_mode']
y_values = top_t_importacion['total_value']
plt.bar(x_values, y_values)
plt.title('Medio más Utilizado para Importaciones')
ax = plt.subplot()                   
ax.set_xticks(x_values)             
ax.set_xticklabels(x_values)       
ax.set_xlabel('Medio de Transporte')  
ax.set_ylabel('Cantidad de Veces Utilizado')
plt.show()
plt.close('all')

x_values = top_t_importacion['transport_mode']
y_values = top_t_importacion['ganancia_importacion*10e-9']
plt.bar(x_values, y_values)
plt.title('Ganancias de los Transportes por Importaciones')
ax = plt.subplot()                   
ax.set_xticks(x_values)             
ax.set_xticklabels(x_values)       
ax.set_xlabel('Medio de transporte')  
ax.set_ylabel('Ganancias(MM)')
plt.show()
plt.close('all')

"""Parte 3: Valor total de Exportaciones e Importaciones

Exportaciones
"""

t_exp=exportacion['total_value'].sum()
g_exportacion = exportacion.groupby(['origin'])
g_exp= g_exportacion.sum()['total_value']
g_exp=g_exp.reset_index()
g_exp['porcentaje']=round((g_exp['total_value']/t_exp)*100,3)
g_exp=g_exp.sort_values('porcentaje',ascending=False).head(8)
g_exp['% acumulado']=g_exp.cumsum()['porcentaje']
g_exp.to_excel('VTotal_exportaciones.xlsx')
print('Los siguientes paises cubren alrededor del 82% de las Ganancias para Exportaciones')
g_exp

"""Importaciones"""

t_exp=importacion['total_value'].sum()
g_imp = importacion.groupby(['origin'])
g_imp= g_imp.sum()['total_value']
g_imp=g_imp.reset_index()
g_imp['porcentaje']=round((g_imp['total_value']/t_exp)*100,3)
g_imp=g_imp.sort_values('porcentaje',ascending=False).head(8)
g_imp['% acumulado']=g_imp.cumsum()['porcentaje']
g_imp.to_excel('VTotal_exportaciones.xlsx')
print('Los siguientes paises cubren alrededor del 82% de las Ganancias para Importaciones')
g_imp