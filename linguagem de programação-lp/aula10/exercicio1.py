import pyautogui
import time

pyautogui.PAUSE=0.6

#print(pyautogui.KEYBOARD_KEYS)
pyautogui.sleep(1)
pyautogui.press("win")
pyautogui.write("bloco de notas")
pyautogui.press("enter")
pyautogui.sleep(1)
pyautogui.write("Laviny")
pyautogui.hotkey("Ctrl", "b")
