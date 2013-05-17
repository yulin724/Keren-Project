# -*- coding: utf-8 -*-                # Document as UTF-8 Document.
#!/usr/bin/python

import sys
import socket
import time
sys.path.append("Modules/guess_language")
import guess_language

def checkLanguage(msg):
    
    guess = (guess_language.guessLanguageName(msg))
    if(guess == "UNKNOWN"):
        guess = "En"
        return guess
    else:
        guess = guess[:2]
        return guess
