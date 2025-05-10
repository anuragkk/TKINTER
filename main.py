from tkinter import *

window = Tk()
window.title("Miles to KM convertor")
window.minsize(height=300, width=500)

input = Entry(width=20)
input.pack()

my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.pack()


def change():
    miles = int(input.get())
    km=miles*1.60934
    my_label.config(text=km)


button = Button(text="calculate", command=change)
button.pack()
window.mainloop()
