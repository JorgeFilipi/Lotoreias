import pandas as pd
import requests

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

def gerarExcel():
    resultado = gerarResultado()
    if resultado:
        df = pd.DataFrame(resultado)
        nome_arquivo = 'dados.xlsx'
        df.to_excel(nome_arquivo, index=False)
        print(f"Dados gravados com sucesso em {nome_arquivo}")
    else:
        print("Não foi possível gerar o Excel devido a um erro na obtenção dos resultados.")

# Chame a função para testar
gerarExcel()

