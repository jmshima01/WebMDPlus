#!/usr/bin/python3
import getpass
import pg8000

def get_conn():
    user = "gstookey" #input("Username: ")
    secret = "@Collin0820" #getpass.getpass()
    conn = pg8000.connect(user=user, password=secret, host='codd.mines.edu', port=5433, database='csci403')
    return conn

def get_cursor(conn):
    cursor = conn.cursor()
    cursor.execute("set search_path to f22_group6")
    return cursor

# "prepared"
# query = "SELECT course_id, section, title FROM mines_courses WHERE instructor = %s"
# instructor = input("Enter instructor as last, first: ")
# cursor.execute(query,  (instructor,))
# results = cursor.fetchall()

# for row in results:
#     course_id, section, title = row
#     print(course_id, section, title)

# # other types
# cursor.execute("SELECT 42, current_date, now(), 3.145::numeric(5,3)")
# print(cursor.fetchall())

# # get column names
# cursor.execute(query, (instructor, ))
# columns = [x[0] for x in cursor.description]
# print(columns)

# # DDL
# cursor.execute("DROP TABLE IF EXISTS fruit")
# cursor.execute("CREATE TABLE fruit (name text, quantity integer)")

# # modification queries
# query = "INSERT INTO fruit VALUES (%s, %s)"
# cursor.execute(query, ("apple", 42))
# cursor.execute(query, ("pear", 17))
# print("Rows inserted: ", cursor.rowcount)

# cursor.execute("UPDATE fruit SET quantity = %s WHERE name = %s", (99, "pear"))
# print("Rows updated: ", cursor.rowcount)

# # this is needed by default to save changes on database
# db.commit()

# # uncomment this if you want all queries to commit immediately
# #db.autocommit = True

# # exception handling
# # if an exception occurs (without autocommit), pg8000 will refuse
# # to do any further queries until you execute a rollback
# try:
#     cursor.execute("SELECT arglbargle FROM blah")
# except pg8000.Error as e:
#     print('Database error: ', e)
#     db.rollback()


