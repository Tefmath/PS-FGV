# Desafio Técnico — Estágio em Ciência de Dados

## Como rodar o projeto

1. Criar e ativar ambiente virtual:

```bash
python -m venv .venv

.\.venv\Scripts\activate 
```

2. Instalar as dependências:

```
pip install -r requirements.txt
```

3. Abrir o arquivo ```notebook.ipynb``` e rodar todas as células (Run All)

## Explicando minhas decisões

Escolhi excutar o projeto na versão 3.12.10 do python por motivos de ser a versão mais estável até o momento, estava enfrentando alguns problemas com as versos mais recentes que estão ainda na fase de bug fix.

Após algumas pesquisas sobre a biblioteca ```sentence-transformers``` e seus modelos,  fiquei indecisa na escolha entre dois modelos específicos, o [paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) e o [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2), muito inspirada por [esse site](https://sbert.net/docs/sentence_transformer/pretrained_models.html) que recomendou bastante o uso desses dois modelos por conta de oferecerem melhor qualidade e terem sido treinados com dados paralelos para mais de 50 idiomas, sendo então adequados para nosso projeto.
Decidi que usaria os dois modelos e analisaria ao final qual performava melhor.

## Avaliação qualitativa dos resultados

Analisando a Etapa 3 do ```notebook.ipynb```, cheguei na conclusão de que ambos modelos performaram muito bem no quesito achar documentos similares à pesquisa feita, porém, o que se destaca mais no geral parece ser o modelo **paraphrase-multilingual-mpnet-base-v2**. 

A diferença de escores entre os dois modelos é muito pouca, porém o do **Mpnet-base-v2** parece ser maior em algumas buscas. Além disso, esse modelo costuma capturar melhor nuances linguísticas e relações semânticas, e como nossa base não é muito grande, então não há a necessidade de utilizarmos um modelo que seja vantajoso pelo custo computacional, como o **MiniLM-L12-v2**. Escolhi representar os resultados como um top 5 dos artigos mais similares à pesquisa. 

Talvez a implementação de ferramentas como lematização, stemização e remoção de stopwords na etapa da limpeza ajudassem a melhorar ainda mais a performance desses modelos. 




