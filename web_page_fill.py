import webbrowser
import multiprocessing
from pyautogui import *
from subprocess import Popen, check_call
from random import *
import tkinter
import time

def open_tab(url):
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)

def click_on_pixel(pixel):
	x, y = pixel[0], pixel[1]
	click(x, y)

def get_random_wait(wait_min, wait_max):
	random_wait = wait_min + ((wait_max - wait_min) * random())
	return random_wait

def click_search_bar(image_file_path):
	#Look for the image on the screen
	image_center = locateCenterScreen(image_file_path)
	if (image_center is not None):
		search_bar_location = (image_center[0] - 100, image_center[1])
		print("Search bar located at coordinates: ", search_bar_location)
	click_on_pixel(search_bar_location)
	return search_bar_location

def run_process(wait_time, function, function_args):
	#run function for at most a given time in seconds
	p = multiprocessing.Process(target = function, name= "function",
		args = function_args)
	p.start()
	print("started")
	# Wait 10 seconds for foo
	time.sleep(wait_time)
	# Terminate foo
	p.terminate()
	# Cleanup
	p.join()
	print("process run: ", function, "(", function_args, ")")

'''
Based on the size of your screen and where wolframAlpha will open in your
browser, please correct searc_bar (line 46) with the appropiate coordinates
by hovering putting your mouse in the middle of the search bar on the desired
web page and running the command pyatuogui.position() which is described here:
https://pyautogui.readthedocs.io/en/latest/mouse.html

All times are in seconds.
The default for web_page_search:
Go to wolframalpha.com and search
whatever is on the clipboard. The script looks for part of the screen
that matches 'image'. It will wait up 10 seconds for the page to load before
giving up.
The script will just paste whatever was most recently copied into the search
bar.

Inputs_dict starts with the smallest number of default inputs for the function
to work as intended, then is overwritten with the user input (if any)

All arguments for web_page_search are optional, but when you do specify an
argument you must also specify all of the arguments before it.
web_page_search(search_bar, url, max_loading_time, search_term,
min_wait_to_look_human, max_wait_to_look_human, lag_between_button_pushes,
image_file_path)
One can simply use all of the default values by running web_page_search without
any input, that is:
	web_page_search().
'''

def web_page_search(**kwargs):
	#kwargs is a dictionary
	inputs_dict = {
		"image_file_path": "C:/Users/engin/Downloads/wolframAlphaEqualSign.PNG",
		#file path of an image which we will look for to see when the page loads
		"url": "https://www.wolframalpha.com", #webpage to open
		"max_loading_time": 5, #seconds
		"min_wait_to_look_human": 0.25, #seconds
		"max_wait_to_look_human": 0.5, #seconds
		"lag_between_button_pushes": 0.1, #seconds
		}
	argument_names = ("search_bar", "max_loading_time", "url", "search_term",
		"min_wait_to_look_human", "max_wait_to_look_human",
		"lag_between_button_pushes", "image_file_path")
	for index in range(len(kwargs)):
		inputs_dict[argument_names[index]] = kwargs[index]
		#Overwrite defaults with the user input
	print(inputs_dict)
	open_tab(inputs_dict["url"])
	#Click in the middle of the search bar
	run_process(inputs_dict["max_loading_time"], click_search_bar,
		inputs_dict["image_file_path"])
	#run function for at most a given time in seconds
	try:
	#There can only be a key in the dictionary named string from user input
		write(inputs_dict["search_term"],
			interval = random() * inputs_dict["lag_between_button_pushes"])
	except:
		#just copy and paste :)
		keyDown('ctrl')
		press('v')
		keyUp('ctrl')
	#wait to search
	time.sleep(get_random_wait(inputs_dict["min_wait_to_look_human"],
		inputs_dict["max_wait_to_look_human"]))
	press('Enter')

#search on wolframalpha whatever is on the clipboard
web_page_search()
