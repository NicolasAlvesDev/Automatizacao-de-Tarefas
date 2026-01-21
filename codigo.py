import pyautogui  # biblioteca para automação do mouse e teclado
import time  # biblioteca para manipulação do mouse e teclado
import pandas as pd  # biblioteca para manipulação de dados

pyautogui.PAUSE = 1  # Pausa de 1 segundo após cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 1 passo - Entrar no sistema da empresa
pyautogui.press("win")
time.sleep(1)
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior para o site carregar
time.sleep(4)

# 2 passo - Fazer login
pyautogui.click(x=573, y=605)  # clicar no campo de email.
pyautogui.write("nicolasalvesdesantana1@gmail.com")  # digitar o email
pyautogui.click(x=551, y=762)  # clicar no campo de senha
pyautogui.write("1234")  # senha
pyautogui.press("tab")  # ir para o botão entrar
pyautogui.press("enter")  # clicar no botão entrar
time.sleep(5)  # esperar o sistema carregar

# 3 passo - Abrir a base de dados
tabela = pd.read_csv("produtos.csv")  # leitura da tabela csv.

# 4 passo - Cadastrar os produtos
for linha in tabela.index:
    pyautogui.click(x=537, y=437)  # clicar na area de codigo do produto.
    codigo = str(tabela.loc[linha, "codigo"])  # pegar o codigo da linha atual
    pyautogui.write(codigo)  # digitar o codigo do produto
    pyautogui.press("tab")  # ir para o proximo campo

    marca = str(tabela.loc[linha, "marca"])  # pegar a marca da linha atual
    pyautogui.write(marca)  # digitar a marca do produto
    pyautogui.press("tab")  # ir para o proximo campo

    tipo = str(tabela.loc[linha, "tipo"])  # pegar o tipo da linha atual
    pyautogui.write(tipo)  # digitar o tipo do produto
    pyautogui.press("tab")  # ir para o proximo campo

    categoria = str(tabela.loc[linha, "categoria"])# pegar a categoria da linha atual
    pyautogui.write(categoria)  # digitar a categoria do produto
    pyautogui.press("tab")  # ir para o proximo campo

    preco = str(tabela.loc[linha, "preco_unitario"])# pegar o preco da linha atual
    pyautogui.write(preco)  # digitar o preco do produto
    pyautogui.press("tab")  # ir para o proximo campo

    custo = str(tabela.loc[linha, "custo"])  # pegar o custo da linha atual
    pyautogui.write(custo)  # digitar o custo do produto
    pyautogui.press("tab")  # ir para o proximo campo

    obs = str(tabela.loc[linha, "obs"])  # pegar a obs da linha atual
    if obs != "nan":
        pyautogui.write(obs)  # digitar a obs do produto
    pyautogui.press("tab")  # vai para o campo de enviar
    pyautogui.press("enter")  # clicou em enviar
    pyautogui.scroll(5000) # subir a tela para o topo