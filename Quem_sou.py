import pandas as pd
import random


class Jogo:

    def __init__(self):
        self.__cont = 0
        self.__pontos = 25

    def lista(self):
        lista_de_dicas = [['BUZZ LIGHTYEAR', 'Um brinquedo do Wandy', 'Patrulheiro espacial', '"Ao infinito e alem"'],
                          ['ARIEL', 'Vive no mar', 'Ruiva', 'Sereia'],
                          ['PETER PAN', 'Menino de espirito livre e travesso', 'Nunca cresce', 'Terra do nunca...'],
                          ['OLAF', 'Gosta de abraços quentinhos', 'Foi criado por uma princesa', 'Boneco de neve'],
                          ['CINDERELA', 'Loira', 'Madrasta má', 'Sapatinho de cristal']]

        return lista_de_dicas

    def palpite(self,palavra_certa,dicas):
        if self.__cont == 0:
            self.__cont += 1
            print(f"A primeira dica é: {dicas[0]}")

        palpite = input("Digite o seu palpite: ").upper()
        if palpite == palavra_certa:
            print("Parabéns, você acertou!")
            print(f"Seus pontos foram {self.__pontos}")
            exit()

        else:
            if self.__cont == 1:
                print(dicas[1])
                self.__cont += 1
                self.__pontos -= 5

            elif self.__cont == 2:
                print(dicas[2])
                self.__cont += 1
                self.__pontos -= 5

            elif self.__cont == 3:
                print(dicas[3])
                self.__cont += 1
                self.__pontos -= 5
            else:
                print('Você perdeu')
                exit()







jogo = Jogo()
lista = jogo.lista()

abertura2 = input("|---------------------------------------------|\n"
                  "|               SEJA BEM VINDO                |\n"
                  "|    O TEMA DO JOGO É PERSONAGENS DA DISNEY   |\n"
                  "|       PRESSIONE ENTER PARA CONTINUAR        |\n"
                  "|---------------------------------------------|\n")

n = input("\t\t Digite o seu nome: ").upper()


abertura1 =print("|---------------------------------------------|\n"
                f"|               OLÁ {n}                      |\n"
                 "|          VAMOS COMEÇAR O JOGO!              |\n" 
                 "|---------------------------------------------|\n")
personagem_escolhido = random.choice(lista)
while True:
    jogo.palpite(personagem_escolhido[0], personagem_escolhido[1:4])
