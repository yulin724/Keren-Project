# -*- coding: utf-8 -*-                # Document as UTF-8 Document.
#!/usr/bin/python                      # This is server.py file

import sys
import time

def logger(kind,log):
    try:
        text_file = open("logging.txt","a")
        text_file.write("[" + kind + "] " + "[" + time.strftime("%X%p") + "] " + log + '\n')
        text_file.close()
        print("[-] Log added sucssfully!")
    except:
        print("[CRITICAL] Error While Logging Session.")
