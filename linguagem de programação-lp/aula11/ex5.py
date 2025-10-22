import pyautogui
import time

time.sleep(5)
pyautogui.dragRel(100, 0, duration=0.5)
pyautogui.dragRel(0, 100, duration=0.5)
pyautogui.dragRel(-100, 0, duration=0.5)
pyautogui.dragRel(0, -100, duration=0.5)
