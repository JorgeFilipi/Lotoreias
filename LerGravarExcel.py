import pandas as pd

# Criando um DataFrame com alguns dados
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 45],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(dados)

# Gravando o DataFrame em um arquivo Excel
df.to_excel('meu_arquivo.xlsx', index=False)

print("Arquivo Excel criado com sucesso!")
# Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.

