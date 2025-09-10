from tkinter import*
import tkinter.messagebox

gui = Tk()
gui.config(background="salmon1")
gui.title("JUMBLED QUIZ")
selection=StringVar()
words = ['Wrong','Cold','Bottle']
jumbled = ['Which word is wrong in the dictionary?','What can you catch but not throw?','What has a neck but no head?']
Score = 0
index = 0
def reset():
    global words,Score,jumbled,index
    title1.config(text = jumbled[index])

def Check():
    global words,Score,jumbled,index
    user = Label1.get()
    if user == words[index]:
     tkinter.messagebox.showinfo("Congratualtions","You got the right answer.") 
     Score += 1
    else:
     tkinter.messagebox.showinfo("Sorry","You got the wrong answer,try again.")   
    index += 1
    title4.config(text = f'Score:{Score}')
    reset()


title1 = Label (gui, text = "",fg = "mint cream" ,bg="salmon1", font = ( "times",25,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Button (gui, text = "Check",fg = "green2" ,bg="salmon1", font = ( "times",28,"bold"),command = Check) 
title2.place(x = 100 , y = 300)
title3 = Button (gui, text = "Reset",fg = "yellow" ,bg="salmon1", font = ( "times",28,"bold"), command = reset) 
title3.place(x = 200 , y = 400)
Label1 = Entry()
Label1.place(x = 100 , y = 200)
title4 = Label (gui, text = "Score",fg = "purple" ,bg="salmon1", font = ( "times",28,"bold")) 
title4.place(x = 300 , y = 500)

reset()
gui.geometry("250x140")
gui.mainloop()
