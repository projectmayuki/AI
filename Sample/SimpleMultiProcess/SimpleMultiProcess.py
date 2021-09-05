import multiprocessing
import queue

def worker_func(worker_index, input_queue, output_queue):

    import time
    time.sleep(3)
    
    while True:
        try:
            input = input_queue.get(timeout=5)
            print("worker_index:" + str(worker_index) + " ")
            print(input)
            # output_queue.put( (input_queue) )
            time.sleep(3)
        except queue.Empty:
            # キューが空になった
            print("worker index:" + str(worker_index) + " End : Queue is empty.")
            break
    return 
            

if __name__ == '__main__':
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    processes = list()
    num_worker = 3
    for worker_index in range(0, num_worker):
        process = multiprocessing.Process(
            target=worker_func,
            args=(worker_index, input_queue, output_queue))
        process.start()
        processes.append(process)

    input_queue.put( [ 1, 2] )
    input_queue.put( "Heelo" )
    input_queue.put( 3 )
    input_queue.put( (4, 5) )
    input_queue.put( "Bye" )

    for p in processes:
        p.join()

    print("All processes end.")
    
