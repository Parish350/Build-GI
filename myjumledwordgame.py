from tkinter import*
import tkinter.messagebox

gui = Tk()
gui.config(background="dark green")
gui.title("JUMBLED WORD GAME")
selection=StringVar()
title1 = Label (gui, text = "elov",fg = "mint cream" ,bg="dark green", font = ( "times",25,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (gui, text = "Check",fg = "green2" ,bg="dark green", font = ( "times",28,"bold")) 
title2.place(x = 100 , y = 100)
title3 = Label (gui, text = "Reset",fg = "yellow" ,bg="dark green", font = ( "times",28,"bold")) 
title3.place(x = 100 , y = 200)
Label = Entry()
Label.place(x = 100 , y = 150)


gui.geometry("250x140")
gui.mainloop()
