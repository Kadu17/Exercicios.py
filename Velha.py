
class jogodavelha:
    def __init__(self):
        self.tabuleiro = {'7': ' ', '8': ' ', '9': ' ',
                          '4': ' ', '5': ' ', '6': ' ',
                          '1': ' ', '2': ' ', '3': ' '}


    def exibirTabuleiro(self):
            print("┌───┬───┬───┐")
            print(f"| {self.tabuleiro['7']} | {self.tabuleiro['8']} | {self.tabuleiro['9']} |")
            print("├───┼───┼───┤")
            print(f"| {self.tabuleiro['4']} | {self.tabuleiro['5']} | {self.tabuleiro['6']} |")
            print("├───┼───┼───┤")
            print(f"| {self.tabuleiro['1']} | {self.tabuleiro['2']} | {self.tabuleiro['3']} |")
            print("└───┴───┴───┘")


    def verificarJogada(self, jogada):
            entrada1 = input("Digite onde vôce gostaria de jogar: ")
            if jogada in self.tabuleiro.keys():
                 return entrada1
            self.tabuleiro[entrada1] = 'x'
            entrada2 = input("Digite onde vôce gostaria de jogar: ")
            self.tabuleiro[entrada2] = 'o'


    def verificarTabuleiro(self):

            if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
                return self.tabuleiro['7']
            elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
                return self.tabuleiro['8']
            elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
                return self.tabuleiro['9']


            if self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
                return self.tabuleiro['7']
            elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
                return self.tabuleiro['8']
            elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
                return self.tabuleiro['1']


            if self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
                return self.tabuleiro['7']
            elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
                return self.tabuleiro['1']

            if [*self.tabuleiro.values()].count(' ') == 0:
                return "empate"
            else:
                return None
        

jogo = jogodavelha()
while True:
    jogada = jogo.exibirTabuleiro()
    jogador_vencedor = jogo.verificarTabuleiro()
    jogo.verificarJogada(jogada)
    if jogador_vencedor == 'x':
        print("Jogador X venceu!!")
    else:
        print("Jogador O vanceu!!")
