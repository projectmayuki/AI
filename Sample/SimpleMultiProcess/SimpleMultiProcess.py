import multiprocessing
import queue

def worker_func(worker_index, input_queue, output_queue):

    import time
    
    while True:
        try:
            input = input_queue.get(timeout=5)
            print("worker_index:" + str(worker_index) + " ")
            print(input)
            output_queue.put((worker_index, input))
            time.sleep(3)
        except queue.Empty:
            # キューが空になった
            print("worker index:" + str(worker_index) + " End : Queue is empty.")
            break
    return 
            

if __name__ == '__main__':
    m = multiprocessing.Manager()
    input_queue = m.Queue()
    output_queue = m.Queue()

    input_queue.put( [ 1, 2] )
    input_queue.put( "Heelo" )
    input_queue.put( 3 )
    input_queue.put( (4, 5) )
    input_queue.put( 6.0 )
    input_queue.put( "Bye" )

    num_worker = 3

    # Pool
    pool = multiprocessing.Pool()
    for worker_index in range(0, num_worker):
        pool.apply_async(worker_func, args=(worker_index, input_queue, output_queue))

    pool.close()
    pool.join()

    print("All processes end.")
    while output_queue.empty() == False:
        q = output_queue.get()
        print(q)


    # Process
    input_queue.put( [ 1, 2] )
    input_queue.put( "Heelo" )
    input_queue.put( 3 )
    input_queue.put( (4, 5) )
    input_queue.put( 6.0 )
    input_queue.put( "Bye" )

    process_list = []
    for worker_index in range(0, num_worker):
        p = multiprocessing.Process(
            target=worker_func,
            args=(worker_index, input_queue, output_queue))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()

    print("All processes end.")
    while output_queue.empty() == False:
        q = output_queue.get()
        print(q)
