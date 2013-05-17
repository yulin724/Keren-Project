#!/usr/bin/python

import urllib, pycurl, os
from time import sleep

def downloadFile(url, fileName):
    fp = open(fileName, "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()

def getGoogleSpeechURL(Sentence,Language):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=" + Language + "&"
    parameters = {'q': Sentence}
    data = urllib.urlencode(parameters)
    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
    return googleTranslateURL

def speakSpeechFromText(Sentence,Language):
    googleSpeechURL = getGoogleSpeechURL(Sentence,Language)
    downloadFile(googleSpeechURL,"tts.mp3")
    os.system("mplayer tts.mp3 -af extrastereo=0 &")
