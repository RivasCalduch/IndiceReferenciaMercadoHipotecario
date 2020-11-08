#!/usr/bin/env python
# coding: utf-8
# 08-11-2020
# Authors Jose Luis Rivas Calduch y Mariano Jimenez Barca
# Web Scrapping con Python
# 

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import os
from datetime import date


# this function converts a month given in 3 chars strings into numbers. Month on original dataset are in spanish and english 

def month_st2nu(month):
    months = {"Ene": 1, "Jan": 1, "Feb": 2, "Mar": 3, "Abr":4, "Apr":4, "May":5, "Mai":6, "Jun":6, 
              "Jul":7, "Ago":8, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dic":12, "Dec":12
    }
    out = months[month]
    return out


# this funtion gets data from INE and return a dataframe to be merged. Parameters are code: INE code 
# num_data: number of data, data: if data are by month by quarter o semestrial.

def from_INE(code, num_data, data):
    
    dfAPI_INE = []  # defining work variables
    
    rowsAPI_INE = [] # here we will put finish result
    
    url_plantilla = 'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?nult={num_datos}'

    url = url_plantilla.format(codigo=code, num_datos=num_data)

    respuesta = requests.get(url)

    datos = respuesta.json()

    for x in datos['Data']:            # datos is JSON format. Data gets the data
    
        valor = x['Valor']
        periodo = x['FK_Periodo']
        ano = x['Anyo']
        if data ==6:                   # when data is semestral periodo = each 6 months.
            if periodo == 26:
                periodo = 1
            else: 
                periodo = 7
    
        if data ==3:                   # when data is by quarter, periodo = each 3 months.
            if periodo == 19:
                periodo = 1
            if periodo == 20: 
                periodo = 4
            if periodo == 21:
                periodo = 7
            if periodo == 22: 
                periodo = 10
        rowINE = {                      # building rows from each INE row
           code: valor,
           'mes': int(periodo),
           'ano': int(ano)
            }
    
        rowsAPI_INE.append(rowINE)
    
    dfAPI_INE = pd.DataFrame(rowsAPI_INE) 
    
    return dfAPI_INE

# This function gets data from am excel file from Ministerio de fomento. Parameters are
# execel_in: excelfile name with extension and row number where data start from.

def API_FOM(excel_in, indice):

    url_plantilla = 'https://apps.fomento.gob.es/BoletinOnline2/sedal/{codigo}'

    url = url_plantilla.format(codigo=excel_in)
    

#https://pandas.pydata.org/docs/user_guide/io.html#excel-files

    rowsFOM = []                   # here we will put finish result

    excel = pd.ExcelFile(url)

#
# All we need is just one row (number) where it is located the total amount for all the country 
# structure file is very concret. dividing data into different sheets all of them with the same format.
# There is not a key because data is dividing into sheets
#

    a = 2003  
    for sheet in  (excel.sheet_names):                 # for all sheets in a file
    
        s = pd.read_excel(url, sheet_name=sheet)
        s = s.loc[indice]
        s = s[2:]                                   # s is the row where data is located in all sheets
        t = 4
    
        for x in s:                                 # x is the data for each year.
                                                    # year and month is building from first position.
            if t % 4 == 0:
                a = a + 1
            valor = x
            ano = a
            mes = (t%4*3+1)
            row_s = {
            excel_in : valor,
            'ano' : ano,
            'mes' : mes
                }
            rowsFOM.append(row_s)                   # building fomento data row from each excel
            t=t+1

    dfrowsFOM = pd.DataFrame(rowsFOM)
    
    return dfrowsFOM

# getting houses selling price from idealista.com 
# while idealista does not allow robots we use selenium (in a very simple way) to avoid control and scrape data

url = 'https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/historico/'

driver = webdriver.Firefox()             # defining driver for selenium

driver.get(url)                          # driver opens browser and url as an human being
 
html = driver.page_source                # Now that url is opened html is loaded in a variable

driver.close()                           # closing browser

# Now we have colected html we can use beautiful soup

soup = BeautifulSoup(html, "html5lib");   # https://beautiful-soup-4.readthedocs.io/en/latest/ 
  
table_data = soup.findAll("table")[0]

rowsIdealista1 = []

cont = 0

for x in table_data.findAll("tr"):
    
    if cont != 0:                   # first list is empty
    
        columns = x.findAll("td")
    
        fecha = (columns[0].text)   # fecha
        
        preciom2 =  (columns[1].text)  # precio m2
            
        varmes = (columns[2].text)  # variación mensual
        
        vartri = (columns[3].text)  # variación trimestral
            
        varanual = (columns[4].text) # variación anual
    
        # we adapt format with regex. 
        # spanish numeric notation is transformed into english (.) (,)
        # delete all character in numeric fields
    
        rowIdealista = {'mes':  int(month_st2nu(fecha.split()[0][0:3])),  # format "Mes Año: Octubre 2019"
                        'ano':  int(fecha.split()[1]),                    # split fecha into two: mes and ano.
                        'precio_venta_m2': float(re.sub("[.]", "",re.sub(" €/m2", "",preciom2))) 
                        }
    
        rowsIdealista1.append(rowIdealista)
        
        
    cont = cont + 1
    
