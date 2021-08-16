from tkinter import *
# don't have to use tkinter. before everything
window = Tk()

def from_kg():
    gram = float(entry1_str.get()) * 1000
    pound = float(entry1_str.get()) * 2.20462
    ounce = float(entry1_str.get()) * 35.247


    text1.delete("1.0", END)
    text1.insert(END, gram)

    text2.delete("1.0", END)
    text2.insert(END, pound)

    text3.delete("1.0", END)
    text3.insert(END, ounce)


label1 = Label(window, text="Kg")
label1.grid(row=0, column=1)

entry1_str = StringVar()
entry1 = Entry(window, width= 10, textvariable=entry1_str)
entry1.grid(row=0, column=0)

button1 = Button(window, text="Convert", command=from_kg)
button1.grid(row=0, column=2)

text1 = Text(window, height=1, width=10)
text1.grid(row=1, column=0)

text2 = Text(window, height=1, width=10)
text2.grid(row=1, column=1)

text3 = Text(window, height=1, width=10)
text3.grid(row=1, column=2)

window.mainloop() #have to have in order to keep open or else it will instantly close