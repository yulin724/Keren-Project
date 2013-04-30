# -*- coding: utf-8 -*-                # Document as UTF-8 Document.

import sqlite3

conn = sqlite3.connect("../Keren_DB.db")
cursor = conn.cursor()
try:
    
    cursor.execute("""
    CREATE TABLE weather_codes
    (country text, city text, zip_code text) 
    """)
    
except:
    
    print("[-] Database Exist :)")
    print("")

    try:

        country = raw_input("input Country: ")
        city = raw_input("input City: ")
        code = raw_input("input Zip Code: ")
        SQL = [(country, city, code)]
        
        cursor.executemany("INSERT INTO weather_codes VALUES (?,?,?)", SQL)
        conn.commit()

    except (KeyboardInterrupt, SystemExit):
             raw_input("Click any key to exit....")
    
