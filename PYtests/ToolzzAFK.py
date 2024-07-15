import time
import pyautogui
from datetime import datetime
from time import sleep
import pyperclip
"""
pyautogui.moveTo(x=-870, y=509)
pyautogui.click()
while True:
    for i in range(9):
        pyautogui.press('right')
        sleep(20)
    for i in range(9):
        pyautogui.press('left')
        sleep(20)
"""
"""
tm = datetime.now()
checkFix = datetime(2024,7,15, 8,4,0)
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
"""
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

while True:
    pyautogui.tripleClick(x=-607, y=61)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    text = pyperclip.paste()
    if 'play/player/' in text:
        pyautogui.moveTo(x=-364, y=400)
        pyautogui.click()
        for i in range(12):
            pyautogui.tripleClick(x=-607, y=61)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            text = pyperclip.paste()
            if 'play/player/' in text:
                pyautogui.moveTo(x=-364, y=400)
                pyautogui.click()
            pyautogui.press('right')
            sleep(5)
        for i in range(12):
            pyautogui.tripleClick(x=-607, y=61)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            text = pyperclip.paste()
            if 'play/player/' in text:
                pyautogui.moveTo(x=-364, y=400)
                pyautogui.click()
            pyautogui.press('left')
            sleep(5)
    elif 'https://cieeaprendiz.app.toolzz.com.br/' in text:
        pyautogui.moveTo(x=-72, y=163)
        pyautogui.click()
        pyautogui.moveTo(x=-193, y=259)
        pyautogui.click()
        sleep(1)
        pyautogui.typewrite('52855137829')
        pyautogui.moveTo(x=-224, y=344)
        pyautogui.click()
        sleep(2)
        pyautogui.typewrite('21120')
        pyautogui.moveTo(x=-181, y=419)
        sleep(1)
        pyautogui.click()
        sleep(10)
        pyautogui.moveTo(x=-806, y=738)
        pyautogui.click()
        sleep(3)
        pyautogui.moveTo(x=-1873, y=435)
        pyautogui.click()
        sleep(2)
        pyautogui.moveTo(x=-364, y=400)
        pyautogui.click()
        sleep(1)
