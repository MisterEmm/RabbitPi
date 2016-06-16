# RabbitPi

The examples included are taken from the RabbitPi project, documented at http://www.instructables.com/id/RabbitPi-the-Alexa-Enabled-IFTTT-Connected-Ear-Wig/ , video at https://www.youtube.com/watch?v=t7cM2mfyBRk

It's a Raspberry Pi digital assistant, building on the IoT heritage of the Nabaztag, Nabaztag:Tag and Karotz smart rabbits that have now been obsolete for several years. 

The code shown is in a "working" state but neads tidying up, a work in progress. I'm conscious that loops need to be added, along with more comments, and a better structure for holding the various credentials in separate files. It also needs additions to make it exit more elegantly in case of problems, and the gmail side would benefit from some encryption. Still it functions surprisingly well on a Pi 3 as a proof of concept and I was reluctant to tinker with it too much while it was working! I also plan to add in more functions to make the rabbit "dance" and so that a random confirmation from a list is read out when a selfie is tweeted.

The files included are as follows: 

main.py


This is an adaptation of the main.py script used in Sam Machin's AlexaPi repository (which you'll need), which is available at https://github.com/sammachin/AlexaPi. 

My version changes very little, just loads a different mp3 on boot and includes extra lines for controlling the Adafruit Motor Hat to make the RabbitPi ears move while Alexa is searching and after booting. If you're interested in the Alexa voice search function it's well worth reading the instructions on the AlexaPi pages and reading through the open issues if you have any problems, I found nearly all of my answers there. The code changes quite often so it's worth keeping an eye on - also other branches are available offering music functionality.

rabbit.py


This is the main script that reads out the notifications, takes pictures and uploads them to Twitter. It includes elements from the below 

Tweeting Babbage - (selfie function) https://www.raspberrypi.org/learning/tweeting-babbage/

Pyvona - (text to speech) http://www.zacharybears.com/pyvona 

Imaplib - (retrieving gmail) https://docs.python.org/2/library/imaplib.html

Adafruit - (controlling ear motors) https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library

It's currently set to run on startup using the /etc/rc.local method ("adding in python /home/pi/RabbitPi/rabbit.py &" just above the last exit 0 line), which has worked fine so far.

Developer Accounts
++++++++++++++++++

The links above provide great resources and the necessary modules are easily installed, Pyvona especially. To get the code to connect to the web services you'll need to set up some developer accounts as well (this is covered in their individual guides as well)

Amazon Alexa (for the AlexaPi voice search) - https://developer.amazon.com/appsandservices/solutions/alexa

Ivona (for the Pyvona TTS service) - https://www.ivona.com/ 

Twitter (for the Selfie Tweeting) - https://apps.twitter.com/

IoT recipes can be created at https://ifttt.com/recipes 








