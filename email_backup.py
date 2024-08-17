from pyautogui import *

#click_on_pixel([100, 300])
def find_image_centers_email(images_dir, max_attempts = 10):
    image_centers = {}
    print("hi")
    attempt = 0
    successful = False
    while not successful and attempt < max_attempts:
        print("Attempt " + str(attempt))
        for image_file in os.listdir(images_dir):
            path = images_dir + "/" + image_file
            print(path)
        try:
            image_centers[image_file] = locateCenterOnScreen(path)
            successful = True
        except:
            attempt += 1
    print(image_centers)
    #now to change to different output units
    if successful:
        for image_file in os.listdir(images_dir):
            moveTo(image_centers[image_file].x , image_centers[image_file].y)
            click()
            click(image_centers[image_file].x , image_centers[image_file].y)
            print([image_centers[image_file].x, image_centers[image_file].y])
    else:
        print("Images not found")
    return image_centers

images_dir = "/home/marcos/Pictures/examples" #"/home/marcos/Pictures/email_backup_buttons"
find_image_centers_email(images_dir)

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

