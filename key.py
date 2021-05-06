import win32api
import win32con
import time
import sys

def inputKey(key):
    win32api.keybd_event(key,0)
    time.sleep(0.2)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

def defineKey(key):    
    print('a')
    if key == 'left':
        inputKey(37)
                
    if key == 'right':
        inputKey(39)
                
    if key == 'up':
        inputKey(38)
                
    if key == 'down':
        inputKey(40)
                
    if key == 'a':
        inputKey(83)
                
    if key == 'b':
        inputKey(65)
                
    if key == 'start':
        inputKey(13)

    if key == 'select':
        inputKey(32) 

key = sys.argv[1]
defineKey(key)