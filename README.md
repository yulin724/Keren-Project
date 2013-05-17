# Keren Project - Smart House at its best.

So at this point you may be wondering... What is the Keren Project?
The simplest way to explain it would be a revolutionary new AI capable of serving you to her fullest.
Whatever you need done, she will do with your consent.

# So what can she do now?

So far we have more or less implemented these features (and this is only a small part):

 - Speech recognition - within the SL4A, Android APP needed. (Thanks to Google Voice Recognition Android API)
 - Recognize the language - Credit to the Author Kent Johnson for the package used.
 - Text-to-Speech in any language - ready! (Thanks to Google Translate TTS)
 - Weather - Ready!
 - Profiles - Ready!
 - Log everything - Ready!
 - Verify legitimate requests - Ready! *Not included in the current client code.
 
 With upcoming features such as:

 - Air Conditioning Control.
 - TV Control.
 - Home Lights Control.
 - Coffee Machine automation (Yes!)
 - An Automatic Plant Watering System.
 - Online IP Camera(s) Control
 - Native android application. (A Regular APK) - Working on it.

# Bugs:

[Solved] - UTF-8 Problem - Can't send Hebrew/Russian or other unique language strings.
[Solved] - socket.error: [Errno 98] Address already in use - Fixed by Overwriting the socket port each startup.

# Updates:

[07/05/2013] Update: All the Server requests are being logged into the logging file,
		     you can't see the request message on the Server anymore, you don't need it anyway.
		     I'm working now on the command recognition in the server side, stay tuned!

[11/05/2013] Update: Added test module, Weather function complete, returning full sentece with the current weather condition.

[15/05/2013] Update: lot of new things, I just connected 8 channels relay, and it works like a charm.
		     I was able to send commands through my android voice recognition to the server, and Power on the relay.
		     There are still lot of bugs and I need contributers or it will take long time to finish this project.
 
[17/05/2013] Update: Repeating code at main.py fixed thanks to "Hydra Hacker", Google TTS Service added.
		     More functions on the way, GPIO Function ready not yet uploaded, too many bugs ...
		     Modules Folder Replaced with Functions Folder.
		     Android Application is being developed at those days.

We hope to see you contribute to our project.