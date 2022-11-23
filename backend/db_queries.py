#!/usr/bin/python3

def get_all_diseases(cursor):
    cursor.execute("SELECT * FROM disease")
    results = cursor.fetchall()
    return results

def get_all_symptoms(cursor):
    cursor.execute("SELECT * FROM symptoms")
    results = cursor.fetchall()
    return results

def get_all_patients(cursor):
    cursor.execute("SELECT * FROM patient")
    results = cursor.fetchall()
    return results

def get_all_patient_symptoms(cursor):
    cursor.execute("SELECT * FROM patient_symptoms")
    results = cursor.fetchall()
    return results

def get_disease_by_name(cursor, dname):
    query = "SELECT name, description FROM disease WHERE name=%s"
    cursor.execute(query, (dname,))
    results = cursor.fetchall()
    return results

def get_patientID_by_name(cursor, name):
    query = "SELECT id FROM patient WHERE name=%s"
    cursor.execute(query, (name,))
    results = cursor.fetchall()
    return results

def get_medication_by_disease_name(cursor, dname):
    query = "SELECT medication_name FROM medication WHERE disease_name=%s"
    cursor.execute(query, (dname,))
    results = cursor.fetchall()
    return results

def create_new_patient(cursor, name, age, sex):
    sexStr = str()
    sexStr = "male" if sex == 0 else "female"
    query = "INSERT INTO patient (name, age, sex) VALUES (%s, %s, %s)"
    cursor.execute(query,  (name, age, sexStr,))

def insert_patient_symptoms(cursor, pid, symptom):
    query = "INSERT INTO patient_symptoms (patient_id, symptom) VALUES (%s, %s)"
    cursor.execute(query,  (pid, symptom,))

def insert_patient_medications(cursor, pid, medication):
    query = "INSERT INTO patient_medications (patient_id, medication) VALUES (%s, %s)"
    cursor.execute(query,  (pid, medication,))