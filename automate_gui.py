import automate_web_typing
from automate_web_typing import *

#Edit the following line to change the search term
def edit_field(search_term):
	keyDown('ctrl')
	press('a')
	keyUp('ctrl')
	write(search_term, interval = [0.1] * len(search_term))