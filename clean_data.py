
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




with open(file_path, 'r') as dataset:
    data = csv.reader(x.replace('\0', '') for x in dataset)
    
    for line in data:
        symptoms = []
        i = 0
        for string in line:
            if(i==1):
                disease = string
            
            if('"symptoms":' in string and (string[13] not in nums)):
                flag = True
                symptoms.append(disease)
                symptoms.append(string[13:len(string)-2].replace('"',''))
                
            i+=1
                
        if(flag):
            diseases.append(symptoms)
            flag = False
    #print(symptoms)
    
    
    
    print(diseases)
    
    
with open("symptoms_disease_mapping.csv",'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(["Disease","Symptom"])
    for i in range(len(diseases)):
        for j in range(1,len(diseases[i]),2):
            w.writerow([diseases[i][0],diseases[i][j]])
            
    

# with open("symptoms_cleaned.csv", 'w', newline='') as f:
#     w = csv.writer(f)
#     w.writerow(['Symptoms'])
#     for i in symptoms:
#         w.writerow([i])
    
#     print('\ndone')
    
    # Cleaning extra spaces and weird inconsistencies:
#     for line in reader:
#         temp = []
#         start = 1
#         for string in line:
#             if (start == 1):
#                 no_spaces = string.replace(' ', '_')
#                 if(no_spaces[-1] == '_'):
#                     no_spaces = no_spaces[:len(no_spaces)-1]
#                 no_spaces = no_spaces.replace('__', '_')
#                 temp.append(no_spaces.lower())
#                 start = 0
#             else:
#                 no_spaces = string.replace(' ', '')
#                 temp.append(no_spaces)
            
                
#         data.append(temp)
        

    
#     # Taking only unique rows:
#     for l in data:
#         if(l not in final_data):
#             final_data.append(l)
    
#     # uncomment to see data in terminal:
#     # for i in final_data:
#     #     print(i)

# Writes cleaned data into new file. REMEMBER to change file name below to not overwrite previous file
with open("new_disease_symptom_dataset2.csv", 'w+', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
    print('\n done.')
# with open("symptoms_to_disease_dataset.csv", 'w+', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(final_data)
#     print('\n done.')
    
        
    
    
    
#     # for i in unique_lines:
#     #     print(i)
        
