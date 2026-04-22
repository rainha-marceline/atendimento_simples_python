# Sistema de Gerenciamento de Atendimentos

Este projeto é uma ferramenta simples e eficiente desenvolvida em **Python** para organizar o fluxo de vendas e prestação de serviços. Ele permite registrar atendimentos individuais, calcular o faturamento e gerar relatórios automáticos salvos em arquivos de texto.

O sistema é ideal para profissionais que precisam de um controle rápido de caixa, como em clínicas de saúde ou atendimentos de estética.

## 🚀 Funcionalidades

* **Cadastro de Atendimentos**: Registro de nome da cliente, valor do serviço, forma de pagamento e status.
* **Cálculo Automático**: Soma total do faturamento da sessão.
* **Relatório Detalhado**: Geração de um resumo com data, hora e lista de todos os serviços realizados.
* **Armazenamento**: Salvamento automático dos dados em um arquivo `vendas.txt` para consulta futura.

## 📁 Estrutura do Projeto

O código está dividido em três arquivos para manter a organização e facilitar a manutenção:

1.  **`models.py`**: Contém a classe `Atendimento`, que define a estrutura de dados (nome, valor, etc.).
2.  **`utils.py`**: Reúne as funções lógicas para gerar o relatório de texto e realizar a gravação no arquivo.
3.  **`main.py`**: É o ponto de entrada do sistema, responsável por interagir com o usuário e coordenar o fluxo do programa.

## 🛠️ Como Executar

Como o sistema utiliza apenas bibliotecas padrão do Python, não é necessário instalar dependências externas.

1.  Certifique-se de ter o Python instalado em seu computador ou dispositivo Android.
2.  Baixe os arquivos `main.py`, `models.py` e `utils.py` para a mesma pasta.
3.  Abra o terminal ou console e execute o comando:
    ```bash
    python main.py
    ```
4.  Siga as instruções na tela para inserir os dados. Digite **"sair"** no campo de nome para finalizar e gerar o relatório final.

## 📝 Exemplo de Relatório Gerado

Ao finalizar uma sessão, o sistema gera uma saída formatada como esta:

```text
Data: 22/04/2026 14:30
- Cliente A: R$ 50.00 (Dinheiro)
- Cliente B: R$ 85.00 (Cartão)
Total: R$ 135.00
------------------------------
```

---
**Desenvolvido para estudos de Lógica de Programação e Desenvolvimento Backend.**