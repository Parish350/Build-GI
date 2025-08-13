from tkinter import*
import tkinter.messagebox

gui = Tk()
gui.config(background="dark green")
gui.title("JUMBLED WORD GAME")
selection=StringVar()
words = ['Banana','Orange','Strawberries']
jumbled = ['nabnaa','engroa','bwerstraresi']
Count = 0
def reset():
    global words,Count,jumbled
    title1.config(text = jumbled[Count])
def Check():
    global words,Count,jumbled
    user = Label.get()
    if user == words[Count]:
     tkinter.messagebox.showinfo("Congratlations","You got the right answer.") 
    else:
     tkinter.messagebox.showinfo("Sorry","You got the wrong answer,try again.")   
    Count += 1
    reset()

title1 = Label (gui, text = "",fg = "mint cream" ,bg="dark green", font = ( "times",25,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Button (gui, text = "Check",fg = "green2" ,bg="dark green", font = ( "times",28,"bold"),command = Check) 
title2.place(x = 100 , y = 150)
title3 = Button (gui, text = "Reset",fg = "yellow" ,bg="dark green", font = ( "times",28,"bold"), command = reset) 
title3.place(x = 100 , y = 250)
Label = Entry()
Label.place(x = 100 , y = 100)

reset()
gui.geometry("250x140")
gui.mainloop()
