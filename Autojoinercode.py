import time
from datetime import datetime
from pynput.keyboard import Controller
from data import lst
import webbrowser

isStarted = False
keyboard = Controller()
classperiod = int(input("Enter school period to start at: ")) 
# comment out the operation below if you have a zero period
classperiod -= 1

for i in lst:
    while True:
        if not isStarted:
            if datetime.now().hour == int(lst[classperiod][1].split(':')[0]) and datetime.now().minute == \
                    int(lst[classperiod][1].split(':')[1]):
                webbrowser.open(lst[classperiod][0])
                isStarted = True
        elif isStarted:
            if datetime.now().hour == int(lst[classperiod][2].split(':')[0]) and datetime.now().minute == \
                    int(lst[classperiod][2].split(':')[1]):
                keyboard.press('-')
                # put in keybind for "end meeting"
                time.sleep(1)
                isStarted = False
                if classperiod - 1 < 6:
                    classperiod += 1
                else:
                    classperiod = 0
                break
