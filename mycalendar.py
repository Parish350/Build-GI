from tkinter import*
import calendar
mai = Tk()
mai.config(background="gray25")
mai.title("Celsius")
mai.geometry("250x150")
def submit_temperature():
    choice = enterthetemperature.get() 
    choice = int(choice)
    #(36°C × 9/5) + 32 = 96.8°F
    text = (choice * 9/5) + 32
    fahrenheit.config(text = f"temperature in fahrenheit:{text}")

title1 = Label (mai, text = "Celsius",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (mai, text = "->Fahrenheit",fg = "gray93" ,bg="gray25", font = ( "times",28,"bold")) 
title2.place(x = 210 , y = 50)
enterthetemperature = Entry ()
enterthetemperature.place(x = 270, y = 180)
convert = Button (mai,text ="convert",bg = "gray93", fg = "gray25", command = submit_temperature)
convert.place(x = 330, y = 210)
temperature = Label (mai,text ="temperature in celsius:",bg = "gray93", fg = "gray25")
temperature.place(x = 100, y = 180)
fahrenheit = Label (mai,text ="temperature in fahrenheit:",bg = "gray93", fg = "gray25")
fahrenheit.place(x = 100, y = 210)
mai.mainloop()
