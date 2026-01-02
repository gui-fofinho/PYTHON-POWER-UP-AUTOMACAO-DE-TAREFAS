import time
import pyautogui
import pandas as pd

# pausa padrão entre os comandos
pyautogui.PAUSE = 0.3


# CONFIGURAÇÕES

URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "SEU_EMAIL_AQUI"
SENHA = "SUA_SENHA_AQUI"


# ABRIR NAVEGADOR

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# clicar na barra de endereços
pyautogui.click(x=432, y=66)
pyautogui.write(URL)
pyautogui.press("enter")
time.sleep(3)


# LOGIN NO SISTEMA

pyautogui.click(x=701, y=405)
pyautogui.write(EMAIL)
pyautogui.press("tab")
pyautogui.write(SENHA)
pyautogui.click(x=951, y=568)
time.sleep(3)


# LER BASE DE PRODUTOS

tabela = pd.read_csv("data/produtos.csv")


# CADASTRAR PRODUTOS

for linha in tabela.index:
    pyautogui.click(x=653, y=294)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
