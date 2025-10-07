import pyautogui
import time
pyautogui.PAUSE=0.3

#possição do mouse
#print(pyautogui.position())

#while(True): #loop infinito



time.sleep(1)
pyautogui.moveTo(1761,155, duration=2)#movimentar o mouse para aquela coordenada

time.sleep(1)
pyautogui.click(1761, 155 ,duration=2)
    
time.sleep(2)
pyautogui.click(1603, 239, duration=2)

time.sleep(2)
pyautogui.write("25160720@2025")

time.sleep(2)
pyautogui.click(1833, 422)
