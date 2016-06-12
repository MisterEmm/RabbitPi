# RabbitPi
Code examples from the RabbitPi project

The examples included are taken from the working RabbitPi project, documented at:

The files included are as follows: 

main.py - this is my version of the main.py script used in Sam Machin's excellent AlexaPi repository, which is available at XXXXXX. 

My version changes very little, just loads a different mp3 on boot and includes extra lines to make the RabbitPi ear motors run while Alexa is searching and after booting. If you're interested in the Alexa voice search function it's well worth reading the instructions on the AlexaPi pages and reading through the open issues. The code changes quite often so it's worth keeping an eye on - also other branches are available offering music functionality.

rabbit.py - this is the main script that reads out the notifications, takes pictures and uploads them to Twitter. It relies on the following repositories which are worth reading beforehand:

Tweeting Babbage
Twython
Pyvona
Imaplib


