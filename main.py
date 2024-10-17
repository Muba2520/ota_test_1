# This is a test file of the OTA code
from machine import Pin
import utime
print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")

led = Pin(2,Pin.OUT)
time1 = utime.time()
print(time1)

while True:     
   for i in range(10):
      led.value(1)
      utime.sleep(1)
      led.value(0)
      utime.sleep(1)
