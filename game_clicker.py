import subprocess
import time

import f
import mouse_simulation

time.sleep(3)

subprocess.call(["xte", "mousemove 700 350"])
mouse_simulation.click()
time.sleep(.3)

x_start = 600
y_start = 600
subprocess.call(["xte", "mousemove " + str(x_start) + " " + str(y_start)])
mouse_simulation.click()
x_0 = -1
y_0 = -1
n = 1000000
for i in range(n):
    # get distance from origin
    mousepos = f.get_mousepos()
    x = mousepos[0]
    y = mousepos[1]
    # set start position
    if x_0 == -1:
        x_0 = x
        y_0 = y
    dx = x - x_0
    dy = y - y_0
    # interrupt loop if mouse is moved
    if dx > 3 or dy > 3:
        break
    subprocess.call(["xte", "mousemove " + str(x_start) + " " + str(y_start)])
    mouse_simulation.click()
    print(f.percent(i, n))
    time.sleep(.002)
