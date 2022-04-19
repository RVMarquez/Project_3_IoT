#PROJECT 3 - Yunah Kim and Rafael Marquez

#Using an RBG LED and Humidity/Temp Sensor along with Photoresistor
#The device will provied the user the nessesary information about the weather
#and assist in what to wear



#libraries
import RPi.GPIO as GPIO
from time import sleep

import Adafruit_DHT
import time
import datetime
from datetime import date
from openpyxl import load_workbook

#SERVER IMPORTS


#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BCM)
#set red,green and blue pins
redPin = 12
greenPin = 19
bluePin = 21


#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

#SETUP for HUMIDITY SENSOR

# DHT11 sensor selected
sensor = Adafruit_DHT.DHT11

# DHT sensor pin connected to GPIO 4
sensor_pin = 4

# create a variable to control the while loop
running = True

# Load the workbook and select the sheet
wb = load_workbook('/home/pi/dht11_excel/weather.xlsx')
sheet = wb['Sheet1']

#COLORS TO BE USED IN LAB
def turnOff():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)
    
def white():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
def red():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def green():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def blue():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def yellow():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def purple():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)


# loop forever
while running:

    try:
        # read the humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

        # The line below converts to Fahrenheit
        temp_f = temperature * 9/5.0 + 32
        
        today = date.today()
        now = datetime.datetime.now().time()

        if humidity is not None and temperature is not None:

            #print temperature and humidity
            print('Temp C = ' + str(temperature) +','+ 'Temp F = ' + str(temp_f) +',' + 'Humidity = ' + str(humidity))
            
            # update data to excel sheet
            row = (today, now, temperature, temp_f, humidity)
            sheet.append(row)
            time.sleep(1)

            # The workbook is saved!
            wb.save('/home/pi/dht11_excel/weather.xlsx')

        else:
            print('Failed to get reading. Try again!')
            time.sleep(1)

    except KeyboardInterrupt:
        print ('Goodbye!')
        running = False
