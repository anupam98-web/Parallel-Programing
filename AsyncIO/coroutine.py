# Python3 program for demonstrating 
# coroutine execution 

def print_name(prefix): 
	print("Searching prefix:{}".format(prefix)) 
	yield 1
	yield 2
	yield 3
	while True:
	    print('Coroutine starting and waiting for the send method')
	    name = (yield) # wait until a value is sent to this coroutine.
	    print(name)
# 		print('11')
	    if prefix in name: 
	    	print('1')

# calling coroutine, nothing will happen 
corou = print_name("Dear") 

# This will start execution of coroutine and 
# Prints first line "Searching prefix..." 
# and advance execution to the first yield expression 
print(corou.__next__()) # yeild 1
print(corou.__next__()) # yeild 2
print(corou.__next__()) # yeild 3

# Coroutine starting
print(corou.__next__()) # initiate the coroutine
# corou.__next__() 
# next(corou)


# sending inputs 
corou.send("Atul") 
corou.send("Dear Atul") 
corou.close()
# corou.send("Dear Atul") 
# print(corou.__next__())



def coroutine():
    print("Coroutine started")
    value = yield  # Pause and wait for a value
    print("Received:", value)
    result = yield    # Pause and return a value
    print("Final result:", result)
    print("Final result:", result)
    print("Final result:", result)
    print("Final result:", result)
    print("Final result:", result)
    res2 = yield
    print(res2)

# Create a generator object from the coroutine
gen = coroutine()

# Start the coroutine and advance to the first yield expression
next(gen)

# Send a value to the coroutine
gen.send("Hello")

# Resume the coroutine and retrieve the result
gen.send("Done")
gen.send("Done2")
# print("Result:", result)
