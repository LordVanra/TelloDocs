import threading
from djitellopy import Tello
import cv2
import time

# Sometimes the connections breaks or the battery is low, so we try to send the command multiple times
def sendCommand(command, maxTries=8):
    try:
        command()
    except Exception as E:
        if maxTries > 0:
            sendCommand(command, maxTries - 1)
        else:
            print(f"Error: {E}")

# No matter what, we never want to stop sending a land command if we want to land
# Otherwise, the drone will just hover in the air and it is NOT FUN
def emergency_land():
    try:
        drone.land()
    except Exception as E:
        emergency_land()

drone = None

try:
    drone = Tello()
    drone.connect()
    time.sleep(2)

    # Movement commands
    drone.takeoff()
    time.sleep(2)

    # Check battery
    # Battery must be greater than 20% for most commands and greater than 50% (?) for flips
    battery = drone.get_battery()
    print(f"Battery level: {battery}%")

    sendCommand(lambda: drone.move_up(50))
        
    time.sleep(5)

    print("Landing...")
    drone.land()
    drone.end()

except Exception as E:
    drone.emergency_land()