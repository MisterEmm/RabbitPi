#! /usr/bin/env python
# For latest version see https://github.com/sammachin/AlexaPi/blob/master/main.py

import os
import random
import time
import RPi.GPIO as GPIO
import alsaaudio
import wave
import random
from creds import *
import requests
import json
import re
from memcache import Client
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

#Settings
button = 18 #GPIO Pin with button connected
lights = [24, 25] # GPIO Pins with LED's conneted
device = "plughw:1" # Name of your microphone/soundcard in arecord -L

#Setup
recorded = False
servers = ["127.0.0.1:11211"]
mc = Client(servers, debug=1)
path = os.path.realpath(__file__).rstrip(os.path.basename(__file__))


def turnOffMotors():
	
mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	
mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)



atexit.register(turnOffMotors)



myMotor = mh.getMotor(2)

myMotor1 = mh.getMotor(4)





def internet_on():
    print "Checking Internet Connection"
    try:
        r =requests.get('https://api.amazon.com/auth/o2/token')
	print "Connection OK"
        return True
    except:
	print "Connection Failed"
    	return False

	
def gettoken():
	token = mc.get("access_token")
	refresh = refresh_token
	if token:
		return token
	elif refresh:
		payload = {"client_id" : Client_ID, "client_secret" : Client_Secret, "refresh_token" : refresh, "grant_type" : "refresh_token", }
		url = "https://api.amazon.com/auth/o2/token"
		r = requests.post(url, data = payload)
		resp = json.loads(r.text)
		mc.set("access_token", resp['access_token'], 3570)
		return resp['access_token']
	else:
		return False
		

def alexa():
	GPIO.output(lights[0], GPIO.HIGH)
	myMotor.run(Adafruit_MotorHAT.FORWARD)
	
	myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	
	myMotor.setSpeed(255)
	
	myMotor1.setSpeed(255)
	
	url = 'https://access-alexa-na.amazon.com/v1/avs/speechrecognizer/recognize'
	headers = {'Authorization' : 'Bearer %s' % gettoken()}
	d = {
   		"messageHeader": {
       		"deviceContext": [
           		{
               		"name": "playbackState",
               		"namespace": "AudioPlayer",
               		"payload": {
                   		"streamId": "",
        			   	"offsetInMilliseconds": "0",
                   		"playerActivity": "IDLE"
               		}
           		}
       		]
		},
   		"messageBody": {
       		"profile": "alexa-close-talk",
       		"locale": "en-us",
       		"format": "audio/L16; rate=16000; channels=1"
   		}
	}
	with open(path+'recording.wav') as inf:
		files = [
				('file', ('request', json.dumps(d), 'application/json; charset=UTF-8')),
				('file', ('audio', inf, 'audio/L16; rate=16000; channels=1'))
				]	
		r = requests.post(url, headers=headers, files=files)
	if r.status_code == 200:
		for v in r.headers['content-type'].split(";"):
			if re.match('.*boundary.*', v):
				boundary =  v.split("=")[1]
		data = r.content.split(boundary)
		for d in data:
			if (len(d) >= 1024):
				audio = d.split('\r\n\r\n')[1].rstrip('--')
		with open(path+"response.mp3", 'wb') as f:
			f.write(audio)
		GPIO.output(lights[1], GPIO.LOW)

		os.system('mpg123 -q {}1sec.mp3 {}response.mp3 {}1sec.mp3'.format(path, path, path))
		GPIO.output(lights[0], GPIO.LOW)
		myMotor.run(Adafruit_MotorHAT.RELEASE)
		
		myMotor1.run(Adafruit_MotorHAT.RELEASE)
	else:
		GPIO.output(lights[1], GPIO.LOW)
		for x in range(0, 3):
			time.sleep(.2)
			GPIO.output(lights[1], GPIO.HIGH)
			time.sleep(.2)
			GPIO.output(lights[1], GPIO.LOW)
		



def start():
	last = GPIO.input(button)
	while True:
		val = GPIO.input(button)
		GPIO.wait_for_edge(button, GPIO.FALLING) # we wait for the button to be pressed
		GPIO.output(lights[1], GPIO.HIGH)
		inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, device)
		inp.setchannels(1)
		inp.setrate(16000)
		inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
		inp.setperiodsize(500)
		audio = ""
		while(GPIO.input(button)==0): # we keep recording while the button is pressed
			l, data = inp.read()
			if l:
				audio += data
		rf = open(path+'recording.wav', 'w')
		rf.write(audio)
		rf.close()
		inp = None
		alexa()

	

if __name__ == "__main__":
	GPIO.setwarnings(False)
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(lights, GPIO.OUT)
	GPIO.output(lights, GPIO.LOW)
	while internet_on() == False:
		print "."
	token = gettoken()
	myMotor.run(Adafruit_MotorHAT.BACKWARD)
	
	myMotor1.run(Adafruit_MotorHAT.FORWARD)
	
	myMotor.setSpeed(255)
	
	myMotor1.setSpeed(255)

	GPIO.output(lights[0], GPIO.HIGH)
	os.system('mpg123 -q {}1sec.mp3 {}boing.mp3'.format(path, path))
	time.sleep(6.6)
	#full ear rotate
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	
	myMotor1.run(Adafruit_MotorHAT.RELEASE)
	GPIO.output(lights[0], GPIO.LOW)
	
start()