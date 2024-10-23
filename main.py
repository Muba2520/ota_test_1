# This is a test file of the OTA code
import utime
import machine
from ota import OTAUpdater


print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")

led = machine.Pin('LED',machine.Pin.OUT)

while True:
      led.value(1)
      utime.sleep(0.1)
      led.value(0)
      utime.sleep(0.1)
      
