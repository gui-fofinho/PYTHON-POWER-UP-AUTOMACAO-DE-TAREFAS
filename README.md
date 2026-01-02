# 🤖 Automação de Cadastro de Produtos com Python

Este projeto realiza a **automação do cadastro de produtos** em um sistema web utilizando **Python**, **PyAutoGUI** e **Pandas**.

A automação lê uma base de dados em CSV e preenche automaticamente os campos do sistema, simulando interações humanas com teclado e mouse.

---

## 🚀 Funcionalidades

- Abertura automática do navegador
- Login automático no sistema
- Leitura de produtos a partir de um arquivo CSV
- Cadastro automático de múltiplos produtos
- Automação completa de tarefas repetitivas

---


## 🛠️ Tecnologias
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web-ff0000?style=flat-square&logo=streamlit)
![OpenAI](https://img.shields.io/badge/OpenAI_API-GPT-412991?style=flat-square&logo=openai)
---

## 📦 Estrutura do projeto

```text
📦 automacao-cadastro-produtos
 
 ┃ 📄 produtos.csv - (arquivo contendo a base de dados de produtos)
 ┃ 📄 pegar_posicao.py - (script auxiliar para determinar posições utilizadas pelo programa principal)
 ┣ 📄 automacao_cadastro.py - (arquivo principal)
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
 ```
 
▶️ Como executar o projeto

1️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

2️⃣ Configurar login

No arquivo automacao_cadastro.py, altere:
```bash
EMAIL = "SEU_EMAIL_AQUI"
SENHA = "SUA_SENHA_AQUI"
```

3️⃣ Executar a automação
```bash
python automacao_cadastro.py
```

⚠️ Importante:

Não utilize o computador durante a execução

As coordenadas da tela podem variar de acordo com a resolução

---

## 📚 Observações
Projeto com fins educacionais

Ideal para demonstrar:

   automação de processos;
   
   manipulação de arquivos CSV;
   
   uso de bibliotecas externas;

Pode ser adaptado para outros sistemas e formulários

---

## 👨‍💻 Autor

Projeto desenvolvido por **Guilherme Matté**,  
como parte dos estudos no curso da **Hashtag Treinamentos**, com foco em automação de processos utilizando Python.
