from time import strftime
from tkinter import Label, Tk

def create_window():
    window = Tk()
    window.title("Digital Clock")
    window.geometry("200x80")
    window.configure(bg="black")
    window.resizable(False, False)
    return window

def create_clock_label(window):
    clock_label = Label(window, bg="black", fg="green", font=("Times", 30, "bold"), relief="flat")
    clock_label.pack(expand=True)
    return clock_label

def update_label(clock_label):
    current_time = strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    clock_label.after(1000, update_label, clock_label)

def main():
    window = create_window()
    clock_label = create_clock_label(window)
    update_label(clock_label)
    window.mainloop()

if __name__ == "__main__":
    main()
