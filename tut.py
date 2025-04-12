# for loop

import time
my_time = int(input("enter the time in seconds: "))
for x in range(my_time ):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)
print("Time is up!")