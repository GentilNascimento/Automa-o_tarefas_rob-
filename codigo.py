# Passo a passo do projeto

# 1. Abrir o sistema da empresa.
#   https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pip install pyautogui

import pandas as pd
import pyautogui
import time

# isso determina meio segundo pra cada comando
pyautogui.PAUSE = 1


# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressiona uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas(ctrl c, ctrl v, alt tab)

# abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site,
# então pedimos pra aguardar 3 segs antes do próx. comando.
#
time.sleep(3)

# 2. Fazendo login, definindo a posição do mouse
pyautogui.click(x=881, y=411)
pyautogui.write("seu_e_mail")

pyautogui.press("tab")  # passou pro campo de senha
pyautogui.write("sua senha aqui")

pyautogui.press("tab")  # passou pro botão login
pyautogui.press("enter")

# 3. Abrir/Importar a base de dados de produtos para cadastrar.
# pip install pandas numpyxl

tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar um produto.

for linha in tabela.index:
    # 'str' pro python ler tanto texto/núm
    codigo = str(tabela.loc[linha, "codigo"])

    # clicar no campo do código do produto
    pyautogui.click(x=759, y=293)

    pyautogui.write(codigo)
    # passar próx campo
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passa próx campo
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passa próx campo
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passa próx campo
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passa próx campo
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passa próx campo
    pyautogui.press("tab")

    # obs.
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # passa próx campo
    pyautogui.press("tab")
 
    # apertar o botão
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# 5. Repetir isso tudo até acabar a lista de produtos.sua senha aqui
