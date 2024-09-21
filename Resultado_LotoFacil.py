import requests

url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Concurso:", data["concurso"])
    print("Data:", data["data"])
    print("Dezenas sorteadas:", data["dezenas"])
else:
    print("Erro ao acessar a API:", response.status_code)
