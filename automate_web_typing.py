from asyncio import subprocess
import webbrowser
import multiprocessing
from pyautogui import *
from subprocess import Popen, check_call
from random import *
import tkinter
import time
import pyperclip

def open_tab(url):
	firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
	webbrowser.get(firefox_path).open(url)
	print("opening ", url)

def click_on_pixel(pixel):
	x, y = pixel[0], pixel[1]
	click(x, y)

def get_random_wait(wait_min, wait_max):
	random_wait = wait_min + ((wait_max - wait_min) * random())
	return random_wait

def click_search_bar(image_file_path, direction = "Left"):
	#Look for the image on the screen
	while True:
		image_center = locateCenterScreen(image_file_path)
		print("looking for ", image_file_path)
		if (image_center is not None):
			if(direction = "Left"):
				search_bar_location = (image_center[0] - 100, image_center[1])
			elif(direction = "Right"):
				search_bar_location = (image_center[0] + 100, image_center[1])
			elif(direction = "Up"):
				search_bar_location = (image_center[0], image_center[1] - 100)
			elif(direction = "Down"):
				search_bar_location = (image_center[0], image_center[1] + 100)
			print("Search bar located at coordinates: ", search_bar_location)
			break
	click_on_pixel(search_bar_location)
	return search_bar_location

def run_process(wait_time, function, function_args, url):
	#run function for at most a given time in seconds
	p = multiprocessing.Process(target = function, name= "function",
		args = function_args)
	p.start()
	open_tab(url)
	print("started the loop")
	# Wait 10 seconds for foo
	time.sleep(wait_time)
	# Terminate foo
	p.terminate()
	# Cleanup
	p.join()
	print("Ran", function, "(", function_args, ")", "for ", wait_time,
		"seconds")

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

def autofill(image_file_path = "C:/Users/engin/Downloads/wolframAlphaEqualSign.PNG",
	        url = "https://www.wolframalpha.com", max_loading_time = 5,
			min_wait_to_look_human = 0.25, max_wait_to_look_human = 0.5,
			lag_between_button_pushes = 0.1, **kwargs):
	'''
	This function will look for an image that matches the image_file_path then click near it
	and either type in a specified search term or paste whatever is on the clipboard.
	'''
	run_process(max_loading_time, click_search_bar, image_file_path, url)
	#run function for at most a given time in seconds
	try:
	#There can only be a key in the dictionary named string from user input
		write(search_term, interval = random() * lag_between_button_pushes)
	except:
		#just copy and paste :)
		keyDown('ctrl')
		press('v')
		keyUp('ctrl')
	#wait to search
	time.sleep(get_random_wait(min_wait_to_look_human, max_wait_to_look_human))
	press('Enter')

def get_webpage_text(image_file_path = "C:/Users/engin/Downloads/caltechLogoToClick.PNG",
	        url = "http://schedules.caltech.edu/WI2020-21.html", 
			notepad_path = "C:\\Windows\\notepad.exe", 
			output_path = "C:\\Users\\engin\\Downloads\\output.txt",
			**kwargs):
	'''
	This function will look for an image that matches the image_file_path then click near it
	and either type in a specified search term or paste whatever is on the clipboard.
	'''
	run_process(max_loading_time, click_search_bar, image_file_path, url)
	#run function for at most a given time in seconds
	#just copy and paste :)
	keyDown('ctrl')
	press('a')
	press('c')
	keyUp('ctrl')
	subprocess.os.system(notepad_path)
	click_search_bar(image_file_path, "Down")
	#now we have all the text on the clipboard
	with open(output_path, "w") as text_file:
    	text_file.write(pyperclip.paste())
	#now we will put the clipboard into a string
