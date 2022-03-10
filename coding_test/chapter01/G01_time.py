import time

start_time = time.time()

for i in range(100000):
    1 == 1

end_time = time.time()


print('time: ', end_time - start_time)