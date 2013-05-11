# -*- coding: utf-8 -*-                                                    # Document as UTF-8 Document.

import sys
import time
sys.path.append("Modules/Weather")
import Weather
sys.path.append("Modules/Logger")
import logit
sys.path.append("Modules/getProfileData")
import profileData

print("------------------------ Check Weather -----------------------")
print("")

location = "Haifa"
weather = Weather.main(location)
print("")
print weather
print("")

logit.logger("Info","Test Module run out. ")

print("")
print ("--------------------------------------------------------------")
print("")

IMEI = "356516040249414"
Fake_IMEI = "35651604000000"
print ("------------ Get Profile Full Name by IMEI ------------------")
print("")

nameData = profileData.getNameData(IMEI)
print nameData

print("")
print ("-------------------------------------------------------------")
print ("")
print ("------------ Check If Device Can Access The Server ----------")
print("")

canAccess = profileData.isVaildIMEI(IMEI)

if(canAccess == True):
        print("Device Is Vaild, Welcome " + nameData)
else:
        print ("Your device isn't Indentified, Access Denied.") # Else == False

print("")
print ("-------------------------------------------------------------")
print("")
print("---------------- If Access denied to the server --------------")
print("")

canAccess = profileData.isVaildIMEI(Fake_IMEI)

if(canAccess == True):
        print("Device Is Vaild, Welcome " + nameData)
else:
        print ("Your device isn't Indentified, Access Denied.") # Else == False

print("")
print("--------------------------------------------------------------")

raw_input("")
