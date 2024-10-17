# This is a test file of the OTA code
import utime
import machine
from ota import OTAUpdater


print('Hello World')
print("Hello")
print("this is another line test, written on an iPad using VS Code for web.")



SSID = "Particle"
PASSWORD = "Test@0115"

firmware_url = "https://github.com/Muba2520/ota_test_1/"
ota_updater = OTAUpdater(SSID,PASSWORD,firmware_url,"main.py")

led = machine.Pin(2,machine.Pin.OUT)
time1 = utime.time()
print(time1)

def check_update(timer):   
      ota_updater.download_and_install_update_if_available()

timer = machine.Timer(0)
timer.init(period=10000, mode=machine.Timer.PERIODIC, callback=check_update)


while True: 
      led.value(1)
      utime.sleep(0.1)
      led.value(0)
      utime.sleep(0.1)
