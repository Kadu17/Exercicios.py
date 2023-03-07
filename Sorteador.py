import random
from threading import Timer



def tempo(texto="Que pena, seu tempo esgotou!"):
    print(f'Fim de jogo -- {texto}')
    pid = os.getpid()
    os.kill(pid, -1)


temporizador = Timer(60, tempo)
temporizador.start()
s = random.randint(0, 100)

vida = 50
t = 3

print('Tente adivinhar o número!')
print('-'*36)

while t != 0 or vida != 0:
    print(s)
    n = int(input('Digite um número de sua escolha: '))
    t -= 1
    chute = abs(s - n)
    vida -= chute
    print('Vida: ', vida)
    if vida <= 0:
        print('Que pena! Suas vidas esgotaram!')
        break
    if n != s:
        print('Você errou!')
        print('-' * 35)
    else:
        print('Você acertou!')
        break
    if t == 0:
        print('Você esgotou todas as suas chances!')
        break
print('-'*36)




