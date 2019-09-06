"""ByteBank - Tratamento de excessões com Python."""
import Clientes


class ContaCorrente(Clientes):
    """Criação de um objeto do tipo ContaCorrente."""

    _totalDeContasCriadas = 0
    saldo = 100

    def sacar(self, valor):
        """Função que realiza saques em Conta Corrente."""
        if (valor < self.saldo):
            return False
        else:
            self.saldo -= valor
            return True

    def depositar(self, valor):
        """Função que realiza depósitos em Conta Corrente."""
        self.saldo += valor

    def transferir(self, valor, contaDestino):
        """Função que realiza transferências em Contas Correntes."""
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            contaDestino.depositar(valor)
            return True

    def __init__(self, numero, agencia):
        """Inicializador do objeto."""
        self.numero = numero
        self.agencia = agencia
        ContaCorrente._totalDeContasCriadas += 1
