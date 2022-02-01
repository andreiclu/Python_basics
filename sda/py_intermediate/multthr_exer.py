import multiprocessing
import timeit as profile
import threading
from typing import List

def search_elem(input: List[int], elem: int) -> bool:
    #if elem in input:
        #print(input.index(elem), len(input))
    return elem in input


def threads_func(nr_threads, input, elem):
    threads = []
    l = len(input)//nr_threads
    for i in range(nr_threads):
        threads.append(threading.Thread(target=search_elem, args=(input[i * l:(i + 1) * l], elem)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def multiprocess_func(nr_process, input, elem):
    processes = []
    l = len(input) // nr_process
    for i in range(nr_process):
        processes.append(multiprocessing.Process(target=search_elem, args=(input[i * l:(i + 1) * l], elem)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    # TODO add nr_threads in the threads list
    # TODO give each thread similar portion of the list to execute

if __name__ == "__main__":
    #print("Number of threads= ")
    nr_threads = 1

    my_input = [i for i in range(1000)]
    elem_cautat = 621
    #threads_func(nr_threads, my_input, elem_cautat)
    #multiprocess_func(nr_threads, my_input, 852147)
    with_multiprocessing = "multiprocess_func(nr_threads, my_input, elem_cautat)"
    setup = "from __main__ import multiprocess_func, threads_func, my_input, elem_cautat, nr_threads"

    with_threading = "threads_func(nr_threads, my_input, elem_cautat)"

    timpThread = profile.timeit(stmt=with_threading, setup=setup, number=10)
    timpMultiProcess = profile.timeit(stmt=with_multiprocessing, setup=setup, number=10)
    print(timpThread, timpMultiProcess)

    #TODO use timeit to profile each method