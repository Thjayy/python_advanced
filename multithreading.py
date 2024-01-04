import concurrent.futures
import threading
import time

start = time.perf_counter()


def index(sec):
    print("run function...")
    time.sleep(sec)
    print("complete function")


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    t = [executor.submit(index, i) for i in seconds]
    for f in concurrent.futures.as_completed(t):
        f.result()



# threads = []

# for _ in range(10):
#     t = threading.Thread(target=index, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


# thread1 = threading.Thread(target=index)
# thread2 = threading.Thread(target=index)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

finish = time.perf_counter()

print(f"finished function {round(finish-start,2)} sec")