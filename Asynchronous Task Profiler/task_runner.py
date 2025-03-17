"""CPU-heavy task (cpu_heavy_task): Функция, которая выполняет вычисления на процессоре, создавая нагрузку.
Асинхронная задача async_task---- нагружаем процессор функцией cpu_heavy_task.
Запускаем в потоке thread_worker- при многозадачности по потоку для CPU-bound задач значительного прироста
 производительности не будет из-за GIL (Global Interpreter Lock) в Python
Мы запускаем в процессе process_worker, и процесс обеспечивает параллельность, потому что каждый 
процесс работает в своем собственном пространстве памяти и не ограничен GIL и дляля CPU-bound задач это лучше.
Запуск с использованием процессов (run_processes):здесь нам нужно использовать процессы для выполнения задачи,каждый
процесс работает в своем собственном адресном пространстве, и GIL не влияет на их параллельность,и улучшаем производительность для CPU-bound
асинхронная версия run_async--использует асинхронное выполнение, но  основная нагрузка все равно ложится на CPU.
Для CPU-bound задач использовуем процессы multiprocessing, потому что они обходят GIL и могут использовать несколько ядер процессора."""
"""CPU-heavy task (cpu_heavy_task): A function that performs calculations on the processor, creating a load.
Asynchronous task async_task---- we load the processor with the function cpu_heavy_task.
We run in the thread_worker thread- when multitasking by thread for CPU-bound tasks there will be no significant increase in
performance due to the GIL (Global Interpreter Lock) in Python
there will be no performance because of GIL (Global Interpreter Lock) in Python
We run in process_worker process, and process provides parallelism because each process runs in its own memory space and is not limited by GIL and for CPU-bound tasks it is better.
Run using processes (run_processes): here we need to use processes to perform the task, each process runs in its own address space, and GIL does not affect their parallelism, and improves performance for CPU-bound
asynchronous version run_async--uses asynchronous execution, but the main load still falls on the CPU.
For CPU-bound tasks, we use multiprocessing processes because they bypass the GIL and can use multiple processor cores."""
import asyncio
import threading
import multiprocessing
import time

def cpu_heavy_task(n):

    count = 0
    for _ in range(n):
        count += 1

    return count

async def async_task(n):
   
    await asyncio.sleep(0)
    return cpu_heavy_task(n)

def thread_worker(n):
    """flow  поток"""
    return cpu_heavy_task(n)

def process_worker(n):
    """ процесс process"""
    return cpu_heavy_task(n)

def run_threads(n, workers=4):
    """Запускаем задачу в потоках"""
    """Running a task in threads"""
    threads = []
    for _ in range(workers):
        t = threading.Thread(target=thread_worker, args=(n,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def run_processes(n, workers=4):
    """Запускаем задачу в процессах"""
    """Running a task in processes"""
    processes = []
    for _ in range(workers):
        p = multiprocessing.Process(target=process_worker, args=(n,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

async def run_async(n, workers=4):
    """Запускаем задачу асинхронно"""
    """Run the task asynchronously"""
    tasks = [async_task(n) for _ in range(workers)]
    await asyncio.gather(*tasks)