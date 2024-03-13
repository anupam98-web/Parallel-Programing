import concurrent.futures
import os
import threading
import time, random

def worker():
  thread_id = threading.get_ident()
  time.sleep(random.uniform(0, 10))  # Simulating I/O-bound operation
  print("Worker is doing it's work, ", thread_id)

def worker_second():
  thread_id = threading.get_ident()
  time.sleep(random.uniform(0, 5))  # Simulating I/O-bound operation
  print("worker_second is doing it's work, ", thread_id)

# creation of thread pool
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2) 

pool.submit(worker)
pool.submit(worker_second)

# waits for the worker threads
pool.shutdown(wait=True)

print("Main thread continuing to run")
