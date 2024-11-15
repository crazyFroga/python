import pyautogui
import time

time.sleep(5); f = open('bemovie.txt','r')
for line in f:
    pyautogui.typewrite (line)
    pyautogui.press ("enter")
