import threading
import time
import random

shared_list = []

def append_to_list(lock, timeout=0):
    global shared_list
    # lock.acquire() 

    # time.sleep(random.uniform(0, timeout))  # Simulating I/O-bound operation
    if timeout:
      time.sleep(random.uniform(0, timeout))  # Simulating I/O-bound operation
      for i in range(10):
        shared_list.append("waiting")
    shared_list.append(threading.current_thread().name)
    for i in range(10):
        shared_list.append(i)
    # lock.release()

lock = threading.Lock() 
# Create two threads that modify the shared list concurrently
thread1 = threading.Thread(target=append_to_list, args=(lock, 10))
thread2 = threading.Thread(target=append_to_list, args=(lock, 10))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final content of the shared list
print("Final content of the shared list:", shared_list)