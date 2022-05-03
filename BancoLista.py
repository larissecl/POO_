class BancoLista:

    def __init__(self):
        self.contas = []

    def cadastrar(self, conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        achou = False

        for elemento in self.contas:
            if elemento.get_numero() == numero:
                achou = True
                return elemento

        if achou is False:
            return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta Inexistente!")

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente!")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta Inexistente!")

    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)

        if conta_origem and conta_destino:

            if self.saldo(origem) >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
            else:
                print("Saldo Inexistente!")
        else:
            print("Conta Inexistente!")