import subprocess
import time

import f
import mouse_simulation

# os.system("watch xdotool getmouselocation")

time.sleep(3)

n = 500
for i in range(n):
    subprocess.call(["xte", "mousemove 400 400"])
    # os.system("xte 'mousemove 900 460'")
    mouse_simulation.click()
    print(f.percent(i, n))
    time.sleep(.01)
