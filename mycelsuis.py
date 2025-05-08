from tkinter import*
import calendar
mai = Tk()
mai.config(background="gray25")
mai.title("Celsius")
mai.geometry("250x150")
def submit_temperature():
    mai2 = Tk()
    mai2.config(background="gray25")
    mai2.title("Celsius")
    mai2.geometry("250x150")
    choice = temperature.get() 

title1 = Label (mai, text = "Celsius",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (mai, text = "->Fahrenheit",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title2.place(x = 210 , y = 50)
enterthetemperature = Entry ()
enterthetemperature.place(x = 270, y = 180)
convert = Button (mai,text ="convert",bg = "gray93", fg = "gray25", command = submit_temperature)
convert.place(x = 330, y = 210)
temperature = Button (mai,text ="Enter temperature in celsius:",bg = "gray93", fg = "gray25", command = exit)
temperature.place(x = 100, y = 180)
mai.mainloop()
