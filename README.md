 ![Logo UOC](img/logo_uoc_peq.png?raw=true) 

# Práctica 1: Web Scraping

## Descripción

El objetivo de la práctica es el de desarrollar un proyecto de web scraping para la asignatura Tipología y ciclo de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC).

El proyecto consiste en analizar si existe alguna relación entre el coste del dinero y el mercado de la vivienda en España. Para ello se han obtenido las series históricas mensuales de los índices de referencia del mercado hipotecario español publicados por la Asociación Hipotecaria Española en su página web, para la obtención de la información se ha desarrollado un script que obtiene los datos mediante web scrapping. Por otro lado, se han obtenido la serie histórica de compraventa mensual de viviendas publicada por el Instituto Nacional de Estadísticas Español (INE), para la obtención de la información se ha desarrollado un script de conexión a la API del INE. También se han extraído información del Ministerio de Fomento de las series históricas trimestrales del número de transacciones inmobiliarias y del precio medio de la vivienda a nivel estatal.

## Miembros del equipo

José Luis Rivas Calduch y Mariano Jiménez Barca

## Ficheros de código fuente
* **scr/scraper_def.py:** Realiza el proceso de scraping.

## Ficheros con el dataset resultado del scraping
* **csv/historico_indices_hipotecario_vivienda_{fecha obtención}.csv:** Fichero en csv con el resultado de *scraper_def.py*.

## Ficheros gráfica
* **chart/chart.ipynb:** Jupyter Notebook con el codigo del desarrollo de la gráfica.
* **chart/chart.png:** Imagen png con la gráfica.

## Recursos

* **Subirats Maté, Laila; Pérez Trenard, Diego O.; Calvo González, Mireia (2019)** Introducción al ciclo de la vida de los datos. UOC
* **Subirats Maté, Laila; Calvo González, Mireia (2019)** Web scraping. UOC

