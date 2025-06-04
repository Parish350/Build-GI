from tkinter import* 
import random
gui = Tk()
gui.config(background="gold")
gui.title("GAME")
gui.geometry("250x140")

title1 = Label (gui, text = "Rock Paper Scissors ",fg = "SpringGreen2" ,bg="gray99", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Label (gui, text = "Let's start the Game",fg = "SpringGreen2" ,bg="gray99", font = ( "times",28,"bold")) 
title2.place(x = 210 , y = 100)
title3 = Label (gui, text = "Your Options",fg = "SpringGreen2" ,bg="gray99", font = ( "times",25,"bold")) 
title3.place(x = 100 , y = 200)
cs = 0
ps = 0 
options = ["Rock","Paper","Scissors"]

Rock = Button (gui,text ="Rock", width = 15 ,bg = "gray99", fg = "SpringGreen2",command = lambda:game("Rock"))
Rock.place(x = 250, y = 250)
Paper = Button (gui,text ="Paper", width = 15 ,bg = "gray99", fg = "SpringGreen2",command = lambda:game("Paper"))
Paper.place(x = 350, y = 250)
Scissors  = Button (gui,text ="Scissors ", width = 15 ,bg = "gray99", fg = "SpringGreen2",command = lambda:game("Scissors"))
Scissors.place(x = 450, y = 250)

def game(user) :
    global cs,ps,options
    userchoice = user  
    Computer = random.choice(options)
    computerselect.config(text = f"Computer Selected:---{Computer}")
    playerselect.config(text = f"Your Selected:---{userchoice}")   
    if userchoice == Computer:
      title2.config(text = 'draw') 
    elif (userchoice=='Rock' and Computer=='Paper') or (userchoice=='Paper' and Computer=='Scissors') or (userchoice=='Scissors' and Computer=='Rock'):
       title2.config(text = 'computer wins') 
       cs +=1 
    else:
      title2.config(text = 'player wins') 
      ps +=1
    computer.config(text = f"Computer Score {cs}")
    player.config(text = f"Player Score {ps}") 

title4 = Label (gui, text = "Score",fg = "SpringGreen2" ,bg="gray99", font = ( "times",25,"bold")) 
title4.place(x = 100 , y = 250)  
computer = Label (gui, text = "Computer Score",fg = "SpringGreen2" ,bg="gray99", font = ( "times",25,"bold")) 
computer.place(x = 200 , y = 280)  
computerselect = Label (gui, text = "Computer Selected:---",fg = "SpringGreen2" ,bg="gray99", font = ( "times",25,"bold")) 
computerselect.place(x = 600 , y = 280)
player = Label (gui, text = "Player Score",fg = "SpringGreen2" ,bg="gray99", font = ( "times",25,"bold")) 
player.place(x = 200 , y = 380)    
playerselect = Label (gui, text = "Your Selected:---",fg = "SpringGreen2" ,bg="gray99", font = ( "times",25,"bold")) 
playerselect.place(x = 600 , y = 380)  
gui.mainloop()
