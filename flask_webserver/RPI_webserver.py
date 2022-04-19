from flask import Flask, render_template
import RPi.GPIO as GPIO
import Adafruit_DHT as dht

import time
import datetime
from datetime import date

app = Flask(__name__)
 
GPIO.setmode(GPIO.BCM)
led1 = 21 
led2 = 20
DHT11_pin = 4


# Set each pin as an output and make it low:
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)



@app.route("/")
   
 
def main():
   return render_template('main.html')
 
# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<pin>/<action>")
def action(pin, action):
   temperature = ''
   temper_f = ''
   humidity = ''
   today_s = ''
   now_s = ''
   
   if pin == "pin1" and action == "on":
      GPIO.output(led1, GPIO.HIGH)
    
   if pin == "pin1" and action == "off":
      GPIO.output(led1, GPIO.LOW)
    
   if pin == "pin2" and action == "on":
      GPIO.output(led2, GPIO.HIGH)
    
   if pin == "pin2" and action == "off":
      GPIO.output(led2, GPIO.LOW)
 
   if pin == "dhtpin" and action == "get":
      #humi, temp = dht.read_retry(dht.DHT11, DHT11_pin)  # Reading humidity and temperature
      
      # read the humidity and temperature
        humi, temp = dht.read_retry(dht.DHT11, DHT11_pin)

        # The line below converts to Fahrenheit
        temp_f = temp* 9/5.0 + 32
        
        today = date.today()
        today_s = today.strftime('%Y-%m-%d')
        now = datetime.datetime.now().time()
        now_s = now.strftime('%H:%M:%S')

        if humi is not None and temp is not None:

            today_s = '%s' % today_s
            now_s = '%s' % now_s
            humi = '{0:0.1f}' .format(humi)
            temp = '{0:0.1f}' .format(temp)
            temper_f = '{0:0.1f}' .format(temp_f)
            
            today_s = 'Date: ' + today_s
            now_s = 'Time: ' + now_s
            temperature = 'Temperature (C): ' + temp
            temper_f = 'Temperature (F): ' + temper_f
            humidity =  'Humidity: ' + humi
            

 
   templateData = {
   'today_s' : today_s,
   'now_s' : now_s,
   'temperature' : temperature,
   'temperature_f' : temper_f,
   'humidity' : humidity
   }
 
   return render_template('main.html', **templateData)
 
if __name__ == "__main__":
   app.run(host='10.224.59.247', port=80, debug=True)