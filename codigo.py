import json
from pprint import pprint # para prints mais bonitos
from bs4 import BeautifulSoup as bs # para limpar as tags e entidades html
import re

# Abrindo o json
with open("dados/noticias_brutas.json","r",encoding="utf-8") as file:
    data = json.load(file)

#pprint(data)

def clean_text(texto_sujo):
    texto_limpo = re.sub(r"\n.+://.+", "\n", texto_sujo, count = 1)
    texto_limpo = bs(texto_limpo, "html.parser").get_text()
    texto_limpo = re.sub(r".+\n", "\n", texto_limpo, count = 1)
    texto_limpo = re.sub(r" +"," ",texto_limpo)
    texto_limpo = re.sub(r"\n+","\n",texto_limpo)
    return texto_limpo.strip()

#print(clean_text(data[17]["texto"]))

def clean_json():
    i = 0
    while True:
        data[i]["texto"] = clean_text(data[i]["texto"])
        if len(data[i]["texto"]) <= 10:
            data.pop(i)
        elif (i+1) < len(data):
            i = i+1
        else:
            break

clean_json()

pprint(data)