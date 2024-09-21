import random
import os
from colorama import Fore
import pandas as pd



def volante():
    return list(range(1, 61))


def sortear():
    listaSort = random.sample(volante(), 6)
    return sorted(listaSort)


def aposta():
    jogo = []
    print("Digite apenas número inteiro entre 1 e 60!")
    while True:
        try:
            for i in range(1, 7):
                num = int(input(f"Digite o {i}º número: "))
                while True:
                    if num > 60:
                        print("A mega sena só aceita números menores ou igual a 60")
                        num = int(input(f"Digite o {i}º número: "))
                    elif num <= 0:
                        print("0 ou números negativos não são permitidos")
                        num = int(input(f"Digite o {i}º número: "))
                    elif num in jogo:
                        print("Este número já foi digitado!")
                        num = int(input(f"Digite o {i}º número: "))
                    else:
                        jogo.append(num)
                        break
            os.system("cls")
            return sorted(jogo)
        except ValueError:
            print("Valor invalido digite apesnumero inteiros entre 1 e 60!")


def acerto(jogo, resposta):
    acert = 0
    for i in jogo:
        if i in resposta:
            acert += 1
    return acert


def ganhador(acert):
    if acert == 6:
        return "BARABÉNS VOCÊ É O GANHARDOR DA MEGA_SENA!!!"
    elif acert == 5:
        return "BARABÉNS VOCÊ ACERTOU 5 DEZENAS, VOCÊ GANHOU A QUINA DA MEGA-SENA!!!"
    elif acert == 4:
        return "BARABÉNS VOCÊ ACERTOU 4 DEZENAS, VOCÊ GANHOU A QUADRA DA MEGA-SENA!!!"
    else:
        return "Não foi desta vez, você não ganhou!!!"


while True:
    os.system("cls")

    print("Vamos fazer uma aposta na MEGA-SENA!\n\n")
    resp1 = str(
        input("Você quer digitar ou gerar um jogo ( D ou G)").lower())

    if resp1 == "d":
        jogo = aposta()
    elif resp1 == "g":
        jogo = random.sample(volante(), 6)

    resposta = sortear()
    pont = acerto(jogo, resposta)
    print("\n")
    print(Fore.YELLOW + f"Números sorteados: {resposta}" + Fore.RESET)
    print(Fore.GREEN + f"Seu jogo: {jogo}" + Fore.RESET)
    print("\n")
    print(f"Você teve um total de {pont} acertos")
    print(ganhador(pont))
    print("\n")

    resp2 = str(input("Você quer vazer outro jogo? (S ou N)").lower())
    if resp2 == "n":
        print("Fim do programa!")
        break
    else:
        os.system("cls")
