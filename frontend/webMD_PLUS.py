from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from tkinter.ttk import Combobox
import backend.db_conn as db
import backend.db_queries as queries

def run_ui():
    conn = db.get_conn()
    cursor = db.get_cursor(conn)

    symptomsObj = queries.get_all_symptoms(cursor)
    symptoms = []
    for row in symptomsObj:
        name = row[0]
        symptoms.append(name)

    # Create an instance of window
    window=Tk()
    # Set the geometry of the window
    window.geometry("1200x800")
    # Create a frame widget
    frame=Frame(window, width=300, height=300)
    frame.grid(row=0, column=0, sticky="NW")
    # Create a label widget
    header=Label(window, text="Welcome to WebMD+", font='Arial 17 bold')
    header.place(relx=0.5, rely=0.05, anchor=CENTER)

    var = StringVar()
    var.set("one")


    cb=Combobox(window, values=symptoms)
    cb.place(x=60, y=150)

    lb=Listbox(window, height=5, selectmode='multiple')
    for num in symptoms:
        lb.insert(END,num)
    lb.place(x=250, y=150)

    v0=IntVar()
    v0.set(1)
    r1=Radiobutton(window, text="male", variable=v0,value=1)
    r2=Radiobutton(window, text="female", variable=v0,value=2)
    r1.place(x=100,y=50)
    r2.place(x=180, y=50)
                    
    v1 = IntVar()
    v2 = IntVar()
    C1 = Checkbutton(window, text = "Cricket", variable = v1)
    C2 = Checkbutton(window, text = "Tennis", variable = v2)
    C1.place(x=100, y=100)
    #Run UI
    window.mainloop()




# def clicked():

#     res = "Welcome to " + txt.get()

#     lbl.configure(text= res)

# btn = Button(window, text="Click Me", command=clicked)

# btn.grid(column=2, row=0)

