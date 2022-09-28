from curses import window
from time import strftime
from tkinter import Label, Tk, mainloop


#Designing the GUI for the digital clock
window = Tk()
window.title("")
window.geometry("200 * 80")
window.configure(bg = "black")
window.resizable(False, False)

#Labeling
clock_label = Label(window, bg= "white", fg= "green", font= ("Times", 30, "bold"), relief= "flat")
clock_label.place(x = 20, y = 20)


#Writing the func
def update_label():
    current_time = strftime("%H: %M: %S")
    clock_label.configure(text= current_time)
    clock_label.after(80, update_label)


#Calling the func
update_label()
window,mainloop()