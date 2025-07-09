from tkinter import*
import tkinter.messagebox
root = Tk()
root.config(background="gray25")
root.title("Lists")
root.geometry("250x150")
def add_list():
 item = listinput.get()
 listbox.insert(END,item)
 listinput.delete(0,END)
from tkinter.ttk import*
from tkinter.filedialog import*




def delete_list():
 item = listbox.curselection()
 if item:
  listbox.delete(item)

def saveFile():
 file=asksaveasfile(defaultextension = ".text")
 if file is not None:
  for item in listbox.get(0,END):
   print(item.strip(),file=file)
 listbox.delete(0,END)


title1 = Button (root, text = "Save", command = saveFile) 
title1.place(x = 100 , y = 100)
title2 = Button (root, text = "Delete", command = delete_list) 
title2.place(x = 600 , y = 100)
title3 = Button (root, text = "Add", command = add_list)
title3.place(x = 100 , y = 200)
title4 = Button (root, text = "Open") 
title4.place(x = 600 , y = 200)
listinput = Entry()
listinput.place(x = 300 , y = 150)
frame = Frame(root)
scrollbar = Scrollbar(frame, orient = "vertical")
scrollbar.pack(side = RIGHT, fill = Y)
listbox = Listbox(frame,width = 70, yscrollcommand=scrollbar.set, bg = "red")
listbox.pack(side = LEFT, padx = 5)
scrollbar.config(command = listbox.yview)
frame.place(x = 150, y = 250)






root.mainloop()
