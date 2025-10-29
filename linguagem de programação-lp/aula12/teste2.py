import pyautogui
import time

time.sleep(5)
im1 = pyautogui.screenshot(region=(381,85,316,528))
im1.save('imagem2.png')