# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:36:20 2022

::: 403 Database Management :::
::: Dataset scrubing script :::

@author: James Shima, Michael Maggiore
"""
import csv

unique_lines = set()
file_path = input("Please enter dataset filepath: ")

data = []
final_data = []

# removed encoding='utf-8' from below line
with open(file_path, 'r', encoding='utf-16', errors='ignore') as dataset:
    reader = csv.reader(dataset)
    
    # Cleaning extra spaces and weird inconsistencies:
    for line in reader:
        temp = []
        start = 1
        for string in line:
            if (start == 1):
                no_spaces = string.replace(' ', '_')
                if(no_spaces[-1] == '_'):
                    no_spaces = no_spaces[:len(no_spaces)-1]
                no_spaces = no_spaces.replace('__', '_')
                temp.append(no_spaces.lower())
                start = 0
            else:
                no_spaces = string.replace(' ', '')
                temp.append(no_spaces)
                
        data.append(temp)

    
    # Taking only unique rows:
    for l in data:
        if(l not in final_data):
            final_data.append(l)
    
    # uncomment to see data in terminal:
    # for i in final_data:
    #     print(i)
    
# Writes cleaned data into new file. REMEMBER to change file name below to not overwrite previous file
with open("new_disease_symptom_dataset2.csv", 'w+', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
    print('\n done.')
    
        
    
    
    
    # for i in unique_lines:
    #     print(i)
        
