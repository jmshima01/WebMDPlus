
"""
Created on Thu Nov 10 09:36:20 2022

::: 403 Database Management :::
::: Dataset scrubing script :::

@author: James Shima, Michael Maggiore
"""
import csv

file_path = input("Please enter dataset filepath: ")

nums = ['0','1','2','3','4','5','6','7','8','9']

final_data = []
symptoms = []
meds = []
diseases = []
desc = []
flag = False



# meds:
with open(file_path, 'r') as dataset:
    data = csv.reader(x.replace('\0', '') for x in dataset)
    for line in data:
        medications = []
        i = 0
        for string in line:
            if(i==1):
                disease = string    
            if('"commonMedications":' in string):
                flag = True
                medications.append(disease)
                medications.append(string[21:len(string)-2].replace('"','').replace(':',''))
                
            i+=1
                
            if(flag):
                if(medications not in meds):
                    meds.append(medications)
                flag = False
    print(meds)
    


with open("medication_disease_mapping.csv",'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(["Disease","Medication"])
    for i in range(len(meds)):
        for j in range(1,len(meds[i]),2):
            w.writerow([meds[i][0],meds[i][j]])       
        
    

    














# Disease Map Generated via this:
#     for line in data:
#         symptoms = []
#         i = 0
#         for string in line:
#             if(i==1):
#                 disease = string
            
#             if('"symptoms":' in string and (string[13] not in nums)):
#                 flag = True
#                 symptoms.append(disease)
#                 symptoms.append(string[13:len(string)-2].replace('"',''))
                
#             i+=1
                
#         if(flag):
#             diseases.append(symptoms)
#             flag = False
#     #print(symptoms)
    
    
    
#     print(diseases)
    
    
# with open("symptoms_disease_mapping.csv",'w',newline='') as f:
#     w = csv.writer(f)
#     w.writerow(["Disease","Symptom"])
#     for i in range(len(diseases)):
#         for j in range(1,len(diseases[i]),2):
#             w.writerow([diseases[i][0],diseases[i][j]])
            
    

        
