from nanpy import ArduinoApi
from nanpy import SerialManager
from os import system
import time

co = SerialManager(device='/dev/ttyUSB0')

uno = ArduinoApi(connection=co)

button = 5
button2 = 2
buttonstate = 0
buttonstate2 = 0
red = 13
green = 12
blue = 11
red2 = 7
green2 = 6
blue2 = 4

uno.pinMode(red, uno.OUTPUT)
uno.pinMode(green, uno.OUTPUT)
uno.pinMode(blue, uno.OUTPUT)
uno.pinMode(button, uno.INPUT)
uno.pinMode(red2, uno.OUTPUT)
uno.pinMode(green2, uno.OUTPUT)
uno.pinMode(blue2, uno.OUTPUT)
uno.pinMode(button2, uno.INPUT)



while True:
    buttonstate = uno.digitalRead(button)
    buttonstate2 = uno.digitalRead(button2)
    if buttonstate == uno.HIGH:
        uno.analogWrite(red, 32)
        uno.analogWrite(green, 178)
        uno.analogWrite(blue, 170)
        system("./dworkspace.sh")
    elif buttonstate2 == uno.HIGH:
        uno.analogWrite(red2, 32)
        uno.analogWrite(green2, 178)
        uno.analogWrite(blue2, 170)
        system("./rworkspace.sh")
    elif buttonstate == uno.LOW or buttonstate2 == uno.LOW:
        uno.analogWrite(red, 0)
        uno.analogWrite(green, 0)
        uno.analogWrite(blue, 0)
        uno.analogWrite(red2, 0)
        uno.analogWrite(green2, 0)
        uno.analogWrite(blue2, 0)
