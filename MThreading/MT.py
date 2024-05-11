import threading
import time
import math

def fungsi_target_thd():
    """
    Target fungsi untuk dijalankan via threading
    """
    thread_name = threading.current_thread().name
    thread_pid = threading.current_thread().native_id
    info_log = f"{thread_name}[{thread_pid}]"

    print(f"{info_log} : Starting...")

    # big numpy factorial job
    print(f"{info_log} : Calculate factorial start")
    fact_result = math.factorial(500000)
    print(f"{info_log} : Calculate factorial finish")

    print(f"{info_log} : Bye...")

def spawning_thread(num_thread):
    print(f"Spawning {num_thread} thread")

    thread_list = []
    for i in range(num_thread):
        thread_item = threading.Thread(name=f"Thread#{i+1}", target=fungsi_target_thd)
        thread_list.append(thread_item)

    # another way to start
    print("Starting all threads")
    [thd.start() for thd in thread_list]

    # join it here
    print("Joining all threads")
    [thd.join() for thd in thread_list]


if __name__ == "__main__":
    print("MultiThreading Demo")
    duration = -time.perf_counter_ns()

    print("Spawning thread start")
    spawning_thread(30)
    print("Spawning thread done")

    duration += time.perf_counter_ns()
    print(f"Duration = {duration/1e6} ms")