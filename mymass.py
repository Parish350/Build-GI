from tkinter import*
import calendar
mai = Tk()
mai.config(background="gray25")
mai.title("Mass")
mai.geometry("250x150")
def submit_grams():
    choice = enterthegrams.get() 
    choice = float(choice)
    #(1/453.6) + 32 = 0.00220462
    text = (choice * 1/453.6) 
    pound.config(text = f"grams in pounds:{text}")

title1 = Label (mai, text = "Mass",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (mai, text = "Grams",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title2.place(x = 210 , y = 50)
enterthegrams = Entry ()
enterthegrams.place(x = 270, y = 180)
convert = Button (mai,text ="convert",bg = "gray93", fg = "gray25", command = submit_grams)
convert.place(x = 330, y = 210)
grams = Label (mai,text ="grams in kilograms:",bg = "gray93", fg = "gray25")
grams.place(x = 100, y = 180)
pound = Label (mai,text ="grams in pounds:",bg = "gray93", fg = "gray25")
pound.place(x = 100, y = 210)
mai.mainloop()
