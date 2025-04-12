# for loop

import math
import time

radius = float(input('what is the radius of the circle? '))
area = math.pi * radius ** 2
sec = 3
for x in range(sec, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)
print(f"in 3 seconds, the area of the circle is {area}m*2")
