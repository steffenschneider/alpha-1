
"""
This program shows you your reaction time
"""

import time
import random
n_items = 4
duration = 0

print("press Enter if you see the ########################### !")
for i in range(n_items):
    time.sleep(random.randint(3000, 10000)*1.0/1000)
    print("#################################")
    print("#################################")
    print("#################################")
    ts1 = time.time()
    input()
    ts2 = time.time()
    duration += ts2-ts1

print("Your reaction time is " + str(duration/n_items) + " s")
