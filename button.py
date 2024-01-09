from tkinter import *

def click():
    print('you clicked the button')
window = Tk()

Button = Button(window,
                text='click me',
                command=click,
                font=('Comic Sans',30),
                bg='black',
                activeforeground='#00FF00',
                activebackground='black'
              )





Button.pack()

window.mainloop()