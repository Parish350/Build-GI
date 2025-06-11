from tkinter import*
from time import strftime
gui = Tk()
gui.config(background="cyan")
gui.title("Digital Clock")
gui.geometry("250x140")
def time():
    string = strftime('%H:%M:%S%p')
    IbI.config(text=string)
    IbI.after(1000,time)
IbI = Label(gui, font=('calibri',40,'bold'),background="cyan",foreground="aquamarine2")
IbI.place (x = 100 ,y = 100)
time()
gui.mainloop()
