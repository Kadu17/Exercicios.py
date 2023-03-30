class Conta():

    def __init__(self, numero: int, titular: str, saldo: 1000, limite: float):

        """
        Construção de um objeto do Tipo Conta
        :param self: Conta
        :param numero: int
        :param titular: str
        :param saldo: float
        :param limite: float
        """

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Titular: ", self.__titular, "Saldo: ", self.__saldo)

    def sacar(self, valor: float):
        self.__saldo -= valor

    def depositar(self, valor: float):
        self.__saldo += valor

    def transferir(self, conta_destino: str, valor: float):

        """
        :param self: Conta
        :param conta_destino: str
        :param valor: float
        """

        self.sacar(valor)
        conta_destino.depositar(valor)

    def __verificar_saque(self, valor: float):
        if valor > self.__limite + self.__saldo:
            return False
        return True

    def sacar(self, valor: float):
        if self.__verificar_saque(valor):
            self.__saldo -= valor
        else:
            print("VALOR ACIMA DO PERMITIDO")

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor > 1.1 * self.__limite:
            print("INFELIZMENTE O LIMITE ESTÁ ACIMA DE 10%")
            print("LIMITE NÃO ALTERADO: ", self.__limite)

        else:
            self.__limite = valor
            print("LIMITE ALTERADO CO SUCESSO")
            print("NOVO VALOR: ", self.limite)


if __name__ == "__main__":
    conta1 = Conta(1, "Fulano", 1000, 0)
    conta2 = Conta(numero=2, titular="Ângelo", saldo=10, limite=1000)
    dic = conta2.__dict__  # Trasforma o objeto em dicionário

    # print(vars(conta1)) #Trasforma o objeto em dicionário

    # conta1.transferir(conta2, 100)
    # conta1.extrato()

    # print(dic)

    # print(conta1.limite)
    # conta1.limite = 1100

    conta1.sacar(2000)
    conta1.extrato()