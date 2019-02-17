from bs4 import BeautifulSoup
import urllib
import sms
import RPi.GPIO as GPIO
import lvl
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
url = "http://192.168.225.175:80"
def levelid():
    content = urllib.urlopen(url).read()
    soup = BeautifulSoup(content,"html5lib")
    #print (soup.prettify())
    lvl=soup.body.string
    level=int(lvl)
    return level
def fillwater():
    lm=levelid()
    while lm!=2:
        lm=levelid()
        GPIO.output(18,False)
        print("water being filled",lm)
        if(GPIO.input(17)==0):
            lowemp()  
    GPIO.output(18,True)
    return
def lowemp():
    GPIO.output(18,True)
    sms.smssend()
    lv=GPIO.input(17)
    while lv==False:
        lv=GPIO.input(17)
        time.sleep(1)
    return
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setwarnings(False)
    lm=levelid()
    lv=GPIO.input(17)
    print(lv)
    if(lv==True):
        if(lm==0):
            fillwater()
            print("Water filled",lm)
            lvl.uploaddata(1000)
    else:
        lowemp()
    GPIO.cleanup()  
