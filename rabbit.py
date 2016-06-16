import imaplib
import email
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import RPi.GPIO as GPIO 
import pyvona
import atexit
from twython import Twython
from picamera import PiCamera
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import os

# Twitter Credentals - input below or import from a separate file
consumer_key        = 'your_consumer_key'
consumer_secret     = 'your_consumer_secret'
access_token        = 'your_access_token'
access_token_secret = 'your_access_token_secret'

path = '/home/pi/RabbitPi/'
mh = Adafruit_MotorHAT(addr=0x60)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT) ## Nose LED
GPIO.setup(25, GPIO.OUT) ## Belly LED

mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

# define which motors are used for the ears
myMotor = mh.getMotor(2)
myMotor1 = mh.getMotor(4)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def checkEmail():
        
    mail = imaplib.IMAP4_SSL('imap.gmail.com');
    mail.login('your_gmail_address','your_gmail_password');
    mail.list();  # Gives list of folders or labels in gmail.
    v = pyvona.create_voice('your_ivona_access_key', 'your_ivona_secret_key')    
    count = 0

    while count < 60:
        try:
            # Connect to inbox
            mail.select("inbox"); 
    
            # Search for an unread email from user's email address
            result, data = mail.search(None,'(UNSEEN FROM "your_email_address")');
    
            ids = data[0]   # data is a list
            id_list = ids.split() # ids is a space separated string

            latest_email_id = id_list[-1] # get the latest
            result, data = mail.fetch(latest_email_id, "(RFC822)");

            raw_email = data[0][1];

            recv_msg = email.message_from_string(raw_email)

            if(recv_msg['Subject'] != "selfie"):

                    print("Normal Message")     
                    print(recv_msg['Subject'])
                    print "Forward! "
                    GPIO.output(24,True)
                    myMotor.run(Adafruit_MotorHAT.FORWARD)
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor.setSpeed(255)
                    myMotor1.setSpeed(255)
                    v.voice_name = 'Amy'
                    v.region = 'eu-west'
                    v.speak(recv_msg['Subject'])
                    print "Release"
                    time.sleep(1)
                    myMotor.run(Adafruit_MotorHAT.RELEASE)
                    myMotor1.run(Adafruit_MotorHAT.RELEASE)
                    GPIO.output(24,False)

            elif(recv_msg['Subject'] == "selfie"):

                    print("Selfie Trigger")     
                    myMotor.run(Adafruit_MotorHAT.FORWARD)
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor.setSpeed(255)
                    myMotor1.setSpeed(255)
                    time.sleep(.8)
                    GPIO.output(25,True)
                    time.sleep(.2)
                    GPIO.output(25,False)
                    myMotor.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor.setSpeed(255)
                    myMotor1.setSpeed(255)
                    time.sleep(.8)
                    GPIO.output(25,True)
                    time.sleep(.2)
                    GPIO.output(25,False)
                    myMotor.run(Adafruit_MotorHAT.FORWARD)
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor.setSpeed(255)
                    myMotor1.setSpeed(255)
                    time.sleep(.8)
                    GPIO.output(25,True)
                    time.sleep(.2)
                    GPIO.output(25,False)
                    camera = PiCamera()
                    camera.vflip = True
                    camera.start_preview()
                    myMotor.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor.setSpeed(255)
                    myMotor1.setSpeed(255)
                    time.sleep(.8)
                    GPIO.output(25,True)
                    time.sleep(.2)
                    GPIO.output(25,False)
                    myMotor.run(Adafruit_MotorHAT.FORWARD)
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor.setSpeed(255)
                    myMotor1.setSpeed(255)
                    time.sleep(.8)
                    GPIO.output(25,True)
                    time.sleep(.2)
                    GPIO.output(25,False)
                    myMotor.run(Adafruit_MotorHAT.RELEASE)
                    myMotor1.run(Adafruit_MotorHAT.RELEASE)
                    time.sleep(.2)
                    camera.capture('/home/pi/image.jpg')
                    camera.stop_preview()
                    os.system('mpg123 -q {}camera.mp3'.format(path, path))
                    message = "RabbitPi Selfie!"
                    with open('/home/pi/image.jpg', 'rb') as photo:
                            twitter.update_status_with_media(status=message, media=photo)
                    v = pyvona.create_voice('your_ivona_access_key', 'your_ivona_secret_key')
                    v.voice_name = 'Amy'
                    v.region = 'eu-west'
                    GPIO.output(24,True)
                    v.speak('Selfie Tweeted')
                    GPIO.output(24,False)
                    GPIO.output(25,True)
                    time.sleep(.2)
                    GPIO.output(25,False)
                    time.sleep(.2)
                    GPIO.output(25,True)
                    time.sleep(.2)
                    GPIO.output(25,False)
                    time.sleep(.2)
                   
            else:
                    print("Nothing")

            
            count = 6

        except IndexError:
            time.sleep(30*1)
            if count < 5:
                count = count + 1
                continue
            else:
                print("Nothing to read out right now")
                count = 6             
checkEmail()
