## AsyncIO
Async IO is a library that provides an asynchronous I/O framework for Python.
It use coroutines and event loops to provide non-blocking code and run code parallely.

So What are Coroutines?

# Coroutines
- A coroutine in Python is a special type of function that can pause and resume its execution at certain points. It allows for cooperative multitasking, enabling multiple tasks to run concurrently within a single thread. Coroutines are a fundamental building block of asynchronous programming in Python, particularly with libraries like asyncio.
-  Coroutines are defined using the `async def` syntax in Python. This syntax distinguishes them from regular functions and indicates that they can use `await` expressions to pause their execution.
-  Coroutines are non-blocking, meaning that when **one coroutine is waiting for an operation to complete (such as I/O or a sleep), other coroutines can continue to execute**. This allows for **efficient concurrency within a single thread**.
- Coroutines are not executed immediately upon definition. Instead, they are scheduled for execution within an event loop. The event loop manages the execution of coroutines, scheduling and running them in an efficient manner.
- Coroutines can return values using the return statement, just like regular functions. However, when calling a coroutine, you typically use await to retrieve its result, as coroutines return awaitable objects.

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)  # Pause execution for 1 second
    print("World")
    return "Done"

async def main():
    result = await greet()
    print("Coroutine returned:", result)

asyncio.run(main())  # Run the main coroutine within the asyncio event loop

```
- Async functions have a lifecycle similar to generator-based coroutines:
- They start execution when called, returning a coroutine object.
- Execution proceeds until the first await expression is encountered.
- Control returns to the event loop, and the coroutine suspends.
- The event loop schedules other tasks or coroutines for execution.
- When the awaited operation completes, the coroutine resumes execution.
- This process continues until the coroutine reaches the end or encounters an exception.


# How Coroutines are implemented.
We first have to understand how **Generator** Works. As Coroutines use generator for there implementation.
I have given [Coroutine Implementation using Generators](coroutine.py). Please  go through it before moving forward.
Now what we see in current python are `async await`.

[Basic code using AsyncIO to show wait and execution of another function.](asyncio.py) -> 
Talk about how there is waiting in the program. And how we add the fn2 to execute `await` keyword makes our function wait till it completed and then move to next line of code.
[Creating a Task Using AsyncIO and showing parallelism](asyncio2.py) -> 
- In This file we have created a task so that it will run fn2 until fn1 is waiting showing proper concurrent programming. I have given the output in the code itself for better understanding.
- This means that the other function will begin to run anytime if there is any free time using asyncio.create_task(fn2())
[Running 3 Functions using AsyncIO showing how differnt function run parallely.](asyncio3.py) -> 
- We have use `await asyncio.gather()` method of asyncio. Task will start whenever other task is waiting achieving concurrency.
- func1(), func2(), and func3() functions are simulated I/O-bound tasks using asyncio.sleep(). They each “wait” for a different amount of time to simulate varying levels of work.
- When you run this code, you’ll see that the tasks start concurrently, perform their work asynchronously, and then complete in parallel. The order of completion might vary depending on how the asyncio event loop schedules the tasks. This asynchronous behavior is fundamental to understanding how to manage tasks efficiently, especially when working with async iterators in Python.

Please play with code and check how the output is changing.


# Note
- **Unlike multithreading, where threads are managed by the operating system scheduler, asyncio uses a single-threaded event loop to manage multiple asynchronous tasks. This event loop schedules and executes tasks in a cooperative manner, avoiding the overhead associated with thread creation and context switching.**
- Asyncio Runs on Single Thread.
Event Loop:
- Coroutines are executed within an event loop, which schedules and runs coroutines in a cooperative multitasking manner.
The event loop manages the execution of coroutines, scheduling and running them in an efficient manner. It ensures that coroutines yield control appropriately so that other tasks can execute concurrently.
- Both asyncio and JavaScript's event loop facilitate concurrency and scalability by allowing multiple tasks to execute concurrently without the overhead of creating additional threads. This enables efficient handling of large numbers of concurrent connections or operations.