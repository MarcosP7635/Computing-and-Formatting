import webbrowser
import multiprocessing
from pyautogui import *
from subprocess import Popen, check_call
from random import *
import tkinter
import time

string = '''\\begin{equation}
\\begin{split}
\\\\
\\end{split}
\\end{equation}'''
time.sleep(1)
click(position())
write(string)
