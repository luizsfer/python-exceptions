"""ByteBank - Tratamento de excessões com Python."""


class SaldoInsuficienteException (Exception):
    """Classe de funções de tratamento de excessões."""

    def __init__(self, saldo, valorSaque):
        """Função que inicia a classe Exception."""
        self.saldo = saldo
        self.valorSaque = valorSaque

    def __str__(self):
        """Função que retorna a mensagem desejada por padrão."""
        return (
            "Tentativa de saque do valor de "
            + self.valorSaque
            + " em uma conta com saldo de "
            + self.saldo)
