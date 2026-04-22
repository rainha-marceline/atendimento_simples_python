import math
import random as rd
from datetime import datetime

class Atendimento:
    def __init__(self, nome, valor, pagamento, status):
        self.nome = nome
        self.valor = valor
        self.pagamento = pagamento
        self.status = status

historico = []

while True:
    nome = input("\nNome (ou 'sair'): ")
    if nome.lower() == "sair": break
    
    try:
        valor = float(input("Valor: R$ "))
        pagamento = input("Pagamento (Cartão/Dinheiro): ")
        status = input("Status (Pago/Pendente): ")
        
        # Criando o objeto e salvando na lista
        cliente = Atendimento(nome, valor, pagamento, status)
        historico.append(cliente)
        
    except ValueError:
        print("❌ Erro: Valor inválido. Tente novamente.")

# Relatório usando os objetos da classe
if historico:
    faturamento = sum(c.valor for c in historico)
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    detalhes = "".join([f"- {c.nome}: R$ {c.valor:.2f} ({c.pagamento})\n" for c in historico])
    
    relatorio = f"Data: {data_atual}\n{detalhes}Total: R$ {faturamento:.2f}\n{'-'*30}\n"
    
    with open("vendas.txt", "a", encoding="utf-8") as f:
        f.write(relatorio)
    
    print("\n✅ Relatório atualizado no histórico!")