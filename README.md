# Zoomautojoiner  
1. Checks if start time and system time matches
2. Opens meeting link when they match
3. Keeps checking if end time and system time matches
4. Exits the meeting using zoom hotkey and pynput when they match 
5. In for loop to move to the next meeting details and repeat the entire process
Make sure to mark "Ask me to confrim when I leave a meeting" in zoom general settings is marked OFF  
Make sure in audio settings to check "automatically join audio by computer audio when joining a meeting" and "mute my microphone when joining a meeting" 
Also make sure to change the keyboard shorcut of "end meeting" to " * " or change the code to any keybind of your chosing. 
And always allow zoom to open links of this type in associated app, when it asks the first time (most people already have this on)

To install pynput, (in pycharm) click on file, settings, python interpreter, the plus button on the right, and search for "pynput" and install the package.  
