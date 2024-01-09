# import time
# import multiprocessing

# start = time.perf_counter()

            
# def index(num):
#     # print("run function...")
#     # time.sleep(1)
#     print("complete function"num)


# if __name__ == "__main__":
#     res = []
#     for _ in range(100):
#         p1 = multiprocessing.Process()(target=index, args=[_])
#         p1.start()
#         res.append(p1)

#     for p1 in res:
#         p1.join()

#     finish = time.perf_counter()
#     print(f"finished function {round(finish-start,2)} sec")


