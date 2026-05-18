from pprint import pprint # para prints mais bonitos
from bs4 import BeautifulSoup as bs # para limpar as tags e entidades html
import re


def limpar_texto(texto_sujo):
    """
    Remove URLs, tags HTML, espaços e quebras de linha extras de um texto.
    
    Args:
        texto_sujo (str): Texto com formatação e caracteres indesejados
    
    Returns:
        str: Texto limpo e normalizado
    """
    texto_limpo = re.sub(r"\n.+://.+", "\n", texto_sujo, count = 1)
    texto_limpo = bs(texto_limpo, "html.parser").get_text()
    texto_limpo = re.sub(r".+\n", "\n", texto_limpo, count = 1)
    texto_limpo = re.sub(r" +"," ",texto_limpo)
    texto_limpo = re.sub(r"\n+","\n",texto_limpo)
    return texto_limpo.strip()

def limpar_json(dados):
    """
    Limpa e filtra uma lista de dicionários contendo texto.
    
    Args:
        dados (list): Lista de dicionários com chave "texto"
    """
    i = 0
    while True:
        dados[i]["texto"] = limpar_texto(dados[i]["texto"])
        # dados[i]["id"] = i+1 # atualiza o id (optei por manter o id original)
        if len(dados[i]["texto"]) <= 10:
            dados.pop(i)
        elif (i+1) < len(dados):
            i = i+1
        else:
            break
