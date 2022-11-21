# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:24:37 2022

@author: James Shima
"""

import getpass 
import pg8000

user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host='codd.mines.edu', port=5433, database='csci403')
cursor = db.cursor()
# immediate
cursor.execute("SELECT * FROM disease")

results = cursor.fetchall()
for i in results:
    print(i)