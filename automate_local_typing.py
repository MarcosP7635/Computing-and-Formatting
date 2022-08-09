from asyncio import subprocess
import multiprocessing
from pyautogui import *
from subprocess import Popen, check_call
import tkinter
import time
import pyperclip
import os
	
'''
Need to navigate to the correct directory and run the program
'''	

def edit_field(search_term):
	keyDown('ctrl')
	press('a')
	keyUp('ctrl')
	write(search_term)

def enter_inputs(images_dir, output_dir, target = 1, projectile = 1):
    edit_field(str(projectile))
    click_button(images_dir + "\\target_image.PNG",
                    direction = "Right", distance = 150)
    edit_field(str(target))
    time.sleep(.5)
    click_button(images_dir + "\\raw_output_image.PNG", 
                    direction = "Right", distance = 225)
    time.sleep(.5)
    keyDown('ctrl')
    press('s')
    keyUp('ctrl')
    time.sleep(.5)
    write(output_dir + "\\" + str(target) + " " + str(projectile))
    press('Enter')
    return 0

def run_local_process(wait_time, function, function_args):
	#run function for at most a given time in seconds
    multiprocessing.freeze_support()
    p = multiprocessing.Process(target = function, name= "function",
        args = function_args)
    p.start()
    print("started the loop")
    # Wait 10 seconds for foo
    time.sleep(wait_time)
    # Terminate foo
    p.terminate()
    # Cleanup
    p.join()
    print("Ran", function, "(", function_args, ")", "for ", wait_time,
        "seconds")

def click_on_pixel(pixel):
	x, y = pixel[0], pixel[1]
	click(x, y)

def click_button(image_file_path, direction = "Left", distance = 100):
	#Look for the image on the screen
	while True:
		image_center = locateCenterOnScreen(image_file_path)
		print("looking for ", image_file_path)
		if (image_center is not None):
			if(direction == "Left"):
				search_bar_location = (image_center[0] - distance, image_center[1])
			elif(direction == "Right"):
				search_bar_location = (image_center[0] + distance, image_center[1])
			elif(direction == "Up"):
				search_bar_location = (image_center[0], image_center[1] - distance)
			elif(direction == "Down"):
				search_bar_location = (image_center[0], image_center[1] + distance)
			print("Search bar located at coordinates: ", search_bar_location)
			break
	click_on_pixel(search_bar_location)
	return search_bar_location

def collect_data( 
		output_dir = "C:\\Users\\engin\\Documents\\GitHub\\Energy\\ImportedData\\DPASS_Output",
		images_dir = "C:\\Users\engin\\Downloads\\DPASS_icons",
		wait_time = 15):
    run_local_process(wait_time = wait_time, function = enter_inputs, 
                    function_args= (images_dir, output_dir))

def find_image_centers(images_dir):
    image_centers = {}
    for image_file in os.listdir(images_dir):
        image_centers[image_file] = locateCenterOnScreen(images_dir + "\\" + image_file)
    return image_centers