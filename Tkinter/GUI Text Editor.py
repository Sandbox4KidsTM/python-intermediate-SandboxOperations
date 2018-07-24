# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:06:57 2018

@author: Mitch Labrenz
"""

from tkinter import *
from tkinter.scrolledtext import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

current_dir = 'C:\\Users\\Mitch Labrenz\\Desktop'
current_file = ""

def open_file():
    global current_file, current_dir
    name = askopenfilename()
    file = open(name, 'r')
    current_dir, current_file = name.rsplit('/', 1)
    text.delete(0.0, END)
    text.insert(0.0, file.read())
    file.close()
    
def save_file():
    global current_file, current_dir
    print(current_dir, current_file)
    print("File: ", current_file)
    name = asksaveasfilename(initialdir=current_dir,\
                                 title='Save File As',\
                                 initialfile = current_file,\
                                 filetypes=(("All Files", "*.*"), ("Python Files", "*.py")))
    if name != '':
        file = open(name, 'w+')
        new_text = text.get(0.0, END)
        file.write(new_text)
        file.close()    

def reset_editor():
    global current_file, current_dir
    current_file = ""
    current_dir = 'C:\\Users\\Mitch Labrenz\\Desktop'
    text.delete(0.0, END)
    
root = Tk()
app = Frame(root)

app.pack()

button_frame = Frame(app)
button_frame.pack(side="top", anchor=W)

new_btn = Button(button_frame)
new_btn["text"] = "New"
new_btn["command"] = reset_editor
new_btn.pack(side="left")

save_btn = Button(button_frame)
save_btn["text"] = "Save"
save_btn["command"] = save_file
save_btn.pack(side="left")

open_btn = Button(button_frame)
open_btn["text"] = "Open"
open_btn["command"] = open_file
open_btn.pack(side="left")

text = ScrolledText(app)
text.pack()

app.mainloop()
