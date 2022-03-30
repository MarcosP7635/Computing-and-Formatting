#%%
import numpy as np
import plotly

'''
Here I will use the words inputs and arguments interchangeably.
Recommended for functions that have a lot of arguments.
Note that since the reslting inputs are a dictionary they are
accessed with the form inputs["example_name_1"].
 
argument_names is a list of strings, which include the names
of all optional and required arguments.

inputs is a dictionary that will be used to store the 
inputs. 

Each key is the default value of an input. If
the user specifies an input, the default value will be 
reassigned to the user input (represented by kwargs).

Example:
def function_name(**kwargs):
	#kwargs is a dictionary
    default_values = {"non_optional_variable": default_value}
    argument_names = ("example_name_1", "example_name_2")  
    inputs = assign_inputs(default_dict, argument_names, 
                       user_input)
'''

def assign_inputs(default_dict, argument_names, 
        user_input):
        inputs = default_dict
        for index in range(len(user_input)):
            inputs[argument_names[index]] = user_input[index]
        return inputs


#%%
class Course:
    def assign_inputs(default_dict, argument_names, 
        user_input):
        inputs = default_dict
        for index in range(len(user_input)):
            inputs[argument_names[index]] = user_input[index]
        return inputs

    def __init__(self, **kwargs):
	#kwargs is a dictionary 
        argument_names = ("department_number", "name",
            "class_times", "terms_offered", "years_offered")  
        inputs = assign_inputs({}, argument_names, kwargs)
        self.inputs = inputs  
        
    def add_courses(self, additional_courses):
        self.courses = np.append(self.courses, 
            additional_courses)

#%%
'''
Each major is an object with the following attributes:

name: string of the name of major

requirements: dictionary of requirements for the major.

required_course: numpy array of all the courses that can 
be used to satify that specific requirement. 
'''

class Major:
    def assign_inputs(default_dict, argument_names, 
        user_input):
        inputs = default_dict
        for index in range(len(user_input)):
            inputs[argument_names[index]] = user_input[index]
        return inputs

    def __init__(self, **kwargs):
	#kwargs is a dictionary 
        argument_names = ("name", "requirements")  
        inputs = assign_inputs({}, argument_names, kwargs)
        self.inputs = inputs   

    def read_from_catalog(self, catalog):
        for term in self.terms:
            for course in catalog.courses:
                if course.inputs["terms_offered"] == term.name:
                        term.add_course(course)

#%%

'''
This next codeblock will use TQFRs and the major requirements 
to create a schedule for a given major.
major_array is a numpy array of Major objects (also includes
minors)
'''

class Schedule:
    def __init__(self, time_constraints, major_array):
        self.time_constraints = time_constraints
        self.terms = np.array([])

        for i in range():
            self.terms.append(Term(time_constraints))
    
    def add_terms(self, additional_terms):
        np.append(self.terms, additional_terms)
    
    #def assign_classes(term):

    
'''
now I need to get a string from a PDF file to get the required courses for a given major
'''
 
# %%
