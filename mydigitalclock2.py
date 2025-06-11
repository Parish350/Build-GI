from tkinter import*
from time import strftime
gui = Tk()
gui.config(background="springgreen")
gui.title("Digital Clock")
gui.geometry("250x140")
def time():
    string = strftime('%I:%M:%S:%p:%B:%Y')
    IbI.config(text=string)
    IbI.after(1000,time)
IbI = Label(gui, font=('calibri',40,'bold'),background="springgreen",foreground="orange")
IbI.place (x = 100 ,y = 100)
time()
gui.mainloop()
