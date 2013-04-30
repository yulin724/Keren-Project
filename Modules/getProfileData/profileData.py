# -*- coding: utf-8 -*-                                                    # Document as UTF-8 Document.
#!/usr/bin/python                                                          # This is server.py file

import sqlite3
import time
import hashlib
import sys
sys.path.append("Modules/Logger")                                          # Get Weather Module Location.
import logit

conn = sqlite3.connect("./Databases/Keren_DB.db")
cursor = conn.cursor()

def isVaildIMEI(IMEI):

    vaildIMEI = False

    hash_IMEI = hashlib.md5(IMEI).hexdigest()
    sql = "SELECT * FROM Profiles WHERE android_imei=?"
    cursor.execute(sql, [(hash_IMEI)])
    try:
        
        results = cursor.fetchall()[0]
        resultsLen = len(results)
        if(resultsLen == 0):
            print 'Could not find any results.'
        else:
            IMEIFromDB = (results)[6]
            nameData = getNameData(IMEI)
            vaildIMEI = True
            logit.logger("Info", nameData + " Accessed the Server.")
            return vaildIMEI
    except:

        logit.logger("Warning","Unverified android device tried to access the server: " + IMEI)
        return False

def getNameData(IMEI):

    hash_IMEI = hashlib.md5(IMEI).hexdigest()
    sql = "SELECT * FROM Profiles WHERE android_imei=?"
    cursor.execute(sql, [(hash_IMEI)])
    try:
        
        results = cursor.fetchall()[0]
        resultsLen = len(results)
        if(resultsLen == 0):
            print 'Could not find any results.'
        else:
            nameData = (results)[0] + " " + (results)[1]
            return nameData
    except:
        
        logit.logger("Warning","Failed to verify Android Device, IMEI: " + IMEI)
        logit.logger("Warning","Unverified android device tried to get Name data From DB.")
        return False
