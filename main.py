from tkinter import *
import tkinter.messagebox as MessageBox
import os
import webbrowser
import random

import config
import animals
import write_xml
import taxonomy_xml

str_about_info = config.str_about_info
str_hello = random.choice(config.str_hello)

# Window
window = Tk()

window.title("ZT2 Classification Editor")
window.geometry("608x386+300+120")
window.resizable(False, True)
 #Var

idx_class = 0
idx_order = 0
idx_family = 0
idx_genus = 0
idx_species = 0

result_classification = []

#Image
image_1 = PhotoImage(file = r".\assets\favicon_zt2library.png")
image_2 = PhotoImage(file = r".\assets\favicon_wiki.png")
image_3 = PhotoImage(file = r".\assets\quill_RoundIcons.png")
image_4 = PhotoImage(file = r".\assets\favicon_github.png")


#Icon
window.iconphoto(False, image_3)

#Class Label
label_classification = Label(window, text=str_hello, justify=CENTER, height=5, anchor=CENTER)
label_classification.pack()

 #List
list_class, list_order, list_family, list_genus, list_species = animals.get_list()

# ListFrame
listframe = Frame(window)
listframe.pack(expand=True, fill=Y)

# Listbox
lb1 = Listbox(listframe, height=8)

for item in list_class:
    lb1.insert(END, item.get('name'))

lb1.pack(side=LEFT, expand=True, fill=Y)

lb2 = Listbox(listframe, height=8)
lb2.pack(side=LEFT, expand=True, fill=Y)

lb3 = Listbox(listframe, height=8)
lb3.pack(side=LEFT, expand=True, fill=Y)

lb4 = Listbox(listframe, height=4)
lb4.pack(side=TOP, expand=True, fill=Y)

lb5 = Listbox(listframe, height=4)
lb5.pack(side=TOP, expand=True, fill=Y)

def lb1_event(event):
    global idx_class
    
    for item in lb1.curselection():
        clear_list(0)
        idx_class = item
        label_text()
        for i in list_order[idx_class]:
            lb2.insert(END, i.get('name'))
            
        output_classification()
        enable_test_button()

def lb2_event(event):
    global idx_class
    global idx_order
    
    for item in lb2.curselection():
        clear_list(1)
        idx_order = item
        label_text()
        for i in list_family[idx_class][idx_order]:
            lb3.insert(END, i.get('name'))
            
        output_classification()
        enable_test_button()

def lb3_event(event):
    global idx_class
    global idx_order
    global idx_family
    
    for item in lb3.curselection():
        clear_list(2)
        idx_family = item
        label_text()
        for i in list_genus[idx_class][idx_order][idx_family]:
            lb4.insert(END, i.get('name'))            
               
        output_classification()
        enable_test_button()

def lb4_event(event):
    global idx_class
    global idx_order
    global idx_family
    global idx_genus
    
    for item in lb4.curselection():
        clear_list(3)
        idx_genus = item
        label_text()
        for i in list_species[idx_class][idx_order][idx_family][idx_genus]:
            lb5.insert(END, i.get('name'))
            
        output_classification()
        enable_test_button()

def lb5_event(event):
    global idx_class
    global idx_order
    global idx_family
    global idx_genus
    global idx_species
    
    for item in lb5.curselection():

        idx_species = item
        label_text()
            
        output_classification()
        enable_test_button()

def output_classification():
    global result_classification
    
    if len(lb1.curselection()) > 0 :
        result_classification = [list_class[idx_class]]
    elif len(lb2.curselection()) > 0 :
        result_classification = [list_class[idx_class], list_order[idx_class][idx_order]]
    elif len(lb3.curselection()) > 0 :
        result_classification = [list_class[idx_class], list_order[idx_class][idx_order], list_family[idx_class][idx_order][idx_family]]
    elif len(lb4.curselection()) > 0 :
        result_classification = [list_class[idx_class], list_order[idx_class][idx_order], list_family[idx_class][idx_order][idx_family], list_genus[idx_class][idx_order][idx_family][idx_genus]]
    elif len(lb5.curselection()) > 0 :
        result_classification = [list_class[idx_class], list_order[idx_class][idx_order], list_family[idx_class][idx_order][idx_family], list_genus[idx_class][idx_order][idx_family][idx_genus], list_species[idx_class][idx_order][idx_family][idx_genus][idx_species]]
    else:
        result_classification = []
    print('rcf len =', len(result_classification))

