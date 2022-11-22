#!/usr/bin/python3

def get_all_diseases(cursor):
    cursor.execute("SELECT * FROM disease")
    results = cursor.fetchall()
    return results

def get_disease_by_name(cursor, dname):
    query = "SELECT name, description FROM disease WHERE name=%s"
    cursor.execute(query, (dname,))
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

def create_new_patient(cursor, name, age, sex):
    sexStr = str()
    sexStr = "male" if sex == 0 else "female"
    query = "INSERT INTO patient (name, age, sex) VALUES (%s, %s, %s)"
    cursor.execute(query,  (name, age, sexStr,))

def get_patientID_by_name(cursor, name):
    query = "SELECT id FROM patient WHERE name=%s"
    cursor.execute(query, (name,))
    results = cursor.fetchall()
    return results