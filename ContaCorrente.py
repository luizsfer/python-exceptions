"""ByteBank - Tratamento de excessões com Python."""
import logging
from SaldoInsuficienteException import SaldoInsuficienteException


class ContaCorrente:
    """Criação de um objeto do tipo ContaCorrente."""

    _totalDeContasCriadas = 0
    _taxaDeOperacao = 0
    _saldo = 100
    _cliente = ''

    def sacar(self, valor):
        """Função que realiza saques em Conta Corrente."""
        if valor < 0:
            raise ValueError("Valor inválido para o saque.", "valor")

        if self._saldo < valor:
            raise SaldoInsuficienteException(self._saldo, valor)

        self._saldo -= valor

    def depositar(self, valor):
        """Função que realiza depósitos em Conta Corrente."""
        self._saldo += valor

    def transferir(self, valor, contaDestino):
        """Função que realiza transferências em Contas Correntes."""
        if valor <= 0:
            raise ValueError("Valor inválido para a transferência.", "valor")
        self._saldo -= valor
        contaDestino.depositar(valor)

    def __init__(self, numero, agencia):
        """Inicializador do objeto."""
        if numero <= 0:
            raise ValueError(
                "O argumento numero deve ser maior que 0.", "numero")
        elif agencia <= 0:
            raise ValueError(
                "O argumento agencia deve ser maior que 0.", "agencia")

        self.numero = numero
        self.agencia = agencia
        ContaCorrente._totalDeContasCriadas += 1
        ContaCorrente._taxaDeOperacao = (
            30 / ContaCorrente._totalDeContasCriadas
            )


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
