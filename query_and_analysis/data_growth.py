import math
import pg8000
import numpy as np
def main():
    #connection
    db = pg8000.connect(user="jlovelace", password="cuddlybear", host='codd.mines.edu', port=5433, database='csci403')
    cursor = db.cursor()

    #search path
    cursor.execute("SET search_path TO f22_group6")
    cursor.execute("SET role TO f22_group6")

    #string data type overhead
    avg_data_type_size_array = []
    total_growth = []
    current_size = 0

    #projected monthly row growth
    disease_growth_month = 1
    symptom_growth_month = 0
    medication_growth_month = 5
    patient_growth_month = 50
    test_procedure_growth_month = 5



##################
#### disease #####
##################
    num_int_fields = 0
    num_text_fields = 2

    #overhead for strings
    cursor.execute("SELECT CEIL(AVG(pg_column_size(name))) FROM disease")
    name_avg_data_type_size = int(cursor.fetchone().pop())
    cursor.execute("SELECT CEIL(AVG( pg_column_size(description))) FROM disease")
    description_avg_data_type_size = int(cursor.fetchone().pop())
    avg_data_type_size_array.append(name_avg_data_type_size)
    avg_data_type_size_array.append(description_avg_data_type_size)
    
    #overhead w/ strings & normal
    print("[disease] ", end="")
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM disease")
    num_rows = int(cursor.fetchone().pop())
    now = table_size_in_pages(num_rows, rows_per_page)

    #growth in ten years
    ltr = table_size_in_pages_ten_years(rows_per_page, num_rows, disease_growth_month)
    total_growth.append(ltr-now)
    current_size+=now

    
########################
### disease_symptoms ###
########################
    num_int_fields = 0
    num_text_fields = 2
    avg_data_type_size_array.clear()

    #overhead for strings
    cursor.execute("SELECT CEIL(AVG(pg_column_size(disease_name))) FROM disease_symptoms")
    disease_name_avg_data_type_size = int(cursor.fetchone().pop())
    cursor.execute("SELECT CEIL(AVG( pg_column_size(symptom))) FROM disease_symptoms")
    symptom_avg_data_type_size = int(cursor.fetchone().pop())
    avg_data_type_size_array.append(disease_name_avg_data_type_size)
    avg_data_type_size_array.append(symptom_avg_data_type_size)
    
    #overhead w/ strings & normal
    print("\n[disease_symptoms] ", end='')
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM disease_symptoms")
    num_rows = int(cursor.fetchone().pop())
    now = table_size_in_pages(num_rows, rows_per_page)

    #growth size in pages in ten years
    ltr = (table_size_in_pages_ten_years(rows_per_page, num_rows, disease_growth_month+symptom_growth_month))
    total_growth.append(ltr-now)
    current_size+=now
########################
###### medication ######
########################
    num_int_fields = 0
    num_text_fields = 2
    avg_data_type_size_array.clear()

    #overhead for strings
    cursor.execute("SELECT CEIL(AVG(pg_column_size(disease_name))) FROM medication")
    disease_name_avg_data_type_size = int(cursor.fetchone().pop())
    cursor.execute("SELECT CEIL(AVG( pg_column_size(medication_name))) FROM medication")
    medication_name_avg_data_type_size = int(cursor.fetchone().pop())
    avg_data_type_size_array.append(disease_name_avg_data_type_size)
    avg_data_type_size_array.append(medication_name_avg_data_type_size)
    
    #overhead w/ strings & normal
    print("\n[medication] ", end='')
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM medication")
    num_rows = int(cursor.fetchone().pop())
    now = table_size_in_pages(num_rows, rows_per_page)

    #growth size in pages in ten years
    ltr = table_size_in_pages_ten_years(rows_per_page, num_rows, medication_growth_month)
    total_growth.append(ltr-now)
    current_size+=now
#####################
###### patient ######
#####################
    num_int_fields = 2
    num_text_fields = 2
    avg_data_type_size_array.clear()

    #overhead for strings
    cursor.execute("SELECT CEIL(AVG(pg_column_size(name))) FROM patient")
    name_avg_data_type_size = int(cursor.fetchone().pop())
    cursor.execute("SELECT CEIL(AVG( pg_column_size(sex))) FROM patient")
    sex_avg_data_type_size = int(cursor.fetchone().pop())
    avg_data_type_size_array.append(name_avg_data_type_size)
    avg_data_type_size_array.append(sex_avg_data_type_size)
    
    #overhead w/ strings & normal
    print("\n[patient] ", end='')
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM patient")
    num_rows = int(cursor.fetchone().pop())
    now = table_size_in_pages(num_rows, rows_per_page)

    #growth size in pages in ten years
    ltr = table_size_in_pages_ten_years(rows_per_page, num_rows, patient_growth_month)
    total_growth.append(ltr-now)
    current_size+=now
