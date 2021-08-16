import time     #builtin library (written in C) (in sys)
import os       #standard library (written in Python)
import pandas   #third-party library [package] (written in Python)

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(2)

print("how are you mane")