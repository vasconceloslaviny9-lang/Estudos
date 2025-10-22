import pyautogui
import time

time.sleep(2)

for _ in range(5):
    pyautogui.scroll(-300)
    time.sleep(0.6)

time.sleep(1)

for _ in range(5):
    pyautogui.scroll(300)
    time.sleep(0.6)