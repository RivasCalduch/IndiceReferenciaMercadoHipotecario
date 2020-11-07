 ![Logo UOC](img/logo_uoc_peq.png?raw=true) 

# Práctica 1: Web Scraping

## Miembros del equipo

José Luis Rivas Calduch y Mariano Jiménez Barca

## Descripción

El objetivo de la práctica es el de capturar datos relativos al mercado inmobiliario para posteriormente realizar una analisis de los mismos. Esta practica se engloba dentro del la asignatura Tipología y ciclo de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC).

Los datos a capturar se corresponden con el mercado inmobiliario español en su conjunto desde el punto de vista temporal y si existe alguna relación entre el coste del dinero, población y el mercado de la vivienda en España. 

## Contexto

Dado que existen muchos datos oficiales al respecto, hemos procurado obtener datos de diferentes fuentes y mediante distintos métodos de cara a poner en práctica varias técnicas. 

## Título del Dataset

historico_indices_hipotecario_vivienda


## Descripción del Dataset

El data set se corresponde con una relación temporal de indices económicos relacionados con el mercado hipotecario extraidos de diferentes fuentes.

Para ello se han obtenido las series históricas mensuales de los índices de referencia del mercado hipotecario español publicados por la Asociación Hipotecaria Española en su página web, la serie histórica de compraventa mensual de viviendas, la población y el PIB publicados por el Instituto Nacional de Estadísticas Español (INE) y las series históricas trimestrales del número de transacciones inmobiliarias y del precio medio de la vivienda a nivel estatal en formato excel del Ministerio de Fomento.

## Representación gráfica

![Representacion_grafica](img/foto2.PNG?raw=true) 

## Contenido

El contenido del dataset es el siguiente:

ano = Año referencia del indicador
mes = mes referencia del indicador
tentesp = Tipo medio préstamos hipotecarios adquisición de vivienda libre A más de tres años territorio España. Origen A.H.E. .Dato mensual. en %
zeuro =  Tipo medio préstamos hipotecarios adquisición de vivienda libre. ZONA EURO. Origen A.H.E. Dato mensual. en %
euribor = Euribor. Dato mensual. Origen A.H.E.. en %            
mibor = Indice Mibor. Dato Mensual. Origen A.H.E.. en %
irs = Interes Rate Swap. Dato Mensual. Origen A.H.E.. en %
deuda = Interés deuda. Dato Mensual. Origen A.H.E.. en %
bancos = IRPH. Tipo medio préstamos hipo. a más de 3 años adq.vivienda libre. Tipo de interés bancos. Origen A.H.E.. Dato mensual. en %
cajas = IRPH. Tipo medio préstamos hipo. a más de 3 años adq.vivienda libre. Tipo de interés cajas . Origen A.H.E..Dato mensual. en %
ceca = IRPH. Tipo medio préstamos hipo. a más de 3 años adq.vivienda libre. Tipo de interés CECA. Origen A.H.E.. Dato mensul. en %
ahe = Referencia tipo hipotecario A.H.E. Origen A.H.E.. Dato trimestral. en %
ced = referencia ced. Origen A.H.E.. Dato mensual. en %
34010110.XLS = transacciones de viviendas. Origen Ministerio de Fomento. Dato trimestral. en unidades.
34020110.XLS = importe de las transacciones de viviendas. Origen Ministerio de Fomento. Dato trimestral. en euros.
ETDP1826 = número de compraventa de viviendas. Origen INE. Dato mensual. en unidades
HPT34618 = hipotecas de viviendas. Origen INE. Dato mensual. en unidades
CP335 = población. Origen INE. Dato semestral. en unidades
CNTR4805 = PIB a precios de mencado. variación trimestral. Origen INE. en %
IPV949 = PIB general. variación trimestral. Origen INE. en %

Por un lado, los datos del AHE se han recogido mediante un scraper en Python. Los datos del INE se han recogido mediante acceso vía API del INE. Los datos del ministerio de Fomento se han recogido a partir del acceso a un fichero Excel.

Cada una de estas técnicas necesitan un procesado posterior así como un fusionado.

## Inspiración

El mercado inmobiliario en España aporta aproximadamente el 10.5% del PIB (datos de 2019 https://es.statista.com/estadisticas/549634/aportacion-de-las-actividades-inmobiliarias-al-pib-en-espana/). Tras la crisis financiera de 2008 los precios de las viviendas vuelven a estar en términos casi semejantes a antes de la crisis.

La pandemia ha bajado de nuevo los precios pero intentar conocer la evolución del conjunto de precios en consonancia con otras variables macro estadísticas es interesante de cara a poder predecir  otras burbujas o situaciones similares. 

## Licencia

La licencia se recoge en el documento LICENSE de este mismo proyecto.

## Codigo Zenodo

El codigo zenodo es...

## Recursos

* **Subirats Maté, Laila; Pérez Trenard, Diego O.; Calvo González, Mireia (2019)** Introducción al ciclo de la vida de los datos. UOC
* **Subirats Maté, Laila; Calvo González, Mireia (2019)** Web scraping. UOC

