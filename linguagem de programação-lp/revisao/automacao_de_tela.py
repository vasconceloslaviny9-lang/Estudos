import pyautogui
pyautogui.moveTo(600,500, duration = 2)

#Clicar
pyautogui.click()

#Digitar
pyautogui.write("Olá mundo!", interval=0.1)

#Pressionar tela
pyautogui.press("enter")

#Exemplo de automação
import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("notepad")
pyautogui.press("enter")


time.sleep(1)
pyautogui.write("Olá, este texto foi digitados automaticamente!", interval=0.07)