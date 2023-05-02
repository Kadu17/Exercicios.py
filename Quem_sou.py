import pandas as pd
import random


class Jogo:

    def __init__(self):
        self.__cont = 0
        self.__pontos = 25
        self.__nome = n

    @property
    def pontos(self):
        return self.__pontos


    def lista(self):
        lista_de_dicas = [['BUZZ LIGHTYEAR', 'Um brinquedo do Wandy', 'Tem um laser no pulso', 'Melhor amigo do Woody', 'Patrulheiro espacial', '"Ao infinito e além"'],
                          ['ARIEL', 'Vive no mar', 'Filha do rei Tritão', 'Melhor amiga de um peixe', 'Ruiva', 'Sereia'],
                          ['PETER PAN', 'Menino de espirito livre e travesso','Aventureiro e ousado', 'É melhor amigo de uma fada', 'Nunca cresce', 'Terra do nunca...'],
                          ['OLAF', 'Gosta de abraços quentinhos', 'Nariz de cenoura', 'Foi criado por uma princesa','Usa galhos como braço', 'Boneco de neve'],
                          ['CINDERELA','Menina órfã', 'Loira', 'Madrasta má', 'Sapatinho de cristal', 'Fada madrinha']]

        return lista_de_dicas

    def palpite(self,palavra_certa,dicas):
        if self.__cont == 0:
            self.__cont += 1
            print(f"A primeira dica é: {dicas[0]}")

        palpite = input("Digite o seu palpite: ").upper()
        if palpite == palavra_certa:
            print("Parabéns,você acertou!")
            print(f"{n} fez {self.__pontos} pontos ")
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

            elif self.__cont == 4:
                print(dicas[4])
                self.__cont += 1
                self.__pontos -= 5

            elif self.__cont == 5:
                print(dicas[4])
                if dicas != palavra_certa:
                    print("Você perdeu!!")
                    self.__pontos -= 5
                    print(f"{n} fez {self.__pontos} pontos")
                    exit()

    def add_jogador(self, pontos):
        n = pd.read_excel("teste.xlsx")
        n.loc[len(n)] = [self.__nome, self.__pontos]
        n.to_excel("teste.xlsx", index=False)

    def cria_planilha():
        d = {"Nome": [''], "Pontos": ['']}
        dados = pd.DataFrame(data=d)
        dados.to_excel("teste.xlsx", index=False)

    def ranking():
        planilha = pd.read_excel(teste.xlsx)
        rank = planilha.loc[:,['Nome','Pontos']]
        rank = rank.sort_values(by=['Pontos'],ascending=False, na_position='last',ignore_index=True).head(5))
        print(rank)





abertura1 = input("|---------------------------------------------|\n"
                  "|               SEJA BEM VINDO                |\n"
                  "|                                             |\n"
                  "|    O TEMA DO JOGO É PERSONAGENS DA DISNEY   |\n"
                  "|                                             |\n"
                  "|       PRESSIONE ENTER PARA CONTINUAR        |\n"
                  "|                                             |\n"
                  "|---------------------------------------------|\n")

n = input("\t\t Digite o seu nome: ").upper()



jogo = Jogo()
lista = jogo.lista()




abertura2 =print("|--------------------------------------------|\n"
                f"|               OLÁ {n}                     |\n"
                 "|                                            |\n"
                 "|          VAMOS COMEÇAR O JOGO!             |\n" 
                 "|--------------------------------------------|\n")
personagem_escolhido = random.choice(lista)
while True:

    jogo.palpite(personagem_escolhido[0], personagem_escolhido[1:6])
import pandas as pd
import random


class Jogo:

    def __init__(self):
        self.__cont = 0
        self.__pontos = 25
        self.__nome = n

    @property
    def pontos(self):
        return self.__pontos


    def lista(self):
        lista_de_dicas = [['BUZZ LIGHTYEAR', 'Um brinquedo do Wandy', 'Tem um laser no pulso', 'Melhor amigo do Woody', 'Patrulheiro espacial', '"Ao infinito e além"'],
                          ['ARIEL', 'Vive no mar', 'Filha do rei Tritão', 'Melhor amiga de um peixe', 'Ruiva', 'Sereia'],
                          ['PETER PAN', 'Menino de espirito livre e travesso','Aventureiro e ousado', 'É melhor amigo de uma fada', 'Nunca cresce', 'Terra do nunca...'],
                          ['OLAF', 'Gosta de abraços quentinhos', 'Nariz de cenoura', 'Foi criado por uma princesa','Usa galhos como braço', 'Boneco de neve'],
                          ['CINDERELA','Menina órfã', 'Loira', 'Madrasta má', 'Sapatinho de cristal', 'Fada madrinha']]

        return lista_de_dicas

    def palpite(self,palavra_certa,dicas):
        if self.__cont == 0:
            self.__cont += 1
            print(f"A primeira dica é: {dicas[0]}")

        palpite = input("Digite o seu palpite: ").upper()
        if palpite == palavra_certa:
            print("Parabéns,você acertou!")
            print(f"{n} fez {self.__pontos} pontos ")
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

            elif self.__cont == 4:
                print(dicas[4])
                self.__cont += 1
                self.__pontos -= 5

            elif self.__cont == 5:
                print(dicas[4])
                if dicas != palavra_certa:
                    print("Você perdeu!!")
                    self.__pontos -= 5
                    print(f"{n} fez {self.__pontos} pontos")
                    exit()

    def add_jogador(self, pontos):
        n = pd.read_excel("teste.xlsx")
        n.loc[len(n)] = [self.__nome, self.__pontos]
        n.to_excel("teste.xlsx", index=False)

    def cria_planilha():
        d = {"Nome": [''], "Pontos": ['']}
        dados = pd.DataFrame(data=d)
        dados.to_excel("teste.xlsx", index=False)

    def ranking():
        planilha = pd.read_excel(teste.xlsx)
        rank = planilha.loc[:,['Nome','Pontos']]
        rank = rank.sort_values(by=['Pontos'],ascending=False, na_position='last',ignore_index=True).head(5))
        print(rank)





abertura1 = input("|---------------------------------------------|\n"
                  "|               SEJA BEM VINDO                |\n"
                  "|                                             |\n"
                  "|    O TEMA DO JOGO É PERSONAGENS DA DISNEY   |\n"
                  "|                                             |\n"
                  "|       PRESSIONE ENTER PARA CONTINUAR        |\n"
                  "|                                             |\n"
                  "|---------------------------------------------|\n")

n = input("\t\t Digite o seu nome: ").upper()



jogo = Jogo()
lista = jogo.lista()




abertura2 =print("|--------------------------------------------|\n"
                f"|               OLÁ {n}                     |\n"
                 "|                                            |\n"
                 "|          VAMOS COMEÇAR O JOGO!             |\n" 
                 "|--------------------------------------------|\n")
personagem_escolhido = random.choice(lista)
while True:

    jogo.palpite(personagem_escolhido[0], personagem_escolhido[1:6])

