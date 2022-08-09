from multiprocessing import Process, freeze_support, Pool
from automate_local_typing import *
if __name__ == '__main__':
    pool = Pool(processes=2)              # start 4 worker processes
    collect_data()

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
    print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"
