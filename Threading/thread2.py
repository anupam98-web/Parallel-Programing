import threading
import time
import random

def task_with_timeout(task_name, timeout):
    print(f"Task '{task_name}' started")
    time.sleep(random.uniform(0, timeout))  # Simulating I/O-bound operation
    print(f"Task '{task_name}' completed")

# List of tasks with corresponding timeouts
tasks = [
    ("Task 1", 3),
    ("Task 2", 5),
    ("Task 3", 2)
]

# Create and start a thread for each task
threads = []
for task_name, timeout in tasks:
    thread = threading.Thread(target=task_with_timeout, args=(task_name, timeout))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
# for thread in threads:
#     thread.join()

print("All tasks completed")
