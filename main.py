# This is a test file of the OTA code
from machine import Pin
import time
print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")

led = Pin(2,Pin.OUT)

while True:
   led.value(1)
   time.sleep(1)
   led.value(0)
   time.sleep(1)
