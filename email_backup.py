from pyautogui import *
from time import sleep
import random

def find_and_click_image_center(image_path):
    image_centers = {}
    image_centers[image_path] = locateCenterOnScreen(image_path)
    click(image_centers[image_path].x , image_centers[image_path].y)
    print(image_centers)
    return image_centers

def send_email(commands, image_path):
    for command in commands:
        sleep(random.random() + 1.5)
        press(command)
        sleep(random.random() + 1.5)
    hotkey("ctrl", "shift", "5")
    sleep(random.random() + 1.5)
    hotkey("ctrl", "enter")
    scroll(1000) 
    try:
        click()
        find_and_click_image_center(image_path)
    except:
        press("esc")
        sleep(random.random() + 1.5)
        press("esc")
    sleep(random.random() + 1.5)
click([500, 900]) #depends on the layout of the displays and windows while running
moveTo([300, 2000])
for i in range(10000):
    send_email(commands = ["esc", "esc", "down", "enter"], image_path = 
    	"/home/marcos/Pictures/email_backup_buttons/x.png")


'''
https://pyautogui.readthedocs.io/en/latest/keyboard.html

['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
'''

