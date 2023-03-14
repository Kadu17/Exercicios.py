
import random

#criando a lista com as palavras secretas
listaPalavrasSecretas = ['cachorro', 'macaco', 'vaca', 'gorila', 'tigre', 'gato']

#pega uma palavra aleatoria e guarda na variavel PalavraSecreta
palavraSecreta = list(random.choice(listaPalavrasSecretas))

# cria uma variavel de texto chamada resultado com "_" correspondentes
resultado = []

# quantidade de letras da palavra secreta
for posicao in range(1, len(palavraSecreta) + 1):
    resultado.append("_")

# mostra os "_" correspondentes a quantidade de letras da palavra secreta
print("Palavra secreta:", " ".join(resultado))

jogo_acabou = False
erros = 0

# impede o programa de acabar
while jogo_acabou == False:
    # cria uma variavel pra guardar a letra que a pessoa digitar
    letra_chute = input("Qual o seu palpite: ")

    # verifica se a letra digitada pelo usuario está dentro da palavra secreta
    if letra_chute in palavraSecreta:

        for posicao_da_letra in range(0, len(palavraSecreta)):

            if palavraSecreta[posicao_da_letra] == letra_chute:
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