def enable_test_button():

    #button2
    if len(write_xml.xml_trees) > 0 :
        if len(lb1.curselection()) > 0 and lb2.size() == 0 :
            button2.config(state=NORMAL)
        elif len(lb2.curselection()) > 0 and lb3.size() == 0 :
            button2.config(state=NORMAL)
        elif len(lb3.curselection()) > 0 and lb4.size() == 0 :
            button2.config(state=NORMAL)
        elif len(lb4.curselection()) > 0 and lb5.size() == 0 :
            button2.config(state=NORMAL)
        elif len(lb5.curselection()) > 0 :
            button2.config(state=NORMAL)
        else:
            button2.config(state=DISABLED)
    else:
        button2.config(state=DISABLED)
        
    #button6
    # if result_classification != [] :
        # if result_classification[-1].get('wiki') != None and result_classification[-1].get('wiki') != '' :
            # button6.config(state=NORMAL)
        # else:
            # button6.config(state=DISABLED)
    # else:
        # button6.config(state=DISABLED)
        
            

def label_text():
    mytext = ['','','','','']
    if lb1.size() > 0 :
        mytext[0] = 'Class: '+list_class[idx_class].get('name')
    if lb2.size() > 0 :
        mytext[1] = '\nOrder: '+list_order[idx_class][idx_order].get('name')
    else:        
        mytext[1] = '\n'
    if lb3.size() > 0 :
        mytext[2] = '\nFamily: '+list_family[idx_class][idx_order][idx_family].get('name')
    else:        
        mytext[2] = '\n'
    if lb4.size() > 0 :
        mytext[3] = '\nGenus: '+list_genus[idx_class][idx_order][idx_family][idx_genus].get('name')
    if lb5.size() > 0 :
        mytext[4] = '\nSpecies: '+list_species[idx_class][idx_order][idx_family][idx_genus][idx_species].get('name')
    label_classification.config(text = "".join([mytext[0], mytext[1], mytext[2], mytext[3], mytext[4]]))
    
def clear_list(args):
    names = globals()
    for i in range(5):
        if i > args :
            names['lb'+str(i+1)].delete(0,END)

# Buttons and Frames
bt_frame = Frame(window)
bt_frame.pack(side=BOTTOM, ipady=25)

bt_frame1 = Frame(bt_frame)
bt_frame1.pack(side=LEFT)

bt_frame2 = Frame(bt_frame)
bt_frame2.pack(side=LEFT, padx=68)

bt_frame3 = Frame(bt_frame)
bt_frame3.pack(side=LEFT, ipadx=32, ipady=15)

button3 = Button(bt_frame1, text="Get Taxonomy XML", command=lambda: taxonomy_xml.get_taxonomy_xml(result_classification))
button3.pack(side=TOP, anchor=N)

bt_frame1_1 = Frame(bt_frame1)
bt_frame1_1.pack(side=TOP, expand=True, fill=X)

button7 = Button(bt_frame1_1, text="", image=image_4, compound = LEFT, command=lambda: webbrowser.open('https://github.com/Summjoke'))
button7.pack(side=LEFT, anchor=W, ipadx=4, ipady=4)

button4 = Button(bt_frame1_1, text="?", command=lambda: MessageBox.showinfo(title="Instruction", message=str_about_info))
button4.pack(side=LEFT, anchor=W)

button1 = Button(bt_frame2, text="Select Animal XMLs", command=lambda: [write_xml.get_xmls(), enable_test_button()])
button1.pack(side=TOP, expand=True, fill=X)

button2 = Button(bt_frame2, text="Modify Types and Save", command=lambda: write_xml.edit_xml([write_xml.xml_trees, result_classification]))
button2.config(state=DISABLED)
button2.pack(side=TOP)

button5 = Button(bt_frame3, text="", image=image_2, compound = LEFT, command=lambda: taxonomy_xml.open_wiki(['Wikipedia', result_classification]))
button5.pack(side=LEFT, anchor=N, ipadx=4, ipady=4)

button6 = Button(bt_frame3, text="", image=image_1, compound = LEFT, command=lambda: taxonomy_xml.open_wiki(['ZT2Library', result_classification]))
button6.pack(side=LEFT, anchor=N, ipadx=4, ipady=4)


lb1.bind('<<ListboxSelect>>', lb1_event)
lb2.bind('<<ListboxSelect>>', lb2_event)
lb3.bind('<<ListboxSelect>>', lb3_event)
lb4.bind('<<ListboxSelect>>', lb4_event)
lb5.bind('<<ListboxSelect>>', lb5_event)


window.mainloop()