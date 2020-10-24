 ![Logo UOC](img/logo_uoc_peq.png?raw=true) 

# Práctica 1: Web Scraping

## Descripción

El objetivo de la presente práctica es el de desarrollar un proyecto de web scraping para la asignatura *Tipología y ciclo de los datos*, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC).

El proyecto consiste en analizar si existe alguna relación entre el coste del dinero y el mercado de la vivienda. Para ello se han obtenido las series históricas de los índices de referencia del mercado hipotecario español publicados por la *Asociación Hipotecaria Española* en su pagina web, para la obtención de la información se ha desarrollado un script que obtiene los datos mediante web scrapping. Por otro lado, se han la serie histórica de compraventa de viviendas publica por *Instituto Nacional de Estadísticas Español* (INE), para la obtención de la información se ha desarrollado un script de conexión a la API del INE. Por último lugar, se ha analizado mediante el desarrollo de una gráfica la existencia de relación entre ambas series.

## Miembros del equipo

José Luis Rivas Calduch y Mariano Jiménez Barca

## Ficheros de código fuente
* **scr/scraper.py:** Realiza el proceso de scraping.

## Ficheros con el dataset resultado del scraping
* **csv/historico_indices.csv:** Fichero en csv con el resultado de *scraper.py*.

## Ficheros gráfica
* **chart/chart.ipynb:** Jupyter Notebook con el codigo del desarrollo de la gráfica.
* **chart/chart.png:** Imagen png con la gráfica.

## Recursos

* **Subirats Maté, Laila; Pérez Trenard, Diego O.; Calvo González, Mireia (2019)** Introducción al ciclo de la vida de los datos. UOC
* **Subirats Maté, Laila; Calvo González, Mireia (2019)** Web scraping. UOC

