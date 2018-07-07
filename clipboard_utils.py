from tkinter import *
from functools import partial

def modify(function, r=None):
    if r == None:
        r=Tk()
        r.withdraw()
    string = r.clipboard_get()
    r.clipboard_clear()
    r.clipboard_append(function(string))
    r.update()
    if r == None:
        r.destroy()

def titlecase(r=None):
    modify(lambda string:string.title(), r)

def uppercase(r=None):
    modify(lambda string:string.upper(), r)

def lowercase(r=None):
    modify(lambda string:string.lower(), r)

def capitalize(r=None):
    modify(lambda string:string.capitalize(), r)


def create_GUI():
    tk = Tk()
    
    button_uppercase = Button(tk, text='Upper Case', command = partial(uppercase, r=tk))
    button_uppercase.pack()
    
    button_lowercase = Button(tk, text='Lower Case', command = partial(lowercase, r=tk))
    button_lowercase.pack()

    button_titlecase = Button(tk, text='Title Case', command = partial(titlecase, r=tk))
    button_titlecase.pack()

    button_capitalize = Button(tk, text = 'Capitalize', command = partial(capitalize, r=tk))
    button_capitalize.pack()

    return tk
