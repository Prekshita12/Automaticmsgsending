import pyautogui as pg 
import time
print("program will rn for 5 min")
print("messgae will be printed 10 times")
time.sleep(5)

for i in range(10):
    pg.write("hello  world")
    time.sleep(0.5)
    pg.press("Enter")