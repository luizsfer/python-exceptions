"""ByteBank - Tratamento de excessões com Python."""
import logging
import ContaCorrente
import Clientes

if __name__ == '__main__':
    try:
        ContaCorrente.metodo()
    except ZeroDivisionError as e:
        logging.exception(e)
