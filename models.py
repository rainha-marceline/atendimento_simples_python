# models.py

class Atendimento:
    """
    Representa um atendimento individual realizado no estabelecimento.
    
    Atributos:
        nome (str): Nome da cliente.
        valor (float): Preço cobrado pelo serviço.
        pagamento (str): Método utilizado (ex: Cartão, Dinheiro).
        status (str): Situação do pagamento (ex: Pago, Pendente).
    """
    def __init__(self, nome, valor, pagamento, status):
        self.nome = nome
        self.valor = valor
        self.pagamento = pagamento
        self.status = status