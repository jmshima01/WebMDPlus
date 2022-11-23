import db_conn
import db_queries

conn = db_conn.get_conn()
cursor = db_conn.get_cursor(conn)

#panicDisorder = db_queries.get_disease_by_name(cursor, "Panic disorder")
# for row in panicDisorder:
#     name, description = row
#     print(description)

# print(cursor.rowcount)

# symptoms = db_queries.get_all_symptoms(cursor)
# for row in symptoms:
#     name = row
#     print(name)

name = "Daffy Duck"
db_queries.create_new_patient(cursor, name, 38, 0)
query = "SELECT * FROM patient WHERE name=%s"
cursor.execute(query, (name,))
results = cursor.fetchall()
print(results)

patients = db_queries.get_all_patients(cursor)

for row in patients:
    name = row
    print(patients)

print("Row count:" + str(cursor.rowcount))