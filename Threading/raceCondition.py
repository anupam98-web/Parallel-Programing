# import threading
# import time
# import random

# counter = 0

# def increment_counter(timeout=None):
#   global counter
#   if timeout:
#     time.sleep(random.uniform(0, timeout))  # Simulating I/O-bound operation
#     for _ in range(100000):
#         counter += 1

#   else:
#     for _ in range(100000):
#         counter += 1

# def main():
#   # global counter
#   # counter = 0
#   # Create two threads that increment the counter concurrently
#   thread1 = threading.Thread(target=increment_counter, args=(10,))
#   thread2 = threading.Thread(target=increment_counter)

#   # Start the threads
#   thread1.start()
#   thread2.start()

#   # Wait for the threads to finish
#   thread1.join()
#   thread2.join()

# for i in range(5):
#   main()
#   # Print the final value of the counter
#   print(f"i: {i} and counter: {counter}")


import threading
import time
import random

shared_list = []

def append_to_list(timeout=0):
    global shared_list
    # time.sleep(random.uniform(0, timeout))  # Simulating I/O-bound operation
    if timeout:
      time.sleep(random.uniform(0, timeout))  # Simulating I/O-bound operation
      for i in range(10):
        shared_list.append("waiting")
    shared_list.append(threading.current_thread().name)
    for i in range(10):
        shared_list.append(i)

# Create two threads that modify the shared list concurrently
thread1 = threading.Thread(target=append_to_list, args=(10,))
thread2 = threading.Thread(target=append_to_list)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final content of the shared list
print("Final content of the shared list:", shared_list)

