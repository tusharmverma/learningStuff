# When are we going to use threading
# When you want to speed up your program.
# Its not necessary the speed up will happen

import time
import threading

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping')


t1 = threading.Thread(target=do_something())
t2 = threading.Thread(target=do_something())

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')