from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root = Tk()
def new():
    global file
    root.title("Untitled - Notepad")
    file=None
    textarea.delete(1.0,END)
def Open():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file=None
        else:
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")
def about():
    msg.showinfo("About","Microsoft Windows 10")
root.title("Notepad")
root.geometry("700x400")
root.wm_iconbitmap("Hopstarter-Sleek-Xp-Software-Notepad.ico")
file = None
textarea = Text(font="lucida 17 bold")
textarea.pack(fill=BOTH,expand=True)
scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=BOTH)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)
men = Menu()
submen1 = Menu(men,tearoff=0)
submen2 = Menu(men,tearoff=0)
submen3 = Menu(men,tearoff=0)
submen1.add_command(label="New",command=new)
submen1.add_command(label="Open",command=Open)
submen1.add_command(label="Save",command=save)
submen1.add_separator()
submen1.add_command(label="Exit",command=quit)
men.add_cascade(label="File",menu=submen1)
submen2.add_command(label="Cut",command=cut)
submen2.add_command(label="Copy",command=copy)
submen2.add_command(label="Paste",command=paste)
men.add_cascade(label="Edit",menu=submen2)
submen3.add_command(label="About Notepad",command=about)
men.add_cascade(label="Help",menu=submen3)
root.config(menu=men)
root.mainloop()
