from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title='read this', message='You are a good person remember that')

window = Tk()
button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()