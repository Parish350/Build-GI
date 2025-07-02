from tkinter import*
import tkinter.messagebox
root = Tk()
root.config(background="gray25")
root.title("Lists")
root.geometry("250x150")
def submit_list():
    choice = theOption1.get()
    tkinter.messagebox.showinfo("lists","lists sucessfully correct") 
from tkinter.ttk import*



title1 = Label (root, text = "Save") 
title1.place(x = 90 , y = 50)
title2 = Label (root, text = "Delete") 
title2.place(x = 90 , y = 100)
title3 = Label (root, text = "Add") 
title3.place(x = 90 , y = 50)
title4 = Label (root, text = "Open") 
title4.place(x = 90 , y = 100)
theOption1 = StringVar()
options1 = Combobox(root,textvariable = theOption1, width = 20, value = theOption1,fg = "red" ,bg="gray99" )
options1['values'] = ("List1","List2","List3","List4","List5","List6","List7","List8","List9","List10")
options1.place(x = 300 ,y = 180)
theOption2 = IntVar()
options2 = Combobox(root,textvariable = theOption2, width = 20, value = theOption2,fg = "red" ,bg="gray99" )
options2['values'] = tuple(range(11))
options2.place(x = 300 ,y = 210)
combo = Entry(root)
combo.place(x = 210, y = 300)
order = Button (root,text ="order", command = submit_list)
order.place(x = 330, y = 250)
list = Label (root,text ="Select your list")
list.place(x = 100, y = 180)
root.mainloop()
