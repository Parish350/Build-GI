from tkinter import*
import tkinter.messagebox
from gtts import gTTS
from translate import Translator

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
def play():
    translator = Translator(to_lang=selection.get())
    text_to_translate = radiobutton.get()
    translated_text = translator.translate(text_to_translate)
    myobj = gTTS(text=translated_text,lang=selection.get(),slow=False)
    myobj.save("convert.mp3")

submit = Button (gui,text ="submit",command = play)
submit.place(x = 200, y = 250)
gui.geometry("250x140")
gui.mainloop()
