import pyautogui
import time

pyautogui.sleep(1)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("wikipedia")
pyautogui.press("enter")
pyautogui.click(1053, 353, duration=2)