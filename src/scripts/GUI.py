#!/usr/bin/env python
# coding: utf-8

# The GUI is Based on OmarQaisi/Part-Of-Speech-Tagger-for-Arabic-Language


from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox
from tkinter import filedialog
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox

from pandas import DataFrame
from Tokenizer import tokenizer
from Postagger import postagger


# main window
root = Tk()
root.geometry('800x800')
root.title('Arabic Part Of Speech Tagger')


fileName = '' #global variable for the selected file
tags = []     #global variable for the generated tags 
flag = False  #global variable for the accuracy button (user handling)
y = []        #global variable for the y-axis values (matplotlib)
result = []   #global variable for the result of the tokenizer 

times = font.Font(family='times', size=12, weight='normal') #the font used for all the buttons

frame1 = Frame(root)
frame1.pack(fill=X)

frame2 = Frame(root)
frame2.pack(fill=X)

frame3 = Frame(root)
frame3.pack(fill=X)

frame4 = Frame(root)
frame4.pack(fill=BOTH)


doc_label = Label(frame1, text="Selected Text:", font=('times', 16, 'normal'))
doc_label.pack(side=LEFT, padx=(20,0),pady=(10,0))

doc = tkscrolled.ScrolledText(frame2, width=60, height=15, wrap='word')
doc.pack(fill=X, padx=(20,20), pady=(4,0))

def browseFiles():
    global result
    global y
    result = []
    y = []
    doc.configure(state='normal')
    doc.delete('1.0', END)
    global fileName 
    fileName = filedialog.askopenfilename(filetypes=(("Corpus Files", ".txt"),("all files","*.*")))
    content = open(fileName,"r",encoding='utf-8').read()
    doc.tag_configure('tag-right', justify='right')
    doc.insert(END, content, 'tag-right')
    doc.configure(state='disabled')
     
browse_button = Button(frame1, width=7, text='Browse', command=browseFiles)
browse_button['font'] = times
browse_button.pack(side=RIGHT, padx=(0,40), pady=(10,0))  




tokenizer_textbox = tkscrolled.ScrolledText(frame4, width=20, height=25, wrap='word')
tokenizer_textbox.pack(fill=Y, side=LEFT, padx=(20,0), pady=(5,10))

def tokenizeTheFile():
    if not fileName:
        messagebox.showerror("Error", "Choose a file first")
    else:
        tokenizer_textbox.configure(state='normal')
        tokenizer_textbox.delete('1.0', END)
        token = tokenizer(fileName)
        global result
        result = token.tokenize()
        tokenizer_textbox.tag_configure('tag-right', justify='right')
        for line in result:
            for word in line:
                tokenizer_textbox.insert(END, word+'\n', 'tag-right')
        tokenizer_textbox.configure(state='disabled')

tokenize_button = Button(frame3, width=10, text='Tokenize', command=tokenizeTheFile)
tokenize_button['font'] = times
tokenize_button.pack(side=LEFT, padx=(50,0), pady=(20,0))






tagger_textbox = tkscrolled.ScrolledText(frame4, width=20, height=25, wrap='word')
tagger_textbox.pack(fill=Y, side=RIGHT, padx=(0,20), pady=(5,10))

def tagWords():
    if not fileName:
        messagebox.showerror("Error", "Choose a file first")
    elif len(result) == 0:
        messagebox.showerror("Error", "Click on the (Tokenizer) button first")
    else:
        global flag
        global tags
        flag = True
        tagger_textbox.configure(state='normal')
        tagger_textbox.delete('1.0', END)
        tagger = postagger(fileName)
        tags, tagsList = tagger.tag()
        tagger_textbox.tag_configure('tag-right', justify='right')
        for tag in tagsList:
            for item in tag.items():
                tagger_textbox.insert(END, str(item)+"\n", 'tag-right')
        tagger_textbox.configure(state='disabled')
        
tag_button = Button(frame3, width=10, text='Tag', command=tagWords)
tag_button['font'] = times
tag_button.pack(side=RIGHT, padx=(0,60), pady=(20,0))



def save_tags():
    if not fileName:
        messagebox.showerror("Error", "Choose a file first")
    else:
        tags, tagsList = postagger(fileName).tag()
        df = DataFrame(tags.items())
        df.to_csv('tags'+'.csv', encoding='utf-8-sig')

tag_button = Button(frame3, width=20, text='Save Tags', command=save_tags)
tag_button['font'] = times
tag_button.pack(side=RIGHT, padx=(0,150), pady=(20,0))



root.mainloop()