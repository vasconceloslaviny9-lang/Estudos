import pyautogui
import time

pyautogui.PAUSE=0.6

pyautogui.press("win")
pyautogui.write("bloco de notas")
pyautogui.press("enter")
pyautogui.write("Automatizando com PyAutoGUI e divertido!", interval=0.2)