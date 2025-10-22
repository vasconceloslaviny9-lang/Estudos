import pyautogui
import time

time.sleep(5)

lado = 200
espaco = 20 

for _ in range(3):
    pyautogui.dragRel(lado, 0, duration = 2)
    pyautogui.dragRel(0, lado, duration = 2)
    pyautogui.dragRel(-lado, 0, duration = 2)
    pyautogui.dragRel(0, -lado, duration = 2)
    
    pyautogui.moveRel(lado + espaco, 0,duration=0.5)
