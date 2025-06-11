from tkinter import*
import calendar
gui = Tk()
gui.config(background="gray25")
gui.title("Distance Calcuator")
gui.geometry("250x150")
def submit_distance():

    choice = enterthedistance.get() 
    choice = int(choice)
    choice1 = enterthespeed.get()
    choice1 = int(choice1)
    distancetext = choice *choice1
    distance.config(text = f"distance(km) = {distancetext} ")


title1 = Label (gui, text = "Time",fg = "gray93" ,bg ="gray25", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (gui, text = "Speed",fg = "gray93" ,bg ="gray25", font = ( "times",28,"bold")) 
title2.place(x = 210 , y = 50)
enterthedistance = Entry ()
enterthedistance.place(x = 270, y = 180)
enterthespeed = Entry ()
enterthespeed.place(x = 270, y = 210)
calculate = Button (gui,text ="calculate distance",bg = "gray93", fg = "gray25", command = submit_distance)
calculate.place(x = 330, y = 250)
time = Label (gui,text ="Time (hours:)",bg = "gray93", fg = "gray25")
time.place(x = 100, y = 180)

speed = Label (gui,text ="Speed (km/hr:)",bg = "gray93", fg = "gray25")
speed.place(x = 100, y = 210)
distance = Label (gui,text ="Distance (km:)",bg = "gray93", fg = "gray25")
distance.place(x = 100, y = 250)
gui.mainloop()
