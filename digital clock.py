from tkinter import *
import time 

window = Tk()

window.title("digital clock")
window.geometry("480x240")

Mylabel = Label(window,font=("arial", 40), bg="Green" , fg="white")

Mylabel.pack()
Mylabel2 = Label(window,font=("arial", 40), bg="Green" , fg="white")
Mylabel2.pack()
 
def mytime():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime('%A')
    mytext = hour + ":" + minute +":" + second +" "+ am_pm
    mytext2 = day
    Mylabel.config(text=mytext)
    Mylabel2.config(text=mytext2)
    Mylabel.after(1000, mytime)





mytime()
window.mainloop()