import random
import pandas as pd
import requests


def retornar_palvras():
    listaPalavras = [['CACHORRO', 'É um animal de estimação'], ['MACACO', 'A fruta preferida dele é banana'],['GATO', 'É um felino'],['ELEFANTE', 'É um animal conhecido por ter medo de ratos' ],['VACA','Muuuh'],['LEAO','É considerado o rei da selva']]

    palavraSecreta = list(random.choice(listaPalavras))
    palavra = palavraSecreta[0]
    dica = palavraSecreta[1]
    return palavra, dica



def jogo(palavra_secreta, dica):
    jogo_acabou = False
    erros = 0

    resultado = []

    for posicao in range(1, len(palavra_secreta) + 1):
        resultado.append("_")

    while jogo_acabou == False:

        print("Palavra secreta:", " ".join(resultado))

        letra_chute = input("Qual o seu palpite: ").upper()

        if letra_chute == 'DICA':
            print(dica)
        else:
            if letra_chute in palavra_secreta:
                for posicao_da_letra in range(0, len(palavra_secreta)):

                    if palavra_secreta[posicao_da_letra] == letra_chute:
                        resultado[posicao_da_letra] = letra_chute

                print(" ".join(resultado).upper())
            else:
                print("Tente novamente! ")
                erros += 1

        if "_" not in resultado:
            print("Você ganhou!")
            jogo_acabou = True


        if erros == 10:
            print("Você perdeu!")
            jogo_acabou = True

def extrair_informaçoes():
    inf = requests.get(palavra, dica)
    print(inf)

    listaInf = {"Palavras": palavra, "Preço": dica}
    plan = pd.DataFrame(listaInf)

    plan.to_excel("py.teste.xlsx")





palavra, dica = retornar_palvras()
jogo(palavra, dica)
