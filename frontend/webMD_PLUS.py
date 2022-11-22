from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as font
from tkinter.ttk import Combobox
import backend.db_conn as db
import backend.db_queries as queries

conn = db.get_conn()
cursor = db.get_cursor(conn)

# Globals
sex = -1
age = -1
first = ""
last = ""
symptomStr = ""
isValidAge = False
isValidName = False

# Window Globals
window=Tk()

symptomsObj = queries.get_all_symptoms(cursor)
symptoms = []

for row in symptomsObj:
    name = row[0]
    symptoms.append(name)

sexVar=IntVar()
sexVar.set(0)

male_radio=Radiobutton(window, text="male", variable=sexVar,value=0)
female_radio=Radiobutton(window, text="female", variable=sexVar,value=1)

firstVar = StringVar()
f_name = Entry(window)

lastVar = StringVar()
l_name = Entry(window)

symptomVar = StringVar()
symptomVar.set("--select a symptom--")
symptoms_dropdown=Combobox(window, values=symptoms, textvariable=symptomVar, width=30, state="readonly")

age_entry = Entry(window)

def validatestring(input):   
    if input.isalpha():
        return True
    else:
        return False

def validateint(input):
    if type(input) == int:
        return True
    else:
        return False

def isValidSymptom():
    return symptomStr != "--select a symptom--"

def isValidInput():
    if not validateint(age):
        messagebox.showerror(title="Invalid Input", message="Please use a number for age")
        return False
    elif not validatestring(first) :
        messagebox.showerror(title="Invalid Input", message="Please enter only letters for first name")
        return False
    elif not validatestring(last):
        messagebox.showerror(title="Invalid Input", message="Please enter only letters for last name")
        return False
    elif not isValidSymptom():
        messagebox.showerror(title="Invalid Input", message="Please select at least one symptom")
        return False
    else:
        return True

def set_sex():
    global sex
    sex = sexVar.get()

def set_age():
    global age
    age = int(age_entry.get())

def set_fname():
    global first
    first = f_name.get()

def set_lname():
    global last
    last = l_name.get()

def set_symptom():
    global symptomStr
    symptomStr = symptomVar.get()

def submitClickEvent():
    set_sex()
    set_age()
    set_fname()
    set_lname()
    set_symptom()

    if isValidInput():
        sx = ""
        if sex == 0:
            sx = "male"
        elif sex == 1:
            sx = "female"
        print("Sex: " + sx)
        print("Age: " + str(age))
        print("First: " + first)
        print("Last: " + last)
        print("Symptoms: " + symptomStr)
    
def run_ui(): 
    window.geometry("1200x800")

    header=Label(window, text="Welcome to WebMD+", font='Arial 17 bold')
    header.place(relx=0.5, rely=0.05, anchor=CENTER)

    patient_info_label = Label(window, text="Patient Info", font='Arial 14 bold')
    patient_info_label.grid(column=0, row=0, padx = 100, pady = (125, 0), sticky=W)

    sex_label = Label(window, text="Sex:")
    sex_label.grid(column=0, row=1, sticky=W, padx = 100, pady = 2)

    male_radio.grid(column=1, row=1, pady = 2, sticky=W)
    female_radio.grid(column=1, row=1, padx = (2, 0), pady = 2)

    Label(window, text="Age:").grid(column=0, row=2, sticky=W, padx = 100, pady = 2)
    age_entry.grid(column=1, row=2, sticky=W)
    age_entry.focus_set()

    Label(window, text="First Name:").grid(column=0, row=3, sticky=W, padx = 100, pady = 2)
    Label(window, text="Last Name:").grid(column=0, row=4, sticky=W, padx = 100, pady = 2)

    f_name.grid(column=1, row=3, sticky=W)
    l_name.grid(column=1, row=4, sticky=W)
    
    symptoms_dropdown_label = Label(window, text="Symptoms")
    symptoms_dropdown_label.grid(column=0, row=5, sticky=W, padx = 100, pady = 2)
    symptoms_dropdown.grid(column=1, row=5, sticky=W)

    isValidName = window.register(validatestring)
    isValidAge = window.register(validateint)

    submit_button = Button(window, text="Submit", command=submitClickEvent)
    submit_button.grid(column=1, row=6, padx = 100, pady = 2, sticky=W)
                    
    #Run UI
    window.mainloop()




# def clicked():

#     res = "Welcome to " + txt.get()

#     lbl.configure(text= res)

# btn = Button(window, text="Click Me", command=clicked)

# btn.grid(column=2, row=0)

