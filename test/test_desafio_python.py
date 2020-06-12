#Prueba Python 
#desarrollada por Sebastián Arias

import json
import requests
import sys
from itertools import groupby

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&api_key="
api_key = sys.argv[1]

def request(url, auth):
    response = requests.request("GET", url + auth)
    results = json.loads(response.text)
    return results

def photos_count(dicc):
    cam = []
    for item in dicc["photos"]:
        cam.append(item["camera"]["name"])
    
    #antes de agrupar es necesario ordenar los registros, por eso se aplicar la función sort
    cam.sort()
    #
    return {k: len(list(v)) for k, v in groupby(cam)}

def build_web_page(dicc):
    li = ""
    imagenes = {}
    for foto in response["photos"]:
        li += "\t<li><img src=\'{}\'></li>\n".format(foto["img_src"])
        imagenes[foto["id"]] = foto["img_src"]
        imagenes["camara_{}".format(foto["id"])] = foto["camera"]["name"]
    ul = "<ul>\n{}<ul>".format(li)
    return "<html>\n<head>\n</head>\n<body>\n{}\n</body>\n<html>".format(ul)  

response =request(url,api_key)

print("Cantidad de fotos por Camara: {}".format(photos_count(response)))
print(build_web_page(response))