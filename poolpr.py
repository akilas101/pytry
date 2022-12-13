import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Pool
from concurrent.futures import ProcessPoolExecutor
import os

# import multiprocessing as mp
# we can use the process class to launch a new process
# def wanabeme():
#     x = input('say my name')
#     return x

# print(wanabeme())

def ask_user():
    start = time.time()
    user_input = input('say my name')
    greet = f'hello, {user_input}'
    print(greet)
    print(f'ask user: {time.time() - start}')


def complex_calculation():
    start = time.time()
    print("calculation starting")
    [x ** 2 for x in range(20000000)]
    print(f'complex caculation: {time.time() - start}')
    return



start = time.time()
# ask_user()
# complex_calculation()
complex_calculation()

# we can import time and use it to time our processes
print(f'single thread total time: {time.time() - start}')

# # thread2 = Thread(target = complex_calculation)

# # thread1 = Thread(target = ask_user)
# # # thread1 = Thread(target = complex_calculation)
# # # to show that if we ran two cpu tasking processes it will take the total time each would have used alone

# # start = time.time()


# # thread2.start()
# # thread1.start()


# # thread2.join()
# # thread1.join()
# with ThreadPoolExecutor(max_workers=2)as pool:
#     pool.submit(complex_calculation)
#     pool.submit(ask_user)

# print(f'Two thread total time = {time.time() - start}')

# multiprocessing
# it is not easy multiple processes beacause it is not easy to share the resources


#  process = Process(target=complex_calculation)
#     #  process2 = Process(target = ask_user)
#     #  process2 = Process(target = complex_calculation)

#  process.start()
#     #  process2.start()
#  start = time.time()
#     #  ask_user()
#  process.join()
#     #  process2.join()
#  print(f'h total time = {time.time() - start}')

# print(__name__)

# def f(x):
#     return x*x

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    


if __name__ == '__main__':
   
    process = Process(target = complex_calculation())
    process2 = Process(target = complex_calculation())
    start = time.time()
    process.start()
    process2.start()
#   this block runs two processes at the same time giving our program access to two cores 
    #  ask_user()
    process.join()
    process2.join()
   
    print(f'multiprocessing total time = {time.time() - start}')


