from tkinter import*
gui = Tk()
gui.config(background="gold")
gui.title("GuessingGame")
gui.geometry("250x140")

import tkinter.messagebox
def getname():
 myName = name.get()
 tkinter.messagebox.showinfo("name", 'Well,' + myName + ',I am thinking of a number between 1 and 20.')

title1 = Label (gui, text = "Number Guessing Game",fg = "SpringGreen2" ,bg="gray99", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (gui, text = "What is your name?",fg = "SpringGreen2" ,bg="gray99", font = ( "times",28,"bold")) 
title2.place(x = 210 , y = 150)
name = Entry(gui)
name.place(x = 210, y = 200)
title3 = Label (gui, text = "Take a guess",fg = "SpringGreen2" ,bg="gray99", font = ( "times",25,"bold")) 
title3.place(x = 100 , y = 300)

ok = Button (gui,text ="ok", width = 15 ,bg = "gray99", fg = "SpringGreen2" , command = getname)
ok.place(x = 400, y = 200)
guess = Button (gui,text ="guess", width = 15 ,bg = "gray99", fg = "SpringGreen2")
guess.place(x = 550, y = 300)
number = Entry(gui)
number.place(x = 300, y = 330)

exit = Button (gui,text ="exit", width = 15 ,bg = "gray99", fg = "SpringGreen2" , command = exit)
exit.place(x = 400, y = 250)

gui.mainloop()
