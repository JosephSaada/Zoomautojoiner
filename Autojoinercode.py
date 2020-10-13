import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst
import webbrowser

isStarted = False
keyboard = Controller()

i = input("Enter school period to start at: ")
print(i)
for i in lst:
    while True:
        if not isStarted:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                keyboard.press('*')   
# put in keybind for "end meeting"
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted = False 
                i += 1
                break
