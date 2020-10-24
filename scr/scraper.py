#!/usr/bin/env python
# coding: utf-8
# 13-10-2020
# Authors Jose Luis Rivas Calduch y Mariano Jimenez Barca
# Web Scrapping con Python
# 


from bs4 import BeautifulSoup;
import pandas as pd
import requests;
import re;
import os
from datetime import date


# this function converts month in strings into numbers. Month on original dataset are in spanish and english 

def month_st2nu(month):
    months = {"Ene": 1, "Jan": 1, "Feb": 2, "Mar": 3, "Abr":4, "Apr":4, "May":5, "Mai":6, "Jun":6, 
              "Jul":7, "Ago":8, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dic":12, "Dec":12
    }
    out = months[month]
    return out


# getting data from INE API

dfINE = []  # defining work variables

rowsINE = [] # here we will put finish result

# INE API

# compraventa de viviendas. ETDP1826

url_plantilla = 'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?nult={num_datos}'

codigo = "ETDP1826"
num_datos = 200

url = url_plantilla.format(codigo=codigo, num_datos=num_datos)

respuesta = requests.get(url)

datos = respuesta.json()

for x in datos['Data']:
    
    viviendas = x['Valor']
    mes = x['FK_Periodo']
    ano = x['Anyo']
    
    rowINE = {
           'viviendas': int(viviendas),
           'mes': int(mes),
           'ano': int(ano)
           }
    
    rowsINE.append(rowINE)
    
dfINE = pd.DataFrame(rowsINE) 


#print(dfINE)


# Getting now reference Indexes from ahe.es

# source url

str = 'http://www.ahe.es/bocms/sites/ahenew/estadisticas/indices-referencia/archivos/historico-de-indices.htm?version=106'

page = requests.get(str);  

status = page.status_code

# Only if url is loaded right, script continues running

if status == 200 :

  
    soup = BeautifulSoup(page.content, "html5lib");   # https://beautiful-soup-4.readthedocs.io/en/latest/ 
  
    table_data = soup.findAll("table")[1]
  
    dfIndex = []  # defining work variables
  
    rowsIndex = [] # here we will put finish result

    currentIndex=12 # avoid rowspan 
  
    for x in table_data.findAll("tr"):
        
        columns = x.findAll("td")
        #print (len(columns))
        if currentIndex%12 == 0: #
            
            ano = (columns[0].text)  # Year
            
            mes =  (columns[1].text)  # Month
            
            tentesp = (columns[2].text)  # T.ENT. ESPAÑA
            
            zeuro = (columns[3].text)  # ZONA EURO
            
            euribor = (columns[4].text)  # EURIBOR
            
            mibor = (columns[5].text)  # Mibor
            
            irs = (columns[6].text)  # IRS 5 años
            
            deuda = (columns[7].text)  # Deuda
            
            bancos = (columns[8].text)  # Bancos
            
            cajas = (columns[9].text)  # Cajas
            
            ceca = (columns[10].text) # CECA 
            
            ahe = (columns[11].text) # AHE
                        
            ced = (columns[12].text) # Ced
        
        elif currentIndex%12 == 1:
      
            #print (columns[0].text) # avoiding rowspan
            
            mes =   (columns[1].text)  # month
            
            tentesp = (columns[2].text)  # T.ENT. ESPAÑA
            
            zeuro = (columns[3].text)  # ZONA EURO
            
            euribor = (columns[4].text)  # EURIBOR
            
            mibor = (columns[5].text)  # Mibor
            
            irs = (columns[6].text)  # IRS 5 años
            
            deuda = (columns[7].text)  # Deuda
            
            bancos = (columns[8].text)  # Bancos
            
            cajas = (columns[9].text)  # Cajas
            
            ceca = (columns[10].text) # CECA 
            
            ahe = (columns[11].text) # AHE
            
            ced = (columns[12].text) # Ced    
        
        else:
            
            mes =   (columns[0].text)  # month
            
            tentesp = (columns[1].text)  # T.ENT. ESPAÑA
            
            zeuro = (columns[2].text)  # ZONA EURO
            
            euribor = (columns[3].text)  # EURIBOR
            
            mibor = (columns[4].text)  # Mibor
            
            irs = (columns[5].text)  # IRS 5 años
            
            deuda = (columns[6].text)  # Deuda
            
            bancos = (columns[7].text)  # Bancos
            
            cajas = (columns[8].text)  # Cajas
            
            ceca = (columns[9].text) # CECA 
            
            ahe = (columns[10].text) # AHE
            
            ced = (columns[11].text) # Ced 
            
            #print (columns[12].text) # solo hay 12 columnas  
     
        currentIndex = currentIndex + 1

        
         # Formating exit row. Deleting  \t, - & spaces. 
         # on numeric we adopt english notation with "." instead ","
         # https://docs.python.org/3/library/re.html    
         # month is converted into numeric with ad-hoc function 
         # force conv to int in order to use as key in merging 
    
    
        rowIndex = {'ano': int(re.sub("[\t -]", "", ano)), 
               'mes': int(month_st2nu(re.sub("[\t -]", "", mes))), 
               'tentesp': re.sub("[,]", ".",re.sub("[\t -]", "", tentesp)),
               'zeuro': re.sub("[,]", ".",re.sub("[\t -]", "", zeuro)),
               'euribor':re.sub("[,]", ".",re.sub("[\t -]", "", euribor)),
               'mibor':re.sub("[,]", ".",re.sub("[\t -]", "", mibor)),
               'irs':re.sub("[,]", ".",re.sub("[\t -]", "", irs)),
               'deuda':re.sub("[,]", ".",re.sub("[\t -]", "", deuda)),
               'bancos':re.sub("[,]", ".",re.sub("[\t -]", "", bancos)),
               'cajas':re.sub("[,]", ".",re.sub("[\t -]", "", cajas)),
               'ceca':re.sub("[,]", ".",re.sub("[\t -]", "", ceca)),
               'ahe':re.sub("[,]", ".",re.sub("[\t -]", "", ahe)),
               'ced':re.sub("[,]", ".",re.sub("[\t -]", "", ced))}
   
        rowsIndex.append(rowIndex)
  
    dfIndex = pd.DataFrame(rowsIndex)
    
    # merging the two dataframes by 'ano' & 'mes' because df
    
    
    result = pd.merge(dfIndex, dfINE, how = 'left', on=['ano','mes'])  # merging by 'ano' + 'mes' https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
    
    result = result.fillna('')  #taking out NaN. subs by ''
    
    # creating a new date column 
    
    fecha = result['ano'].astype('str') + '-' + result['mes'].astype('str') + '-' + '01'
   
    result['date'] = pd.to_datetime(fecha)
        
    # creating directory in case it is not existis df = df.fillna('')

    if os.path.exists('csv') == False:
        
        os.mkdir('csv')
    
    # naming file with current date to save older files

    today = date.today()
    
    todayTofile = today.strftime("%b-%d-%Y")   #https://www.programiz.com/python-programming/datetime/current-datetime
    
    # If SO is windows '../csv/historico_indices_'+todayTofile+'.csv'
    # If SO is linux 'csv/historico_indices_'+todayTofile+'.csv'
        
    fileName = 'csv/historico_indices_'+todayTofile+'.csv'  
  
    result.to_csv(fileName, index=False)
  
    print ("Execution is finished.")

else :
  
    print('Conection to url has not been right!!')
