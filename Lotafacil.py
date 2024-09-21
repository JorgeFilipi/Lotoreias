import requests
import random
import pandas as pd


def gerarResultado():

    url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        resultado = {
            "Concurso": [data["concurso"]],
            "Data": [data["data"]],
            "Dezenas sorteadas": [", ".join(data["dezenas"])]
        }
        return resultado
    else:
        print("Erro ao acessar a API:", response.status_code)
        return None

def obterResultadoLotofacil(concurso):
    
    url = f"https://loteriascaixa-api.herokuapp.com/api/lotofacil/{concurso}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Concurso:", data["concurso"])
        print("Data:", data["data"])
        print("Dezenas sorteadas:", data["dezenas"])
    else:
        print("Erro ao acessar a API:", response.status_code)


def gerarJogo():

    jogo = random.sample(range(1, 26), 15)
    jogo.sort()
    return jogo


def gerarExcel():
    
    resultado = gerarResultado()
    if resultado:
        df = pd.DataFrame(resultado)
        nome_arquivo = 'dados.xlsx'
        df.to_excel(nome_arquivo, index=False)
        print(f"Dados gravados com sucesso em {nome_arquivo}")
    else:
        print("Não foi possível gerar o Excel devido a um erro na obtenção dos resultados.")

gerarExcel()
print(gerarResultado())
n = 3199
for i in range(11):
    print(obterResultadoLotofacil(n))
    n -= 1
    print(n)
