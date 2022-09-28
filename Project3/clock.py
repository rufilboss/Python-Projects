from curses import window
from time import strftime
from tkinter import Label, Tk


#Designing the GUI for the digital clock
window = Tk()
window.title("")
window.geometry("200 * 80")
window.configure(bg = "black")
window.resizable(False, False)