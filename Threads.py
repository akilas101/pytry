import time
from threading import Thread
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
    [x**2 for x in range(20000000)]
    print(f'complex caculation: {time.time() - start}')

start = time.time()
ask_user()
complex_calculation()
# we can import time and use it to time our processes
print(f'single thread total time: {time.time() -start}')

thread2 = Thread(target = complex_calculation)

thread1 = Thread(target = ask_user)
# thread1 = Thread(target = complex_calculation)
# to show that if we ran two cpu tasking processes it will take the total time each would have used alone

start = time.time()


thread2.start()
thread1.start()


thread2.join()
thread1.join()

print(f'Two thread total time = {time.time() - start}')