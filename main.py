# This is a test file of the OTA code
from machine import Pin
import utime
from ota import OTAUpdater


print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")



SSID = "Particle"
PASSWORD = "Test@0115"

firmware_url = "https://github.com/Muba2520/ota_test_1/"
ota_updater = OTAUpdater(SSID,PASSWORD,firmware_url,"main.py")

led = Pin(2,Pin.OUT)
time1 = utime.time()
print(time1)

def check_update(timer):   
      ota_updater.download_and_install_update_if_available()

timer = machine.Timer(0)
timer.init(period=10000, mode=machine.Timer.PERIODIC, callback=check_update)


while True: 
   
      
   for i in range(10):
      led.value(1)
      utime.sleep(0.5)
      led.value(0)
      utime.sleep(0.5)
