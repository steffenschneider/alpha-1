from vpython import *

ball1 = sphere()
ball1.color = (1, .5, 0)

ball2 = sphere()
ball2.color = (1, 1, 0)
ball2.pos = (4, 0, 0)

ball3 = sphere()
ball3.color = (1, 0, 0)
ball3.pos = (-4, 0, 0)

ball4 = sphere()
ball4.color = (0, 0, 1)
ball4.pos = (-8, 0, 0)
ball4.radius = .8

ball5 = sphere()
ball5.color = (0.5, 0.5, 1)
ball5.pos = (0, 4, 0)
ball5.radius = 3

for i in range(1000):
    time.sleep(.02)
    ball1.pos += (math.cos(i), math.sin(i), 0)