dfIdealista1 = pd.DataFrame(rowsIdealista1)


# Now we renting prices from Idealista with the same strategy

url = 'https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/alquiler/historico/'

driver = webdriver.Firefox()         # defining driver for selenium

driver.get(url)                      # driver opens browser and url as an human being
                                     
html = driver.page_source            # Now that url is opened html is loaded in a variable

driver.close()                       # closing browser

# Now we have colected html we can use beautiful soup
                                          
soup = BeautifulSoup(html, "html5lib");   # https://beautiful-soup-4.readthedocs.io/en/latest/ 
  
table_data = soup.findAll("table")[0]

rowsIdealista2 = []

cont = 0

for x in table_data.findAll("tr"):
    
    if cont != 0:                   # first list is empty
    
        columns = x.findAll("td")
    
        fecha = (columns[0].text)  # fecha 
        
        preciom2 =  (columns[1].text)  # precio m2
            
        varmes = (columns[2].text)  # variación mensual
        
        vartri = (columns[3].text)  # variación trimestral
            
        varanual = (columns[4].text) # variación anual
        
        # we adapt format with regex. 
        # spanish numeric notation is transformed into english (.) (,)
        # delete all character in numeric fields
        
        rowIdealista = {'mes':  int(month_st2nu(fecha.split()[0][0:3])),  # format "Mes Año: Octubre 2019"
                        'ano':  int(fecha.split()[1]),                    # split fecha into two: mes and ano.
                        'precio_alq_m2': float(re.sub("[,]", ".",re.sub(" €/m2", "",preciom2))) 
                        }
    
        rowsIdealista2.append(rowIdealista)
        
        
    cont = cont + 1
    
dfIdealista2 = pd.DataFrame(rowsIdealista2)


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
            
            #print (columns[12].text) # only 12 columns  
     
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
    
    # merging the  dataframes by 'ano' & 'mes' https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
    
     # transacciones de viviendas (trimestral)
    dfrowsTrans = API_FOM("34010110.XLS",13)

    # importe de las transacciones (trimestral)
    dfrowsValor = API_FOM("34020110.XLS",14)

    # compraventa de viviendas "ETDP1826" (mensual)
    dfINE_Viv = from_INE("ETDP1826",400,1)

    # hipotecas de viviendas "HPT34618" (mensual)
    dfINE_Hip = from_INE("HPT34618",400,1)

    # población "CP335" semestral
    dfINE_Pob = from_INE("CP335",200,6)

    # PIB a precios de mercado. variación trimestral 
    dfINE_PIB1 = from_INE("CNTR4805",400,3)

    # PIB a general variación trimestral
    dfINE_PIB2 = from_INE("IPV949",400,3)

    result = pd.merge(dfIndex, dfINE_Pob,   how = 'left', on=['ano','mes'])  
    result = pd.merge(result,  dfrowsTrans, how = 'left', on=['ano','mes'])
    result = pd.merge(result,  dfrowsValor, how = 'left', on=['ano','mes']) 
    result = pd.merge(result,  dfINE_Viv,   how = 'left', on=['ano','mes']) 
    result = pd.merge(result,  dfINE_Hip,   how = 'left', on=['ano','mes']) 
    result = pd.merge(result,  dfINE_PIB1,   how = 'left', on=['ano','mes'])
    result = pd.merge(result,  dfINE_PIB2,   how = 'left', on=['ano','mes'])
    result = pd.merge(result,  dfIdealista1,   how = 'left', on=['ano','mes'])
    result = pd.merge(result,  dfIdealista2,   how = 'left', on=['ano','mes'])
    
    
    result = result.fillna('')  #taking out NaN. subs by ''
        
    # creating directory in case it is not existis 

    if os.path.exists('csv') == False:
        
        os.mkdir('csv')
    
    # naming file with current date to save older files

    today = date.today()
    
    todayTofile = today.strftime("%b-%d-%Y")   #https://www.programiz.com/python-programming/datetime/current-datetime
    
    # If SO is windows '../csv/historico_indices_'+todayTofile+'.csv'
    # If SO is linux 'csv/historico_indices_'+todayTofile+'.csv'
        
    fileName = 'csv/historico_indices_hipotecario_vivienda_'+todayTofile+'.csv'  
  
    result.to_csv(fileName, index=False)
  
    print ("Execution is finished.")

else :
  
    print('Conection to url has not been right!!')
    

