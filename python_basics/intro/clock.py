import time
seconds = 0
minutes = 0
hours = 0
while True:
    time.sleep(1)
    print(hours, ":", minutes, ":", seconds)
    if seconds<59:
        seconds = seconds+1
    else:
        seconds = 0
    if seconds == 0:
        minutes = minutes+1
    if minutes == 60:
        hours = hours + 1
        minutes = 0