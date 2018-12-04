import RPi.GPIO as GPIO
from time import sleep
import requests
from firebase import firebase
fbase = firebase.FirebaseApplication('https://iot-smart-parking-bdf95.firebaseio.com/',None)


GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.IN)
GPIO.setup(4,GPIO.IN)
GPIO.setup(26,GPIO.IN)
GPIO.setup(27,GPIO.IN)


while True:
    sensedata = GPIO.input(14)
    sense2 = GPIO.input(4)
    sense3 = GPIO.input(27)
    sense4 = GPIO.input(26)
    
    getdata = fbase.get('nodes/node1/reading','')
    getdata2 = fbase.get('nodes/node2/reading','')
    getdata3 = fbase.get('nodes/node3/reading','')
    getdata4 = fbase.get('nodes/node4/reading','')
    
    if sensedata==int(getdata):
        print("No state change in node 1")
    else:
        print("State changed in A1")
        res = fbase.put('nodes/node1','reading',str(sensedata))
        if sensedata == 0:
            print("car parked in A1")
            sleep(2)
        elif sensedata == 1:
            print("Car Left from A1")
            sleep(2)
    if sense2==int(getdata2):
        print("No state change in node 2")
    else:
        print("State changed in 2")
        res = fbase.put('nodes/node2','reading',str(sense2))
        if sense2 == 0:
            print("car parked in A2")
            sleep(2)
        elif sense2 == 1:
            print("Car Left from A2")
            sleep(2)
    if sense3==int(getdata3):
        print("No state change in node 3")
    else:
        print("State changed in A3")
        res = fbase.put('nodes/node3','reading',str(sense3))
        if sense3 == 0:
            print("car parked in A3")
            sleep(2)
        elif sense3 == 1:
            print("Car Left from A3")
            sleep(2)
    if sense4==int(getdata4):
        print("No state change in node 4")
    else:
        print("State changed in 4")
        res = fbase.put('nodes/node4','reading',str(sense4))
        if sense4 == 0:
            print("car parked in A4")
            sleep(2)
        elif sense4 == 1:
            print("Car Left from A4")
            sleep(2)
