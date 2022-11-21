import db_conn
import db_queries

conn = db_conn.get_conn()
cursor = db_conn.get_cursor(conn)

#panicDisorder = db_queries.get_disease_by_name(cursor, "Panic disorder")
# for row in panicDisorder:
#     name, description = row
#     print(description)

# print(cursor.rowcount)

symptoms = db_queries.get_all_symptoms(cursor)
for row in symptoms:
    name = row
    print(name)

print("Row count:" + cursor.rowcount)