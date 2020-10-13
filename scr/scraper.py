# -*- coding: utf-8 -*-

"""
Created 13/10/2020
@authors: José Luis Rivas Calduch y Mariano Jimenez Barca
"""

# Librerias

import requests
from bs4 import BeautifulSoup

# Cargamos en una variable la dirección de la página sobre la queremos raspar

str = 'http://www.ahe.es/bocms/sites/ahenew/estadisticas/indices-referencia/archivos/historico-de-indices.htm?version=106'


# Llamamos a la página y comprobamos que codigo devuelto por el servidor HTTP es el 200
page = requests.get(str)

status = page.status_code

# Si el codigo es el 200 continuamos con la ejecución

if status == 200 :
        
    soup = BeautifulSoup(page.content)
        
    print(soup)
        
else :
    
    print('La conexión con la página ha sido erronea!!')
            
