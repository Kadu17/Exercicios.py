import random

def retornar_palvras():
    listaPalavras = ['CACHORRO', 'MACACO', 'GATO', 'GORILA', 'VACA', 'TIGRE' ]

    palavraSecretas = list(random.choice(listaPalavras))
    return palavraSecretas


def jogo(palavra_secreta):
    jogo_acabou = False
    erros = 0

    resultado = []

    for posicao in range(1, len(palavra_secreta) + 1):
        resultado.append("_")

    while jogo_acabou == False:

        #print("Palavra secreta:", " ".join(resultado))

        letra_chute = input("Qual o seu palpite: ").upper()

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


        if erros == 3:
            print("Você perdeu!")
            jogo_acabou = True



palavra = retornar_palvras()
jogo(palavra)