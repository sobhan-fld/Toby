import os
import time
import sys

x = int(input("How many minutes to shutdown: "))

for remaining in range(x, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} minutes to shutdown.".format(remaining))
    sys.stdout.flush()
    time.sleep(60)

print("\nshuting down\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

os.system("shutdown /s /t 1")