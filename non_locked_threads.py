import time
import random
from threading import Thread

counter = 0


def Increment_counter():
 global counter
 time.sleep(random.random())

 counter+=1
 time.sleep(random.random())
 
 print(f"New increment counter {counter}")
 time.sleep(random.random())
 print("-------------------------")


for i in range(10):
    # Increment_counter()
    # the above part works fine because it is running sequentially

# we will now implement the abouve statement using Threads
    # T = Thread(target = Increment_counter)
    # T.start()
    # this also looks like it works sequentially but that is wrong
    # the reason it looks sequential is only because the abouve funtion is so small that is completes before a new thread is created
    # to test for that we use the rndom and time modules
    # the method is called FUZZYING, its is inserting random time lags in between statements to test if they are working properly 

    T = Thread(target = Increment_counter)
# we will insert a random time.sleep ,thods which will stop the thread for a random number of seconds in each loop
    time.sleep(random.random())
    T.start()

