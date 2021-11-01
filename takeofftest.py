import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
import time

DRONE_IP = "192.168.42.1"
SKYCTRL_IP = "192.168.53.1"

if __name__ == "__main__":
    #drone = olympe.Drone(DRONE_IP, is_skyctrl=True)
    drone = olympe.Drone(SKYCTRL_IP)
    drone.connect()
    drone(TakeOff()).wait().success()
    time.sleep(10)
    drone(Landing()).wait().success()
    drone.disconnect()
