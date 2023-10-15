import requests
from bs4 import BeautifulSoup
import re

#* URL
url = "https://www.bcv.org.ve/"
response = requests.get(url)
html = response.content

#! print(html)

#* Analizar el HTML utilizando 
soup = BeautifulSoup(html,"html.parser")

#*Obtener el titulo de la pagina
title = soup.title.string
print("="*40)
print(f" Titulo : {title}")
# print("*"*100)
#*Obtener todos los enlases de la pagina
links = []
for link in soup.find_all("a",href=True):
    if "http" in link["href"]:
        links.append(link["href"])
        
#! print(links)        
# print("*"*100)
#* obtener todos los encabezados de la pagina
encabezados = []

for encabezado in soup.find_all(re.compile("^h[1-6]")):
    encabezados.append(encabezado.text.strip())
 
#!print(encabezados)        
# print("*"*100)    
#* obtener las imagenes principales

img = soup.find("img",{"class":"img-responsive"})
img_url = "https:"+ img["src"]

#! print(f"la imagen es {img_url}")        
print("="*40)  

#* Obtener el precio del dolar 
div_dolar = soup.find("div",{"id":"dolar"})
dolar = div_dolar.find("strong").text
print(f"Precio del Dolar: ${dolar}") 
print("="*40) 
