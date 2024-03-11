# Python program to understand 
# the concept of pool 
import multiprocessing 
import os 

def square(n): 
	print("Worker process id for {0}: {1}".format(n, os.getpid())) 
	return (n*n) 

if __name__ == "__main__": 
	# input list 
	mylist = [1,2,3,4,5] 

	# creating a pool object 
	p = multiprocessing.Pool() 

	# map list to target function 
	result = p.map(square, mylist) 

	print(result) 

# Worker process id for 2: 4152
# Worker process id for 1: 4151
# Worker process id for 4: 4151
# Worker process id for 3: 4153
# Worker process id for 5: 4152
# [1, 4, 9, 16, 25]