from tkinter import *
from tkinter import filedialog

def saveFile():
    file =filedialog.asksaveasfile(defaultextension='.txt',
                                   filetypes=[
                                       ('Text file','.txt')])
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()


window = Tk()
button = Button(window,text='Save', command=saveFile)
text = Text(window)
button.pack()
text.pack()
window.mainloop()