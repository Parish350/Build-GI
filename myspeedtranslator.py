from tkinter import*
import tkinter.messagebox

gui = Tk()
gui.config(background="medium spring green")
gui.title("Text to Speech Converter")
selection=StringVar()
world={'Spanish':'es','French':'fr','Tamil':'ta'}
r1=Radiobutton(gui,text='Spanish',variable=selection,value='es')
r1.place(x = 100 ,y = 100)
r2=Radiobutton(gui,text='French',variable=selection,value='fr')
r2.place(x = 200 ,y = 100)
r3=Radiobutton(gui,text='Tamil',variable=selection,value='ta')
r3.place(x = 300 ,y = 100)
radiobutton = Entry()
radiobutton.place(x = 200 , y = 150)
submit = Button (gui,text ="submit")
submit.place(x = 400, y = 100)
gui.geometry("250x140")
gui.mainloop()
