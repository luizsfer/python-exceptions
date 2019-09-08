"""ByteBank - Tratamento de excessões com Python."""
import logging


class ContaCorrente:
    """Criação de um objeto do tipo ContaCorrente."""

    _totalDeContasCriadas = 0
    _taxaDeOperacao = 0
    _saldo = 100
    _cliente = ''

    def sacar(self, valor):
        """Função que realiza saques em Conta Corrente."""
        if (self.saldo < valor):
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
        ContaCorrente._taxaDeOperacao = (
            30 / ContaCorrente._totalDeContasCriadas
            )
        ContaCorrente._totalDeContasCriadas += 1


def dividir(numero, divisor):
    """Função que realiza a divisão de dois números."""
    conta = ContaCorrente(None)
    print(conta._saldo)
    return numero / divisor


def testaDivisao(divisor):
    """Função que executa a outra função chamada dividir."""
    return dividir(10, divisor)


def metodo():
    """Função que chama a função testaDivisao."""
    try:
        testaDivisao(0)
    except TypeError as e:
        logging.exception(e)
