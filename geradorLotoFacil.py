import openpyxl
import pandas as pd
import random

n = 6
numbers = range(1, 26)
# print(numbers)
dados = []
# combinations = itertools.combinations(numbers, 15)
# valid_combinations = [comb for comb in combinations if not has_long_sequence(comb)]
for i in range(n):
    jogo = random.sample(numbers, 15)
    jogo.sort()   
    dados.append(jogo)

# x = 1
# for i in valid_combinations:
#     print(i, x)
#     x +=1
for i in range(n):
    print(dados[i])   
df = pd.DataFrame(dados)
df.to_excel('Lotofacil.xlsx', index=False, header=False)

