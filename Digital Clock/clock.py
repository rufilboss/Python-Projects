from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Digital Clock")
window.geometry("200x80")
window.configure(bg="black")
window.resizable(False, False)

clock_label = Label(window, bg="black", fg="green", font=("Times", 30, "bold"), relief="flat")
clock_label.place(x=20, y=20)

def update_label():
    current_time = strftime("%H:%M:%S") 
    clock_label.configure(text=current_time)
    clock_label.after(1000, update_label)

update_label()
window.mainloop()
