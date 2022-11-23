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
    print("Disease")
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM disease")
    num_rows = int(cursor.fetchone().pop())
    print("Table size in pages now: " + str(table_size_in_pages(num_rows, rows_per_page)))

    #growth size in pages in ten years
    print("Table size in pages in ten years: " + str(table_size_in_pages_ten_years(rows_per_page, num_rows, 10)))
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
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM disease_symptoms")
    num_rows = int(cursor.fetchone().pop())
    print("\n\nDisease Symptoms")
    print("Table size in pages now: " + str(table_size_in_pages(num_rows, rows_per_page)))

    #growth size in pages in ten years
    print("Table size in pages in ten years: " + str(table_size_in_pages_ten_years(rows_per_page, num_rows, 10)))

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
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM medication")
    num_rows = int(cursor.fetchone().pop())
    print("\n\nMedication")
    print("Table size in pages now: " + str(table_size_in_pages(num_rows, rows_per_page)))

    #growth size in pages in ten years
    print("Table size in pages in ten years: " + str(table_size_in_pages_ten_years(rows_per_page, num_rows, 10)))

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
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM patient")
    num_rows = int(cursor.fetchone().pop())
    print("\n\nPatient")
    print("Table size in pages now: " + str(table_size_in_pages(num_rows, rows_per_page)))

    #growth size in pages in ten years
    print("Table size in pages in ten years: " + str(table_size_in_pages_ten_years(rows_per_page, num_rows, 20)))

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
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM symptoms")
    num_rows = int(cursor.fetchone().pop())
    print("\n\nSymptoms")
    print("Table size in pages now: " + str(table_size_in_pages(num_rows, rows_per_page)))

    #growth size in pages in ten years
    print("Table size in pages in ten years: " + str(table_size_in_pages_ten_years(rows_per_page, num_rows, 1)))


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
    print("\n\nTests and Procedures")
    rows_per_page = common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array)

    #table size in pages now
    cursor.execute("SELECT COUNT(*) FROM tests_and_procedures")
    num_rows = int(cursor.fetchone().pop())
    
    print("Table size in pages now: " + str(table_size_in_pages(num_rows, rows_per_page)))

    #growth size in pages in ten years
    print("Table size in pages in ten years: " + str(table_size_in_pages_ten_years(rows_per_page, num_rows, 10)))


def common_overhead_calc(num_int_fields, num_text_fields, avg_data_type_size_array):
    page_size = 8192
    page_overhead = 24
    row_overhead = 27

    no_data_type_overhead = row_overhead+num_int_fields*4+num_text_fields*4
    total_overhead = no_data_type_overhead
    for data_type_overhead in avg_data_type_size_array:
        total_overhead = total_overhead + data_type_overhead

    R = (page_size - page_overhead) / (total_overhead)
    print("\tCalc: \n Rows in Page=(8192-" + str(page_overhead) + ")" + "/" + "(" + str(row_overhead) + "+" + str(num_int_fields) + "*4" + "+" + str(num_text_fields) + "*4", end ="")
    
    for data_type_overhead in avg_data_type_size_array:
        print( "+" + str(data_type_overhead), end ="")
    print(")=" + str(R))
    
    return math.floor(R)


def table_size_in_pages(num_rows, rows_per_page):
    print("Table size in pages=" + str(num_rows) + "/" + str(rows_per_page) + "=" + str(num_rows / rows_per_page))
    return math.ceil(num_rows / rows_per_page)

def table_size_in_pages_ten_years(rows_per_page, num_rows, add_num_rows_month):
    print("\tCalc: " )
    return math.ceil((num_rows / rows_per_page) + ((add_num_rows_month*12*10)/rows_per_page))

main()


