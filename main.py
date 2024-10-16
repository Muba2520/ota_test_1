# This is a test file of the OTA code
from machine import Pin
import utime
print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")

led = Pin(2,Pin.OUT)

while True:
  led.value(1)
  ultime.sleep(1)
  led.value(0)
  ultime.sleep(1)
