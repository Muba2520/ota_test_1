# This is a test file of the OTA code
from machine import Pin
import utime
print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")

led = Pin(2,Pin.OUT)

while True:
# num = int(input("Etter a number : "))
# for i in range(5):
   led.value(1)
   utime.sleep(0.1)
   led.value(0)
   utime.sleep(0.1)
