from tkinter import *

window = Tk()
window.geometry('420x420')
window.title('Bro code first GUI program')

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background='black')

window.mainloop()