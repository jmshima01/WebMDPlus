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