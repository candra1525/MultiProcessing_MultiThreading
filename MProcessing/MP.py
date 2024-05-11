import multiprocessing
import time
import math

def fungsi_target_mp():
    """
    Target fungsi untuk dijalankan via multiprocessing
    """
    core_id = multiprocessing.current_process()._identity[0]
    process_name = multiprocessing.current_process().name
    process_pid = multiprocessing.current_process().pid
    process_daemon = multiprocessing.current_process().daemon
    info_log = f"{process_name}[{process_pid}]-[{core_id}]-[{process_daemon}]"

    print(f"{info_log} : Starting...")

    # big numpy factorial job
    print(f"{info_log} : Calculate factorial start")
    fact_result = math.factorial(500000)
    print(f"{info_log} : Calculate factorial finish")

    print(f"{info_log} : Bye...")


def spawning_process(num_process, is_background_process=False):
    print(f"Spawning {num_process} process with daemon mode = {is_background_process}")

    process_list = []
    for i in range(num_process):
        process_item = multiprocessing.Process(name=f"Process#{i+1}", target=fungsi_target_mp, daemon=is_background_process)
        process_list.append(process_item)

    # another way to start
    print("Starting all processes")
    [proc.start() for proc in process_list]

    # join it here
    print("Joining all processes")
    [proc.join() for proc in process_list]


if __name__ == "__main__":
    print("Multiprocessing Demo")
    print(f"CPU = {multiprocessing.cpu_count()} core(s)")

    duration = -time.perf_counter_ns()

    print("Spawning process start")
    spawning_process(30, True)
    print("Spawning process done")

    duration += time.perf_counter_ns()
    print(f"Duration = {duration/1e6} ms")