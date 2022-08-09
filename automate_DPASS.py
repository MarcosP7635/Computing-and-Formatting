from multiprocessing import Process, freeze_support, Pool
from automate_local_typing import *
if __name__ == '__main__':
    wait_time = 60
    output_dir = "C:\\Users\\engin\\Documents\\GitHub\\Energy\\ImportedData\\DPASS_Output"
    images_dir = "C:\\Users\engin\\Downloads\\DPASS_icons"
    program_path = ["C:\\Users\\engin\\Downloads\\DPASS2106\\DPASS2106\\DPASS.exe"]
    pool = Pool(processes=2)              # start 4 worker processes
    result = pool.apply_async(os.system, program_path)
    result2 = pool.apply_async(enter_inputs, (images_dir, output_dir))
    result2.get(timeout= wait_time)    #run the function for at most a given time in seconds
    result.get()                  

