#!/usr/bin/env python
# coding: utf-8
# 13-10-2020
# Authors Jose Luis Rivas Calduch y Mariano Jimenez Barca
# Web Scrapping con Python (serie trimestral)
 
# MERGE de dos ficheros Excell del ministerio de Fomento y una llamada a API del INE 
# numero total de transacciones de viviendas y su importe recogido del ministerio de fomento
# poblacion recogido del INE,
# Datos trimestrales excepto poblacion que es semestral. He convertido los datos del INe a trimestrales.

import pandas as pd
import requests
import os
from datetime import date


# Transacciones trimestrales de viviendas

url = "https://apps.fomento.gob.es/BoletinOnline2/sedal/34010110.XLS"

#https://pandas.pydata.org/docs/user_guide/io.html#excel-files

page = requests.get(url);  # requests.get captura un recurso http

status = page.status_code

# Si el codigo es el 200 continuamos con la ejecución

if status == 200 :

    rowsTrans = []
    
    excel = pd.ExcelFile(url)
    
    #
    # All we need is just one row (number 13) where it is located the total amount for all the country 
    # 
    
    a = 2003  
    
    for sheet in  (excel.sheet_names):  # for all sheets in a file
        
        s = pd.read_excel(url, sheet_name=sheet)
        s = s.loc[13]
        s = s[2:]
        t = 4
        
        for x in s:
        
            if t % 4 == 0:
                a = a + 1
            transacciones = x
            ano = a
            trimestre = t%4+1
            row_s = {
                'transacciones' : transacciones,
                'ano' : ano,
                'trimestre' : trimestre
                    }
            rowsTrans.append(row_s)
            t=t+1
    
    dfrowsTrans = pd.DataFrame(rowsTrans)

    print ("Execution is finished.")  # para saber que ha terminado

else :
  
    print('Conection to url has not been right!!')

#
# valor de las transacciones de viviendas
#

url = "https://apps.fomento.gob.es/BoletinOnline2/sedal/34020110.XLS"

page = requests.get(url);  # requests.get captura un recurso http

status = page.status_code

# Si el codigo es el 200 continuamos con la ejecución

if status == 200 :

    rowsValor = []
    
    excel = pd.ExcelFile(url)
    
    a = 2003  
    for sheet in  (excel.sheet_names):
        
        s = pd.read_excel(url, sheet_name=sheet)
        s = s.loc[14]
        s = s[2:]
        t = 4
        
        for x in s:
        
            if t % 4 == 0:
                a = a + 1
            valor = x
            ano = a
            trimestre = t%4+1
            row_s = {
                'valorTransac' : valor,
                'ano' : ano,
                'trimestre' : trimestre
                    }
            rowsValor.append(row_s)
            t=t+1
    
    
            dfrowsValor = pd.DataFrame(rowsValor) 

    print ("Execution is finished.")  # para saber que ha terminado

else :
  
    print('Conection to url has not been right!!')

# merge los dos ficheros de ministerio de fomanto

result = pd.merge(dfrowsValor, dfrowsTrans, how = 'left', on=['ano','trimestre'])  # merging by 'ano' + 'trimestre' https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
    
result = result.fillna('')  #taking out NaN. subs by ''


# API del INE:

dfINEPob = []  # defining work variables

rowsINEPob = [] # here we will put finish result

# INE API

# Población. semestral

url_plantilla = 'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?nult={num_datos}'

codigo = "CP335"
num_datos = 1000

url = url_plantilla.format(codigo=codigo, num_datos=num_datos)

respuesta = requests.get(url)

datos = respuesta.json()

for x in datos['Data']:
    
    valor = x['Valor']
    periodo = x['FK_Periodo']
    anyo = x['Anyo']
    if periodo%2 == 0:
        periodo = 1
    else: 
        periodo = 3  
    
    # como es semestral doblo el registro y le doy el mismo valor a los dos trimestres pero el periodo lo cambio
    
    rowINE1 = {
           'poblacion':valor,
           'trimestre':periodo ,
           'ano':anyo
           }
    rowINE2 = {
           'poblacion':valor,
           'trimestre':periodo + 1 ,
           'ano':anyo
           }
    rowsINEPob.append(rowINE1)
    rowsINEPob.append(rowINE2)
    
dfowsINEPob = pd.DataFrame(rowsINEPob)

result = pd.merge(result, dfowsINEPob, how = 'left', on=['ano','trimestre'])  # merging by 'ano' + 'trimestre' https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
    
result = result.fillna('')  #taking out NaN. subs by ''

result

# creating directory in case it is not existis df = df.fillna('')

if os.path.exists('csv') == False:
        
   os.mkdir('csv')
    
    # naming file with current date to save older files

today = date.today()
    
todayTofile = today.strftime("%b-%d-%Y")   #https://www.programiz.com/python-programming/datetime/current-datetime
    
# If SO is windows '../csv/historico_indices_'+todayTofile+'.csv'
# If SO is linux 'csv/historico_indices_'+todayTofile+'.csv'
        
fileName = '../csv/historico_indices_trimestral_'+todayTofile+'.csv'  
  
result.to_csv(fileName, index=False)
