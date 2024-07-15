from datetime import datetime
import pyautogui
from time import sleep

tm = datetime.now()
checkFix = datetime(2024,7,15, 0,46,0)
remaining = checkFix - tm
base_datetime = datetime(1,1,1)
remTime = base_datetime + remaining
actual = tm.hour

h = remTime.hour
m = remTime.minute
s = remTime.second
if h < 1:
     h = h * -1
if m < 1:
    m = m * -1
if s < 1:
    s = s * -1
print(f'hours: {h}')
print(f'minutes: {m}')
print(f'seconds: {s}')
sleep(h*3600)
sleep(m*60)
sleep(s)

pyautogui.moveTo(x=-1707, y=1060)
pyautogui.rightClick()
sleep(3)
pyautogui.moveTo(x=-1694, y=954)
sleep(1)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=-691, y=106)
sleep(1)
pyautogui.click()
sleep(2)

