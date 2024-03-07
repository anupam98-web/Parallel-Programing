import threading
import time
import random

def task1():
    print("Task 1 started")
    time.sleep(random.uniform(0, 10))  # Simulating I/O-bound operation with timeout of 3 seconds
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(random.uniform(0, 5))  # Simulating I/O-bound operation with timeout of 5 seconds
    print("Task 2 completed")

def task3():
    print("Task 3 started")
    time.sleep(random.uniform(0, 2))  # Simulating I/O-bound operation with timeout of 2 seconds
    print("Task 3 completed")

# Create and start a thread for each task
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread3 = threading.Thread(target=task3)

thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All tasks completed")
