class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome

    @property #Faz uma validação
    def nome(self):
        return self.__nome.upper()

    @nome.setter
    def nome(self, nome):
        print("CHAMANDO SETTER NOME...")


cliente = Cliente("angelo")
print(cliente.nome)
cliente.nome = "Fulano"
print(cliente.nome)