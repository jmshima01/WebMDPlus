
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
proc =[]
proc_final = []
symptoms = []
meds = []
dis = []
desc = []
flag = False


# with open(file_path,'r')as f:
#     r = csv.reader(f)
#     for i in r:
#         print(i)

#diseases
big_lis = []
big_lis.append(['Disease','Desciption'])

with open(file_path, 'r') as dataset:
    data = csv.reader(x.replace('\0', '') for x in dataset)    
    for line in data:
        dis = []
        for i,string in enumerate(line):
            if(i!=0):  
                if('"symptoms":' in line[i-1]) and ('"symptoms":' not in string):
                    dis.append(line[1])
                    if("We will add more content to this page if enough people like you show interest." in string):
                        dis.append("None")
                    else:
                        dis.append(string.replace('\t', '').replace("   ", ' ').replace("  "," "))
                    
                    big_lis.append(dis)
    print(big_lis)
    
with open("disease_table.csv", 'w',newline='') as f:
    w = csv.writer(f)
    w.writerows(big_lis)
    print('\ndone')
            
            
                
                
                
            
                
    
    
    
    
    # for line in data:
    #     proc = []
    #     i = 0
    #     for string in line:
    #         if(i==1):
    #             disease = string    
    #         if('"commonTestsAndProcedures":' in string):
    #             flag = True
    #             proc.append(disease)
    #             proc.append(string[27:len(string)-2].replace('"','').replace(':',''))
                
    #         i+=1
                
    #         if(flag):
    #             if(proc not in proc_final):
    #                 proc_final.append(proc)
    #             flag = False
    # print(proc_final)
    


with open("commonTests_disease_mapping.csv",'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(["Disease","CommonTestAndProcedure"])
    for i in range(len(proc_final)):
        for j in range(1,len(proc_final[i]),2):
            w.writerow([proc_final[i][0],proc_final[i][j]])       
        
    









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
            
    

        
