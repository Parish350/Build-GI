from tkinter import*
import calendar
mai = Tk()
mai.config(background="gray25")
mai.title("CELSIUS")
mai.geometry("250x140")
def submit_temperature():
    mai2 = Tk()
    mai2.config(background="gray25")
    mai2.title("CELSIUS")
    mai2.geometry("250x140")
    choice = temperature.get() 

title1 = Label (mai, text = "CELSIUS",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title1.place(x = 50 , y = 50)
title2 = Label (mai, text = "fahrenheit",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title2.place(x = 100 , y = 100)
enterthetemperature = Entry ()
enterthetemperature.place(x = 200, y = 180)
convert = Button (mai,text ="convert",bg = "gray93", fg = "gray25", command = submit_temperature)
convert.place(x = 150, y = 250)
temperature = Button (mai,text ="temperature",bg = "gray93", fg = "gray25", command = exit)
temperature.place(x = 300, y = 250)
mai.mainloop()
