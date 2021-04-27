import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
import time

DRONE_IP = "192.168.42.1"

if __name__ == "__main__":
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    drone(TakeOff() >> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
    drone(moveBy(10, 0, 0, 0) >> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
    drone(Landing()).wait().success()
    drone.disconnect()
