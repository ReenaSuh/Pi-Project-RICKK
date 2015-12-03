# Group 4
# Catherine O'Mary
# Keerthana Ramesh
# Kayla Scott
# Reena Suh

from time import sleep
import sys
import Adafruit_DHT 
import RPi.GPIO as GPIO

def main:
    #Main, takes input from the sensor and the keypad and turns the fan and the humidifier 
    #on or off based on the return values of the sensor and the keypad 

    #coded by Catherine O'Mary
    #import sensor and keypad libraries

    #“””*****************************Gathering data*********************************”””

    #Get min temp from keypad
    min_temp=raw_input("Enter the temperature at which you would like the fan to turn off: ")

    #Get max temp from keyboard
    max_temp=raw_input("Enter the temperature at which you would like the fan to turn on: ")
    while max_temp <= min_temp :
        max_temp=raw_input("Make sure the max temperature is greater than the minimum temperature: ")

    #Get min hum from keypad
    min_hum=raw_input("Enter the humidity at which you would like the humidifier to turn on: ")

    #Get max hum from keypad
    max_hum=raw_input("Enter the humidity at which you would like the humidifier to turn off: ")
    while max_hum <= min_hum :
       max_hum=raw_input("Make sure the max humidity is greater than the minimum humidity: ")


    #“””*****************************Making Decisions*******************************”””

    quit=False
    #loops forever 
    while not quit :
        #Break down the input from the sensor into humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        #“””try to get the temperature in the range (min_temp,max_temp) non-inclusive by controlling the fan”””
        if temperature < min_temp:
            #turn fan off, it’s too cold
	          off(1)
        elif temperature >max_temp:
            #turn fan on, it’s too hot
            on(1)
        #“””try to get the humidity in the range (min_hum,max_hum) non-inclusive by controlling the humidifier”””
        if temperature < min_hum:
            #turn humidifier on, it’s too dry
            on(2)
        elif temperature >max_hum:
            #turn fan off, it’s too humid
            off(2)
        sleep(60)#pauses the program for 60 seconds
        
#This function is from github
def on(outlet):
    #! /usr/bin
    relay_pins = {'one': 21, 'two':22} #'three':12, 'four':16, 'five':18, 'six':22, 'seven':15, 'eight':13}
    GPIO.setmode(GPIO.BOARD) # use P1 header pin numbering convention
    GPIO.setwarnings(False) # don't want to hear about how pins are already in use
    
    for relay_pin, board_pin in relay_pins.iteritems():
        GPIO.setup(board_pin, GPIO.OUT)
        GPIO.output(board_pin, GPIO.HIGH)
#This one too
def off(outlet)
    #! /usr/bin/python

    relay_pins = {'one': 21, 'two':22} #'three':12, 'four':16, 'five':18, 'six':22, 'seven':15, 'eight':13}
    GPIO.setmode(GPIO.BOARD) # use P1 header pin numbering convention
    GPIO.setwarnings(False) # don't want to hear about how pins are already in use
    
    for relay_pin, board_pin in relay_pins.iteritems():
        GPIO.setup(board_pin, GPIO.OUT)
        GPIO.output(board_pin, GPIO.LOW)


