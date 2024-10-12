from tkinter import *
import time

def update_time():
   
    new_time = time.strftime("%I:%M:%S %p")  
    lbl.config(text=new_time)
    clock.after(1000, update_time)  


clock = Tk()
clock.title("Clock")
clock.geometry("600x200") 


lbl = Label(clock, text="", font=("Times New Roman", 80), fg="black")
lbl.pack(pady=20) 

update_time()


clock.mainloop()
