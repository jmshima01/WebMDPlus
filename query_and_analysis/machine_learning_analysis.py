# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:24:37 2022

@author: James Shima
"""
#libs:
import getpass 
import pg8000
import secrets
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import warnings
from sklearn.metrics import classification_report
import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix ,classification_report
from sklearn.tree import DecisionTreeClassifier

warnings.simplefilter("ignore")

print("Running...")

#user = input("Username: ")
#secret = getpass.getpass()
db = pg8000.connect(user="jamesshima", password="Snowm@ss", host='codd.mines.edu', port=5433, database='csci403')
cursor = db.cursor()
# Setting search path/role
cursor.execute("SET search_path TO f22_group6")
cursor.execute("SET role TO f22_group6")

# getting unique symptoms:
cursor.execute("SELECT * FROM symptoms")
results = cursor.fetchall()

symptoms = []
for row in results:
    symptoms.append(row[0])


# Random number simulating a fake patient chosing up to 15 diff symptoms:
num_of_symptoms = 5
symptoms_chosen = []
for i in range(num_of_symptoms):
    symptoms_chosen.append(symptoms[secrets.randbelow(len(symptoms)-2)+1])


print(symptoms_chosen)

# finding all diseases that have listed symptoms:
possible_diseases = []
for i in symptoms_chosen:
    query = "SELECT disease_name FROM disease_symptoms WHERE symptom = %s"
    cursor.execute(query,(i,))
    results = cursor.fetchall()
    for row in results:
        possible_diseases.append(row[0])

#print(possible_diseases)


# ========= Analysis using Random Forrest ==============

df = pd.read_csv("learning_data.csv")

df["symptoms"] = 0

records = df.shape[0]
for i in range(records):
    values = df.iloc[i].values
    values = values.tolist()
    if 0 in values:
        df["symptoms"][i] = values[1:values.index(0)]
    else:
        df["symptoms"][i] = values[1:]



column_values = df[['symptom_1', 'symptom_2', 'symptom_3', 'symptom_4',
       'symptom_5', 'symptom_6', 'symptom_7', 'symptom_8', 'symptom_9',
       'symptom_10', 'symptom_11', 'symptom_12']].values.ravel()

symps = pd.unique(column_values)
symps = symps.tolist()
symps = [i for i in symps if str(i) != "nan"]

simp = pd.DataFrame(columns = symps,index = df.index)

simp["symptoms"] = df["symptoms"]

for i in symps:
    simp[i] = simp.apply(lambda x:1 if i in x.symptoms else 0, axis=1)

simp["disease"] = df["disease"]
simp = simp.drop("symptoms",axis=1)

label = simp['disease']

simp = simp.drop("disease",axis=1) # data


# adding weights:
for i,sy in enumerate(symptoms_chosen):
    simp = simp.replace({sy:{1:len(symptoms_chosen)-i}})
    

clf = RandomForestClassifier()

x_train, x_test, y_train, y_test = train_test_split(simp, label)

clf.fit(x_train,y_train)
result = clf.predict(x_test)

prediction = []
s = list(simp.columns.values)
indexes_of_chosen_symps = []

for i,v in enumerate(s):
    for j in symptoms_chosen:
        if v == j:
            indexes_of_chosen_symps.append(i)
            
for i in range(len(s)):
    if i in indexes_of_chosen_symps:
        prediction.append(1)
    else:
        prediction.append(0)
        
print("I think you have...")
print(clf.predict([prediction])[0])
print("Out of...")
print(possible_diseases)
    
