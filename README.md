# RabbitPi
Code examples from the RabbitPi project

The examples included are taken from the working RabbitPi project, documented at http://www.instructables.com/id/RabbitPi-the-Alexa-Enabled-IFTTT-Connected-Ear-Wig/

The code shown is in a "working" state but neads some serious tidying up. I'm conscious that loops need to be added, along with more comments, and a better structure for holding the various credentials in separate files. It also needs additions to make it exit more elegantly in case of problems, and the gmail side would benefit from some encryption. Still it works surprisingly well and I was reluctant to tinker with it too much while it was working! 

The files included are as follows: 

main.py
+++++++

This is my version of the main.py script used in Sam Machin's AlexaPi repository (which you'll need), which is available at https://github.com/sammachin/AlexaPi. 

My version changes very little, just loads a different mp3 on boot and includes extra lines for controlling the Adafruit Motor Hat to make the RabbitPi ears move while Alexa is searching and after booting. If you're interested in the Alexa voice search function it's well worth reading the instructions on the AlexaPi pages and reading through the open issues if you have any problems, I found nearly all of my answers there. The code changes quite often so it's worth keeping an eye on - also other branches are available offering music functionality.

rabbit.py
+++++++++

This is the main script that reads out the notifications, takes pictures and uploads them to Twitter. It includes elements from the below 

Tweeting Babbage - https://www.raspberrypi.org/learning/tweeting-babbage/
Pyvona - http://www.zacharybears.com/pyvona 
Imaplib - https://docs.python.org/2/library/imaplib.html

It's currently set to run on startup using the /etc/rc.local method, which has worked fine so far.

Developer Accounts
++++++++++++++++++

The links above provide great resources and the necessary modules are easily installed, Pyvona especially. To get the code to connect to the web services you'll need to set up some developer accounts as well (this is covered in their individual guides as well)

Amazon Alexa (for the AlexaPi voice search) - https://developer.amazon.com/appsandservices/solutions/alexa

Ivona (for the Pyvona TTS service) - https://www.ivona.com/ 

Twitter (for the Selfie Tweeting) - https://apps.twitter.com/








