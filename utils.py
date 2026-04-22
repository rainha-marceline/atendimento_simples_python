# utils.py
from datetime import datetime

def gerar_relatorio(lista_atendimentos):
    """
    Processa uma lista de objetos Atendimento e gera um relatório formatado.
    
    Args:
        lista_atendimentos (list): Uma lista contendo objetos da classe Atendimento.
        
    Returns:
        str: Texto formatado com data, detalhes por cliente e faturamento total.
        None: Se a lista estiver vazia.
    """
    if not lista_atendimentos:
        return None
    
    # Calcula a soma de todos os valores na lista de objetos
    faturamento = sum(c.valor for c in lista_atendimentos)
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Cria as linhas de detalhamento usando list comprehension
    detalhes = "".join([f"- {c.nome}: R$ {c.valor:.2f} ({c.pagamento})\n" for c in lista_atendimentos])
    
    return f"Data: {data_atual}\n{detalhes}Total: R$ {faturamento:.2f}\n{'-'*30}\n"

def salvar_no_arquivo(conteudo, nome_arquivo="vendas.txt"):
    """
    Salva uma string em um arquivo de texto no modo 'append' (anexar).
    
    Args:
        conteudo (str): O texto que será gravado no arquivo.
        nome_arquivo (str): Nome do arquivo de destino. Padrão: 'vendas.txt'.
    """
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        f.write(conteudo)