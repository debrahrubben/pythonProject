from tkinter import *

window = Tk()

photo = PhotoImage(file='logo.png')

label = Label(window,
              text='Hello world',
              font=('Arial',40,'bold',),
              fg='#00FF00',
              relief=RAISED,
              bd=10,
              image=photo,
              compound='bottom'
              )





label.pack()

window.mainloop()