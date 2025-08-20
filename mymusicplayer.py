from tkinter import*
from tkinter import filedialog
import pygame 
import os
pygame.mixer.init()
playlist = []
index = 0
paused = False
gui = Tk()
gui.config(background="turquoise1")
gui.title("Music Player App")
gui.geometry("250x140")
def load_music():
 global playlist, index
 files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
 if files:
  playlist = list(files)
  index = 0
  title1.config(text=os.path.basename(playlist[index]))

title1 = Label (gui, text = "No songs loaded",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold")) 
title1.place(x = 90 , y = 50)
title2 = Button(gui, text = "Load",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold"), command = load_music) 
title2.place(x = 100 , y = 100)
title3 = Button (gui, text = "Play ▶️",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold")) 
title3.place(x = 100 , y = 200)
title4 = Button (gui, text = "Stop ⏹️",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold")) 
title4.place(x = 100 , y = 300)
title5 = Button(gui, text = "Pervious ⏮️",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold")) 
title5.place(x = 300 , y = 100)
title6 = Button(gui, text = "Pause ⏸️",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold")) 
title6.place(x = 300 , y = 200)
title7 = Button(gui, text = "Next ⏭️",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold")) 
title7.place(x = 300 , y = 300)
title8 = Label(gui, text = "Volume",fg = "purple" ,bg="turquoise1", font = ( "times",28,"bold")) 
title8.place(x = 500 , y = 300)
title9 = Scale(gui, from_=0, to=100,orient="horizontal")
title9.place(x = 500 , y = 350)

gui.mainloop()
