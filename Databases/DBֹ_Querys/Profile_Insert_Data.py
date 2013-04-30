# -*- coding: utf-8 -*-                # Document as UTF-8 Document.

import sqlite3

conn = sqlite3.connect("../Keren_DB.db")
cursor = conn.cursor()
try:
    
    cursor.execute("""
    CREATE TABLE Profiles
    (name text, last_name text, birth_date text, gender text, country text, city text, android_imei) 
    """)
    
except:

    print("[-] Database Exist :)")
    print("")

    try:

        name = raw_input("Input Name: ")
        last_name = raw_input("Input Last Name: ")
        birth_date = raw_input("Input Birth Date (i.e 17061996): ")
        gender = raw_input("Input Gender: ")
        country = raw_input("input Country: ")
        city = raw_input("input City: ")
        imei = raw_input("Input Android IMEI Code (Keypress '*#06#' to find out the code): ")
        SQL = [(name, last_name, birth_date, gender, country, city, imei)]
        
        cursor.executemany("INSERT INTO Profiles VALUES (?,?,?,?,?,?,?)", SQL)
        conn.commit()
        print ''
        
    except (KeyboardInterrupt, SystemExit):
        raw_input("Click any key to exit....")
