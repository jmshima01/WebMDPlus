"""
clean disease_symptoms to get name and desc as an array of arrays
"""
import csv
import pandas as pd
import re

def main():
    # FIND NUMBER OF ROWS
    num_rows = 0
    with open('disease_symptoms.csv', 'r', encoding='utf-16') as input:
        r = csv.reader(input)
        for row in r:
            num_rows+=1

    with open('disease_symptoms.csv',  'r', encoding='utf-16') as file:
        newfile = file.read()
        test = re.sub(r'\[.*?\]', '!', newfile)
        with open('clean_disease_symptoms.csv', 'w', encoding='utf-16') as output:
            output.write(test)
 
    disease_map = [[] for _ in range (num_rows-1)]
    with open('clean_disease_symptoms.csv', 'r', encoding='utf-16') as file:
        r = csv.reader(x.replace('\t', '') for x in file)
        i=0
        for row in r:
            if(i > 0):
                disease_map[i-1].append(row[1])

                new_string = "".join(row) 
                list = new_string.split('!')
                if(list[1]):
                    disease_map[i-1].append(list[1])
                print(disease_map[i-1]) 
            i+=1
         

            
main()
