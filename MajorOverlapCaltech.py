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

# %%

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
        argument_names = ("department_number", 
            "abbreviation", "class_times", "terms_offered",
            "years_offered")  
        inputs = assign_inputs({}, argument_names, kwargs)
        self.inputs = inputs  
        
    def add_courses(self, additional_courses):
        self.courses = np.append(self.courses, 
            additional_courses)

#%%

class Major:

    '''
    You can set whatever you want as an attribute! 
    Only abbreviation and name are required.
    Some useful optional attributes:
    
    catalog_file_path: string that is the file path of 
        the PDF of the Caltech catalog.
        
    courses: list of courses that are offered in the major.

    required_course: numpy array of all the courses that can 
    be used to satify that specific requirement. 
    '''

    def __init__(self, abbreviation, name, **kwargs):
	    #kwargs is a dictionary 
       self.abbreviation = abbreviation
       self.name = name
       for key in kwargs:
            setattr(self, key, kwargs[key])

    def get_string_from_pdf(self, pdf_file_path):
        from PyPDF2 import PdfFileReader
        pdf_file = PdfFileReader(open(pdf_file_path, "rb"))
        page = pdf_file.getPage(0)
        pdf_complete_text = ""
        total_pages = pdf_file.getNumPages()
        for i in range(total_pages):
            page = pdf_file.getPage(i)
            pdf_complete_text += page.extractText()
        self.catalog = pdf_complete_text

    def read_from_catalog(self, catalog):
        for term in self.terms:
            for course in catalog.courses:
                if course.inputs["terms_offered"] == term.name:
                        term.add_course(course)

    def find_major_name(major_string):
        major_name_start = major_string.find("Major:")
        major_name_end = major_string.find("Requirements:")
        major_name = major_string[major_name_start+7:major_name_end-1]
        return major_name

astro = Major(abbreviation = 'Ay', name = 'Astrophysics', 
    catalog_file_path = 'catalogUGinfo.pdf')
#astro.get_string_from_pdf(astro.catalog_file_path)
print(astro.abbreviation, astro.name)
#astro.terms = np.array([Term(name="Fall"), Term(name="Spring")])
#astro.get_string_from_pdf("catalogUGinfo.pdf")
#print(astro.catalog_complete_text)
#%%

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
        self.constraints, self.major_array = (
            time_constraints, major_array)
    
    def add_terms(self, additional_terms):
        np.append(self.terms, additional_terms)

    def assign_classes(term):
        pass

#find name of major in the string
geobio_name = 'Geobiology'
geobio = Major(abbreviation = geobio_name, 
        name = geobio_name, 
        catalog_file_path = astro.catalog_file_path)

astro_geobio_schedule = Schedule(['2022 Fall', '2022 Spring'], 
     [astro, geobio])
print(astro_geobio_schedule.time_constraints)
for major in astro_geobio_schedule.major_array:
    print(major.name)
#ADD INSTITUTE REQUIREMENTS!!
# %
# %%
