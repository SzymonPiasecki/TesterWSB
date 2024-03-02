import os
import subprocess
import time

# subprocess.run(["tracert 8.8.8.8 > tracert_result.txt"])

#time_start = time.time()
#os.system('cmd "(["tracert 8.8.8.8 > tracert_result.txt"])"')
#time_end = time.time()

with open('tracert_result.txt', 'r') as f:
    lines = f.readlines()

count = 0
for i in range(4, len(lines)-2):
    count += 1
    line = lines[i]
    line = line.split()
    print(line[-1])

print (count)
