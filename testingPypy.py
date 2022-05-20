#print the nth fibonacci number using python
def nth_fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibb(n-1) + nth_fibb(n-2)

print(nth_fibb(10))

#time the how long it takes to fun a function
import time

def time_function(func, *args):
    t1 = time.time()
    result = func(*args)
    t2 = time.time()
    #turn the function name into a string
    string_output = func.__name__ + "(" + str(*args) + ") = " + str(result) 
    string_output += " ran in " + str(t2-t1) + " seconds"
    return string_output

print(time_function(nth_fibb, 10))
