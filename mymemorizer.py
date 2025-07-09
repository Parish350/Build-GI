from tkinter import*
import tkinter.messagebox
root = Tk()
root.config(background="lightcyan")
root.title("Memorizer")
root.geometry("250x150")
def add_memorizer():
 item = memorizerinput.get()
 memorizerbox.insert(END,item)
 memorizerinput.delete(0,END)
from tkinter.ttk import*
from tkinter.filedialog import*




def delete_memorizer():
 item = memorizerbox.curselection()
 if item:
  memorizerbox.delete(item)

def saveFile():
 file=asksaveasfile(defaultextension = ".text")
 if file is not None:
  for item in memorizerbox.get(0,END):
   print(item.strip(),file=file)
 memorizerbox.delete(0,END)


title1 = Button (root, text = "Save", command = saveFile) 
title1.place(x = 100 , y = 100)
title2 = Button (root, text = "Delete", command = delete_memorizer) 
title2.place(x = 600 , y = 100)
title3 = Button (root, text = "Add", command = add_memorizer)
title3.place(x = 100 , y = 200)
title4 = Button (root, text = "Open") 
title4.place(x = 600 , y = 200)
memorizerinput = Entry()
memorizerinput.place(x = 300 , y = 150)
frame = Frame(root)
scrollbar = Scrollbar(frame, orient = "vertical")
scrollbar.pack(side = RIGHT, fill = Y)
memorizerbox = Listbox(frame,width = 70, yscrollcommand=scrollbar.set, bg = "deep pink")
memorizerbox.pack(side = LEFT, padx = 5)
scrollbar.config(command = memorizerbox.yview)
frame.place(x = 150, y = 250)






root.mainloop()
