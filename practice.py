from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


def click():
    new_text = input.get()
    my_label.config(text=new_text)
    print(f"changed text to {new_text}")


def click_2():
    my_label.config("text=2nd button is clicked")


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label.config(pady=20,padx=20)

input = Entry(width=25)
input.grid(row=2, column=2)

button = Button(text="Click_me", command=click)
button.grid(row=1, column=1)

new_button = Button(text="What?", command=click_2)
new_button.grid(row=3,column=3)
window.mainloop()
