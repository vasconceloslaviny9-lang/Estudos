import pyautogui

pyautogui.alert(text="Inicialndo automação", title="Automação de login", button="ok")
email = pyautogui.prompt(text = " Digite seu email: ", title= "Informação obrigatória")
print(f"Seu email: [email]")
resposta = pyautogui.confirm(text = "Continua nossa automação?", title = "Confirmação", buttons = ["Sim", "Não", "Cancelar"])
print(resposta)