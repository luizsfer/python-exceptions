"""ByteBank - Tratamento de excessões com Python."""
from ContaCorrente import ContaCorrente


if __name__ == '__main__':
    try:
        conta = ContaCorrente(456, 0)
    except ValueError as ex:
        mensagem, nome = ex.args
        print("Argumento com problema: " + nome)
        print("Ocorreu uma excessão do tipo ValueError")
        print(mensagem)
    except Exception as ex:
        print(ex.message)
