import webbrowser
from pyautogui import *
from subprocess import Popen, check_call
from random import *
import tkinter

'''
Please use the command pyautogui.position() to find the location of the mouse
on the screen when you put your cursor over the search bar in wolframalpha.
Then change the variable search_bar to the location of that pixel.
'''

search_bar = (2500, 700)

def open_tab(url):
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)

def open_click_close(url, wait_time, pixel): #open and close tab
	open_tab(url)
	time.sleep(wait_time[0])
	click_on_pixel(pixel)
	time.sleep(wait_time[1])
	close_tab()

def close_tab():
	keyDown('ctrl')
	press('w')
	keyUp('ctrl')

def click_on_pixel(pixel):
	x, y = pixel[0], pixel[1]
	click(x, y)

wolfram_alpha_url = "https://www.wolframalpha.com"


def web_page_search(url, input):
	#Similar setup to the docustring
	wait_min, wait_max = 2.5, 3
	diff = wait_max - wait_min
	wait_time = (wait_min * random() + diff * random(),
		wait_min * random() + diff * random())
	#search_button = (3700,700)
	#Here input is a string representing what to search
	open_tab(url)
	time.sleep(wait_time[0])
	click_on_pixel(search_bar)
	write(input, interval = random() * .1)
	time.sleep(wait_time[1])
	keyDown('Enter')
#search on wolframalpha whatever is on the clipboard
web_page_search(wolfram_alpha_url, tkinter.Tk().clipboard_get())

#It currently moves ecosia's counter 1/3 of the time
