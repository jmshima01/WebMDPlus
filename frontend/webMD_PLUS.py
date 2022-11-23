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
symptomStr_1 = ""
symptomStr_2 = ""
symptomStr_3 = ""
symptomStr_4 = ""
symptomStr_5 = ""
isValidAge = False
isValidName = False
patient_symptoms = []

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

symptomVar_1 = StringVar()
symptomVar_1.set("--select a symptom--")
symptomVar_2 = StringVar()
symptomVar_2.set("--select a symptom--")
symptomVar_3 = StringVar()
symptomVar_3.set("--select a symptom--")
symptomVar_4 = StringVar()
symptomVar_4.set("--select a symptom--")
symptomVar_5 = StringVar()
symptomVar_5.set("--select a symptom--")

symptoms_dropdown_1=Combobox(window, values=symptoms, textvariable=symptomVar_1, width=30, state="readonly")
symptoms_dropdown_2=Combobox(window, values=symptoms, textvariable=symptomVar_2, width=30, state="readonly")
symptoms_dropdown_3=Combobox(window, values=symptoms, textvariable=symptomVar_3, width=30, state="readonly")
symptoms_dropdown_4=Combobox(window, values=symptoms, textvariable=symptomVar_4, width=30, state="readonly")
symptoms_dropdown_5=Combobox(window, values=symptoms, textvariable=symptomVar_5, width=30, state="readonly")

ageVar = IntVar()
age_entry = Entry(window, )

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
    return symptomStr_1 != "--select a symptom--"

def isValidInput():
    if not validateint(ageVar):
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
    global ageVar
    ageVar = int(age_entry.get())

def set_fname():
    global first
    first = f_name.get()

def set_lname():
    global last
    last = l_name.get()

def set_symptoms():
    global symptomStr_1
    global symptomStr_2
    global symptomStr_3
    global symptomStr_4
    global symptomStr_5

    symptomStr_1 = symptomVar_1.get()
    symptomStr_2 = symptomVar_2.get()
    symptomStr_3 = symptomVar_3.get()
    symptomStr_4 = symptomVar_4.get()
    symptomStr_5 = symptomVar_5.get()

    patient_symptoms.append(symptomStr_1)
    patient_symptoms.append(symptomStr_2)
    patient_symptoms.append(symptomStr_3)
    patient_symptoms.append(symptomStr_4)
    patient_symptoms.append(symptomStr_5)

def set_input_vars():
    set_sex()
    set_age()
    set_fname()
    set_lname()
    set_symptoms()

def build_symptoms_list():
    symptoms_list = []
    global patient_symptoms
    for sym in patient_symptoms:
        if sym != "--select a symptom--":
            symptoms_list.append(sym)
    return symptoms_list

def submitClickEvent():
    set_input_vars()

    if isValidInput():
        print("Sex: " + str(sex))
        print("Age: " + str(ageVar))
        print("First: " + first)
        print("Last: " + last)
        print("Symptoms: " + symptomStr_1)

        symptoms_list = build_symptoms_list()

        full_name = first + " " + last

        queries.create_new_patient(cursor, full_name, ageVar, sex)
        conn.commit()
        print(queries.get_patientID_by_name(cursor, full_name))
        for sym in symptoms_list:
            print(sym)

    
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
    
    symptoms_dropdown_label_1 = Label(window, text="Symptom 1:")
    symptoms_dropdown_label_1.grid(column=0, row=5, sticky=W, padx = 100, pady = 2)
    symptoms_dropdown_1.grid(column=1, row=5, sticky=W)

    symptoms_dropdown_label_2 = Label(window, text="Symptom 2:")
    symptoms_dropdown_label_2.grid(column=0, row=6, sticky=W, padx = 100, pady = 2)
    symptoms_dropdown_2.grid(column=1, row=6, sticky=W)

    symptoms_dropdown_label_3 = Label(window, text="Symptom 3:")
    symptoms_dropdown_label_3.grid(column=0, row=7, sticky=W, padx = 100, pady = 2)
    symptoms_dropdown_3.grid(column=1, row=7, sticky=W)

    symptoms_dropdown_label_4 = Label(window, text="Symptom 4:")
    symptoms_dropdown_label_4.grid(column=0, row=8, sticky=W, padx = 100, pady = 2)
    symptoms_dropdown_4.grid(column=1, row=8, sticky=W)

    symptoms_dropdown_label_5 = Label(window, text="Symptom 5:")
    symptoms_dropdown_label_5.grid(column=0, row=9, sticky=W, padx = 100, pady = 2)
    symptoms_dropdown_5.grid(column=1, row=9, sticky=W)





    submit_button = Button(window, text="Submit", command=submitClickEvent)
    submit_button.grid(column=1, row=10, padx = 100, pady = 2, sticky=W)
                    
    #Run UI
    window.mainloop()


