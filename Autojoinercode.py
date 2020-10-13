import time
from datetime import datetime
from pynput.keyboard import Controller
from data import lst
import webbrowser

isStarted = False
keyboard = Controller()
classperiod = int(input("Enter school period to start at: "))
classperiod -= 1

for i in lst:
    while True:
        if not isStarted:
            if datetime.now() == (lst[classperiod][1]):
                webbrowser.open(lst[classperiod][0])
                isStarted = True
        elif isStarted:
            if datetime.now() == (lst[classperiod][2]):
                keyboard.press('-')
                # put in keybind for "end meeting"
                time.sleep(1)
                isStarted = False
                classperiod += 1
                break
