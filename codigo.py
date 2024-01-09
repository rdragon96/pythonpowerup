# Passo a passo

#  PASSO 1 - Entraar no sistema da empresa
 
    # # https://dlp.hashtagtreinamentos.com/python/intensivao/login

#instalar e importar pyautogui
import pyautogui
import time
import pandas as pd
import numpy
import openpyxl


pyautogui.PAUSE=1

pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("Enter")
time.sleep(3)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")

time.sleep(5)

#  PASSO 2 - Fazer login
pyautogui.click(x=398, y=378)

pyautogui.write("rafael@gmail.com")
pyautogui.press("tab")
pyautogui.write("R1234@")
pyautogui.press("tab")
pyautogui.press("Enter")

time.sleep(3)



#  PASSO 3 - Importar a base de Dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    #  PASSO 4 - Cadastrar um produto
    pyautogui.click(x=455, y=256)
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
        pyautogui.write(obs)
    pyautogui.write("")
    pyautogui.press("tab")

    pyautogui.press("Enter")
    pyautogui.scroll(5000)

#  Passo 5 - Repetir isso ate acabar a base de dados