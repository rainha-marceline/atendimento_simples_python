# main.py
"""
Script Principal do Sistema de Caixa.
Responsável pela interação com o usuário, coleta de dados e execução do fluxo.
"""
from models import Atendimento
from utils import gerar_relatorio, salvar_no_arquivo

# Lista global para armazenar os atendimentos da sessão atual
historico = []

print("--- SISTEMA DE CAIXA INICIADO ---")

while True:
    nome = str(input("\nNome (ou 'sair' para encerrar): "))
    if nome.lower() == "sair": 
        break
    
    try:
        # Validação de entrada: garante que o valor seja o especificado.
        valor = float(input("Valor: R$ "))
        pagamento = str(input("Pagamento (Cartão/Dinheiro): "))
        status = str(input("Status (Pago/Pendente): "))
        
        # Instanciação do objeto Atendimento
        cliente = Atendimento(nome, valor, pagamento, status)
        historico.append(cliente)
        
    except ValueError:
        print("❌ Erro: Valor inválido. O sistema aceita apenas números (use ponto para decimais).")

# Geração e salvamento do relatório final
relatorio = gerar_relatorio(historico)

if relatorio:
    salvar_no_arquivo(relatorio)
    print("\n✅ Relatório gerado e salvo com sucesso no arquivo 'vendas.txt'!")
    print(relatorio)
else:
    print("\nNenhum atendimento registrado nesta sessão.")
