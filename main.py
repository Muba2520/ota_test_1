# This is a test file of the OTA code
import utime
from ota import OTAUpdater
from machine import Timer,Pin

SSID = "Particle"
PASSWORD = "Test@0115"
firmware_url = "https://github.com/Muba2520/ota_test_1/"

ota_updater = OTAUpdater(SSID,PASSWORD,firmware_url,"main.py")
# Define a callback function that will be called by the timer interrupt
def timer_callback(timer):
    ota_updater.download_and_install_update_if_available()

# Create a timer object
timer = Timer()

# Configure the timer to call the timer_callback function every 5 minute (300000 ms)
timer.init(period=300000, mode=Timer.PERIODIC, callback=timer_callback)


print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")

led = machine.Pin('LED',machine.Pin.OUT)

while True:
      led.value(1)
      utime.sleep(0.2)
      led.value(0)
      utime.sleep(0.2)
      
