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
   time2 = utime.time()
   ftime = time2 - time1
   if ftime >= 10:
      ota_updater.download_and_install_update_if_available()
      
   for i in range(10):
      led.value(1)
      utime.sleep(5)
      led.value(0)
      utime.sleep(5)
