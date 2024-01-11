from tkinter import *

def submit():
    inputarea = text.get('1.0',END)
    print(inputarea)


window = Tk()
text = Text(window, bg='tomato', font=('ink free',25), width=20)
button = Button(window,text='submit',command=submit, )
button.pack()
text.pack()
window.mainloop()
