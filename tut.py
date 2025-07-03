import time

def count(start, end):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Counting complete!")
count(0, 10)