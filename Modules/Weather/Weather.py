# -*- coding: utf-8 -*-                # Document as UTF-8 Document.
#!/usr/bin/python                      # This is server.py file

import urllib
from xml.dom import minidom
import sqlite3

conn = sqlite3.connect("./Databases/Keren_DB.db")
cursor = conn.cursor()

wurl = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
wser = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_zip(zip_code):
    url = wurl % zip_code +'&u=c'
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    for node in dom.getElementsByTagNameNS(wser, 'forecast'):
        forecasts.append({
        'date': node.getAttribute('date'),
        'low': node.getAttribute('low'),
        'high': node.getAttribute('high'),
        'condition': node.getAttribute('text')
        })
        ycondition = dom.getElementsByTagNameNS(wser, 'condition')[0]
        return {
            'current_condition': ycondition.getAttribute('text'),
            'current_temp': ycondition.getAttribute('temp'),
            'forecasts': forecasts ,
            'title': dom.getElementsByTagName('title')[0].firstChild.data
        }
def main(location):
    Search_Query = location
    try:
        sql = "SELECT * FROM weather_codes WHERE city=?"
        cursor.execute(sql, [(Search_Query)])
        results = cursor.fetchall()[0]
        a=weather_for_zip((results)[2])

        current_condition = a['current_condition']
        current_temp = a['current_temp']
        
        
        today = a['forecasts'][0]['date']
        high = a['forecasts'][0]['high']
        low = a['forecasts'][0]['low']
        condition = a['forecasts'][0]['condition']
        
        #print '=================================='
        #print '|',a['title'],'|'
        print '=================================='
        print '|current condition = ' + current_condition
        print '|current temp      = ' + current_temp
        print '=================================='
        print '|  today     = ' + today
        print '|  hight     = ' + high
        print '|  low       = ' + low
        print '|  condition = ' + condition
        print '=================================='
        #print '|  tomorrow  =',a['forecasts'][1]['date']
        #print '|  hight     =',a['forecasts'][1]['high']
        #print '|  low       =',a['forecasts'][1]['low']
        #print '|  condition =',a['forecasts'][1]['condition']
        #print '=================================='

        return "Today is " + today + ", The weather is expected to be between " + low + " and " + high + ", The current weather is " + current_temp + ", The sky is " + current_condition + " and it's expected to be " + condition
        
    except:
        print("Something went wrong... maybe the City isn't in our database")
        return 0
  #  main()
