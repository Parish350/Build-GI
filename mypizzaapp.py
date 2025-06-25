from tkinter import*
import calendar
mai = Tk()
mai.config(background="gray25")
mai.title("Pizza")
mai.geometry("250x150")
def submit_pizza():
    choice = enterthepizza.get() 
    choice = int(choice)

title1 = Label (mai, text = "Welcome to",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (mai, text = "Pizza Hut",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title2.place(x = 90 , y = 100)
enterthepizza = Entry ()
enterthepizza.place(x = 270, y = 180)
order = Button (mai,text ="order",bg = "gray93", fg = "gray25", command = submit_pizza)
order.place(x = 330, y = 210)
favourite = Label (mai,text ="Select your fav pizza",bg = "gray93", fg = "gray25")
favourite.place(x = 100, y = 180)
quanity = Label (mai,text ="Select the qty of your pizza",bg = "gray93", fg = "gray25")
quanity.place(x = 100, y = 210)
mai.mainloop()
