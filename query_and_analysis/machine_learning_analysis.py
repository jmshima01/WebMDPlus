# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:24:37 2022

@author: James Shima
"""

import getpass 
import pg8000
import secrets
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

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
num_of_symptoms = secrets.randbelow(15)
symptoms_chosen = []
for i in range(num_of_symptoms):
    symptoms_chosen.append(symptoms[secrets.randbelow(len(symptoms)-2)+1])



# finding all diseases that have listed symptoms:
possible_diseases = []
for i in symptoms_chosen:
    query = "SELECT disease_name FROM disease_symptoms WHERE symptom = %s"
    cursor.execute(query,(i,))
    results = cursor.fetchall()
    print('==================')
    for row in results:
        possible_diseases.append(row[0])

#print(possible_diseases)

# ========= Analysis using Random Forrest ==============

df = pd.read_csv("learning_data.csv")
print(df.head())

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


train, test = train_test_split(simp,test_size=0.2)
X_train = train.drop("disease",axis=1)
y_train = train["disease"].copy()
X_test = test.drop("disease",axis=1)
y_test = test["disease"].copy()

clf = RandomForestClassifier()
clf.fit(X_train,y_train)

#cross_val_score(clf,x_train,y_train).mean()


from sklearn import metrics 


y_pred = clf.predict(X_test)
# using metrics module for accuracy calculation
print("ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred))


prediction = []
for i in range(376):
    if i % 2 == 0:
        prediction.append(0)
    else:
        prediction.append(1)

print(clf.predict([prediction]))


# print(data.describe())
# d = pd.get_dummies(data)

# # Remove the labels from the features
# # axis 1 refers to the columns
# labels = np.array(data['disease']) # target

# # Remove the labels from the features
# # axis 1 refers to the columns
# data= data.drop('disease', axis = 1)
# # Saving feature names for later use
# data_cols = list(data.columns)
# # Convert to numpy array
# #data = np.array(data)

# # Split the data into training and testing sets
# train_features, test_features, train_labels, test_labels = train_test_split(data, labels, test_size = 0.25, random_state = 42)

# # Import the model we are using
# clf = RandomForestClassifier(n_estimators = 100) 
# clf.fit(train_features, train_labels);

# predictions = clf.predict(test_features)

# from sklearn import metrics 
# print()
 
# # using metrics module for accuracy calculation
# print("ACCURACY OF THE MODEL: ", metrics.accuracy_score(test_features, predictions))

# #rf_clf = RandomForestClassifier(criterion='entropy')  

        
    
    
    
    


    

