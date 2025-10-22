import pyautogui
import time

pyautogui.sleep(1)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(969, 205, duration=3)
pyautogui.write("Musicas relaxantes")
pyautogui.press("enter")