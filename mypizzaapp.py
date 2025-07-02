from tkinter import*
import tkinter.messagebox
mai = Tk()
mai.config(background="gray25")
mai.title("Pizza")
mai.geometry("250x150")
def submit_pizza():
    choice = theNum1.get()
    tkinter.messagebox.showinfo("order","order sucessfully placed") 
from tkinter.ttk import*



title1 = Label (mai, text = "Welcome to") 
title1.place(x = 90 , y = 50)
title2 = Label (mai, text = "Pizza Hut") 
title2.place(x = 90 , y = 100)
theNum1 = StringVar()
numbers1 = Combobox(mai,textvariable = theNum1, width = 20, value = theNum1 )
numbers1['values'] = ("Chicago Style","Brick Oven Pizza","Italian Pizza","Neapolitan Pizza","California Pizza","New York Style Pizza","Sicilian Pizza","Greek Pizza")
numbers1.place(x = 300 ,y = 180)
theNum2 = IntVar()
numbers2 = Combobox(mai,textvariable = theNum2, width = 20, value = theNum2 )
numbers2['values'] = tuple(range(10))
numbers2.place(x = 300 ,y = 210)
order = Button (mai,text ="order", command = submit_pizza)
order.place(x = 330, y = 250)
favourite = Label (mai,text ="Select your fav pizza")
favourite.place(x = 100, y = 180)
quanity = Label (mai,text ="Select the qty of your pizza")
quanity.place(x = 100, y = 210)
mai.mainloop()
