#!/usr/bin/env python
# coding: utf-8
# 19-10-2020
# Authors Jose Luis Rivas Calduch y Mariano Jimenez Barca
# Python Web Scrapping INE API 
# 

import datetime
import requests
import pandas as pd

i = 0 # Utilizamos un contador para igualar las series dado que PIB es menor IPV

df1 = []  # defining work variables
df2 = []  # defining work variables

rows1 = [] # here we will put finish result
rows2 = [] # here we will put finish result

# INE API

# Total Nacional. Datos ajustados de estacionalidad y calendario. Producto interior bruto a precios de mercado. Variación trimestral. Precios corrientes.

url_plantilla = 'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?nult={num_datos}'

codigo = "CNTR4805"
num_datos = 100

url = url_plantilla.format(codigo=codigo, num_datos=num_datos)

respuesta = requests.get(url)

datos = respuesta.json()

print(datos['Nombre'])

for x in datos['Data']:
    
    fecha = datetime.date.fromtimestamp(x['Fecha'] // 1000)
    
    var_GDP = x['Valor']
    
    row = {'fecha': fecha,
           'var_GDP':var_GDP}
    
    rows1.append(row)
    
    i = i + 1  
    
df1 = pd.DataFrame(rows1) 

# Total Nacional. General. Variación trimestral. 

codigo = "IPV949"
num_datos = i

url = url_plantilla.format(codigo=codigo, num_datos=num_datos)
respuesta = requests.get(url)

datos = respuesta.json()

for x in datos['Data']:
    
    fecha = datetime.date.fromtimestamp(x['Fecha'] // 1000)
    
    var_IPV = x['Valor']
    
    row = {'fecha': fecha,
           'var_GDP':var_IPV}
    
    rows2.append(row)
    
df2 = pd.DataFrame(rows2)

result = pd.merge(df1, df2, on='fecha')

print(result)


 


