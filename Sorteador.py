import random
from threading import Timer



def tempo(texto="Tente novamente, seu tempo esgotou!"):
    print(f'Fim de jogo -- {texto}')




temporizador = Timer(60, tempo)
temporizador.start()
s = random.randint(0, 1000)

vida = 1000
tentativas = 15

print('Tente adivinhar o número!')
print('-'*36)

while tentativas != 0 or vida != 0:
    print(s)
    n = int(input('Digite um número de sua escolha: '))
    tentativas -= 1
    chute = abs(s - n)
    vida -= chute
    print('Vida: ', vida)
    if vida <= 0:
        print('Suas vidas esgotaram!')
        break
    if n != s:
        print('Você errou!')
        print('-' * 35)
    else:
        print('Você acertou!')
        break
    if t == 0:
        print('Você acabou com todas as suas chances!')
        break
print('-'*36)


