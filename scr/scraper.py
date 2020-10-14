#!/usr/bin/env python
# coding: utf-8
# 13-10-2020
# Authors JoeLuis Rivas Calduch y Mariano Jimenez Barca
# Web Scrapping con Python
# 


from bs4 import BeautifulSoup;
#import pandas as pd
import requests;
import re;

str = 'http://www.ahe.es/bocms/sites/ahenew/estadisticas/indices-referencia/archivos/historico-de-indices.htm?version=106'

page = requests.get(str);  # requests.get captura un recurso http

status = page.status_code

# Si el codigo es el 200 continuamos con la ejecución

if status == 200 :

  
  soup = BeautifulSoup(page.content, "html5lib");   # https://beautiful-soup-4.readthedocs.io/en/latest/ 
  
  #table_title = soup.findAll("table")[0]
  table_data = soup.findAll("table")[1]


  currentIndex=12 # evita el rowspan 
  for row in table_data.findAll("tr"):
     columns = row.findAll("td")
     #print (len(columns))
     if currentIndex%12 == 0: # en la posicion 0 de este caso esta el año
      ano = (columns[0].text)  # AÑO
      mes =  (columns[1].text)  # mes
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
      #print (columns[0].text) # en esta posición esta el rowspan
      mes =   (columns[1].text)  # mes
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
      mes =   (columns[0].text)  # mes
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
     row = {'ano': re.sub("[\t ]", "", ano), 
            'mes': re.sub("[\t ]", "", mes), 
            'tentesp': re.sub("[\t ]", "", tentesp),
            'zeuro': re.sub("[\t ]", "", zeuro),
            'euribor':re.sub("[\t ]", "", euribor),
            'mibor':re.sub("[\t ]", "", mibor),
            'irs':re.sub("[\t ]", "", irs),
            'deuda':re.sub("[\t ]", "", deuda),
            'bancos':re.sub("[\t ]", "", bancos),
            'cajas':re.sub("[\t ]", "", cajas),
            'ceca':re.sub("[\t ]", "", ceca),
            'ahe':re.sub("[\t ]", "", ahe),
            'ced':re.sub("[\t ]", "", ced)}
   
     print (row)


else :
  print('La conexión con la página ha sido erronea!!')
        

