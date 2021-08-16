def mean(value):
    if isinstance(value, dict):
        average = sum(value.values()) / len(value)
    else:
        average = sum(value) / len(value)
    return average
student_grades = {"Jonson": 91, "Terry": 88, "Sims": 75}
print(mean(student_grades))




monday_temperatures = [9.1, 8.8, 7.6]
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
user_input = input("Enter something: ")
print(type(user_input))





phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print(f"{key}: {value}")



username = ''
while username != 'pypy':
    username = input('Enter username: ')




def sentence_maker(phrase):
    inters = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(inters):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
results = []
while True:
    user_input = input("Enter something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))
print(" ".join(results))




temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps)




def mean(**kwargs):
    return kwargs
print(mean(a=1, b=4, c=5))




with open("files/vegetables.txt", "a+") as myFile:
    myFile.write("\nApple")
    myFile.seek(0)
    content = myFile.read()
print(content)



import sys
print(sys.builtin_module_names_)
import time
import os
 #time. is a module of sys but you have to import time if you want the time methods






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
