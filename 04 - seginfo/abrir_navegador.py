'''abrir navegador'''
import webbrowser
from tkinter import Tk, Button


def google():
    '''site'''
    webbrowser.open('www.google.com')


root = Tk()
root.title('Abrir Browser')
root.geometry('300x200')
Button(root, text='Google', command=google).pack(pady=20)

root.mainloop()
