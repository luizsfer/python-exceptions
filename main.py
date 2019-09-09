"""ByteBank - Tratamento de excessões com Python."""
"""from ContaCorrente import ContaCorrente
from SaldoInsuficienteException import SaldoInsuficienteException"""


if __name__ == '__main__':
    """
    Usando método with para tratamento de arquivo. Esse método irá garantir o
    fechamento do arquivo mesmo de forma implicita, ele executa as funções
    __enter__ e __exit__
    """
    try:
        with open("contas.txt", "w") as f:
            print(f.read())
    except IOError as e:
        print("Erro ao executar a manipulação de arquivo. Detalhe: ", e)
    except Exception as e:
        print("Ocorreu um erro ao executar. Detalhe: ", e)

    """
    Manipulação de arquivo com tratamento de exceção deixando o usuário
    cuidar do fechamento do arquivo.
    """
    """
    try:
        f = open("contas.txt", "w")
        print(f.read())
    except IOError as e:
        print("Erro ao executar a manipulação de arquivo. Detalhe: ", e)
    except Exception as e:
        print("Ocorreu um erro ao executar. Detalhe: ", e)
    finally:
        f.close()
    """
    """
    Execução de testes das funções e excessões no programa ByteBank.
    """
    """
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
    """
