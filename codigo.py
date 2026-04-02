import pyautogui
import time
import pandas

# Dá uma pequena pausa entre cada comando
pyautogui.PAUSE = 0.5

# Link do sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

# Abrir o site
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# Login
pyautogui.click(x=662, y=463)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab")
pyautogui.write("senha")

pyautogui.press("tab")
pyautogui.press("enter")

# Espera o sistema carregar
time.sleep(5)

pyautogui.click(x=1169, y=449) 
pyautogui.press("enter")

# Ler a tabela de produtos
tabela = pandas.read_csv("produtos.csv")

# Cadastro dos produtos
for linha in tabela.index:

    # Garante que está no começo do formulário
    pyautogui.scroll(5000)
    time.sleep(1)

    pyautogui.click(x=650, y=331)
    time.sleep(0.5)

    # Código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Observação
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # Vai para o botão de cadastrar
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Espera o cadastro   
    