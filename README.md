# Power Up - Automação de Tarefas com Python

O **Power Up** é um projeto em Python desenvolvido para automatizar tarefas repetitivas, tornando processos mais rápidos e eficientes. Ele simula a leitura de uma base de dados e o cadastro automático de produtos.

---

## Funcionalidades

- **Leitura de Base de Dados:** O sistema lê informações de uma base de dados (CSV, Excel ou SQLite) para identificar produtos e dados necessários.
- **Cadastro Automático de Produtos:** Com base nos dados lidos, o programa cadastra produtos automaticamente.
- **Automação de Processos Repetitivos:** Qualquer tarefa repetitiva pode ser adaptada e automatizada pelo código.

---

## Tecnologias Utilizadas

- **Python** – Linguagem principal do projeto.
- **Pandas** – Para manipulação e leitura da base de dados.
- **SQLite / CSV** – Exemplos de formatos de base de dados utilizados.

---

## Como Funciona

1. O usuário fornece uma base de dados com informações dos produtos.
2. O script em Python lê os dados e processa as informações.
3. Os produtos são cadastrados automaticamente conforme o exemplo no código.

---

## Exemplo de Código

```python
import pandas as pd

# Leitura da base de dados
produtos = pd.read_csv("produtos.csv")

# Cadastro automático
for index, produto in produtos.iterrows():
    print(f"Cadastrando produto: {produto['nome']} - R${produto['preco']}")