#####################
##### symptoms #####
#####################
    num_int_fields = 0
    num_text_fields = 1
    avg_data_type_size_array.clear()

    #overhead for strings
    cursor.execute("SELECT CEIL(AVG(pg_column_size(name))) FROM symptoms")
    name_avg_data_type_size = int(cursor.fetchone().pop())
    avg_data_type_size_array.append(name_avg_data_type_size)
    
    #overhead w/ strings & normal
    print("\n[symptoms] ", end='')
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM symptoms")
    num_rows = int(cursor.fetchone().pop())
    now = table_size_in_pages(num_rows, rows_per_page)

    #growth size in pages in ten years
    ltr = table_size_in_pages_ten_years(rows_per_page, num_rows, symptom_growth_month)
    total_growth.append(ltr-now)
    current_size+=now
################################
##### tests_and_procedures #####
################################
    num_int_fields = 0
    num_text_fields = 2
    avg_data_type_size_array.clear()

    #overhead for strings
    cursor.execute("SELECT CEIL(AVG(pg_column_size(disease_name))) FROM tests_and_procedures")
    disease_name_avg_data_type_size = int(cursor.fetchone().pop())
    cursor.execute("SELECT CEIL(AVG(pg_column_size(test_procedure))) FROM tests_and_procedures")
    test_procedure_avg_data_type_size = int(cursor.fetchone().pop())
    avg_data_type_size_array.append(disease_name_avg_data_type_size)
    avg_data_type_size_array.append(test_procedure_avg_data_type_size)

    #overhead w/ strings & normal
    print("\n[tests_and_procedures] ", end='')
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM tests_and_procedures")
    num_rows = int(cursor.fetchone().pop())
    
    now = table_size_in_pages(num_rows, rows_per_page)

    #growth size in pages in ten years
    ltr = table_size_in_pages_ten_years(rows_per_page, num_rows, test_procedure_growth_month)
    total_growth.append(ltr-now)
    current_size+=now

    ################
    # total growth #
    ################
    print("\nTotal growth in pages for all tables=", end='')
    i = 0
    for page_growth in total_growth:
        print(str(page_growth), end="")
        if(i < (len(total_growth)-1)):
            print("+", end='')
        i+=1
    print('=' + str(sum(total_growth)))
    print('Current total page size: '+ str(current_size))
    print('Final total page size: ' + str(current_size + sum(total_growth))) 
    

def common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array):
    page_size = 8192
    page_overhead = 24
    row_overhead = 27

    no_data_type_overhead = row_overhead+num_int_fields*4+num_text_fields*4
    total_overhead = no_data_type_overhead
    for data_type_overhead in avg_data_type_size_array:
        total_overhead = total_overhead + data_type_overhead

    R = (page_size - page_overhead) / (total_overhead)
    print("Calculations: \nRows per Page=(8192-" + str(page_overhead) + ")" + "/" + "(" + str(row_overhead) + "+" + str(num_int_fields) + "*4" + "+" + str(num_text_fields) + "*4", end ="")
    
    for data_type_overhead in avg_data_type_size_array:
        print( "+" + str(data_type_overhead), end ="")
    print(")=" + str("{0:.3f}".format(R)) + '=' + str(math.floor(R)))
    
    return math.floor(R)


def table_size_in_pages(num_rows, rows_per_page):
    print("Current table size in pages=(Rows/Rows Per Page)=" + str(num_rows) + "/" + str(rows_per_page) + "=" + str("{0:.3f}".format(num_rows / rows_per_page)) + "=" + str(math.ceil(num_rows / rows_per_page)))
    return math.ceil(num_rows / rows_per_page)

def table_size_in_pages_ten_years(rows_per_page, num_rows, add_num_rows_month):
    growth = (num_rows / rows_per_page) + ((add_num_rows_month*12*10)/rows_per_page)
    print("Future table size in pages after growing " + str(add_num_rows_month) + " rows per month=(" + str("{0:.3f}".format(num_rows/rows_per_page)) + "+" + str("{0:.3f}".format(add_num_rows_month*12/rows_per_page)) + "*10)=" + str("{0:.3f}".format(growth)) + "=" + str(math.ceil(growth)))
    return math.ceil(growth)

main()


