"""ByteBank - Tratamento de excessões com Python."""
from ContaCorrente import ContaCorrente
from SaldoInsuficienteException import SaldoInsuficienteException


if __name__ == '__main__':
    try:
        print("Iniciando aplicação")
        conta = ContaCorrente(456, 4578420)
        conta2 = ContaCorrente(485, 456478)

        conta2.transferir(-10, conta)
        conta.depositar(50)
        print(conta._saldo)
        conta.sacar(-500)

    except ValueError as ex:
        mensagem, nome = ex.args
        print("Argumento com problema: " + nome)
        print("Ocorreu uma excessão do tipo ValueError")
        print(mensagem)
    except SaldoInsuficienteException as ex:
        print(ex)
        print("Exceção do tipo SaldoInsuficienteException")
