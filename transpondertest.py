import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged, GpsLocationChanged, AirSpeedChanged
import threading
import requests
import time

# IP address of the drone we want to connect to. TODO: Make this depend on input instead of being constant.
DRONEIP = "192.168.42.1"
# Name of the drone we want to connect to. TODO: Make this depend on input instead of being constant.
NAME = "Mihir's ANAFI"
# Decides whether the transponder is active or not. Once it becomes inactive, it must be restarted as a new thread.
broadcasting = True

# Transponder thread which will update the drone's location on the map.
def transponder_thread(drone, tag):
    while (broadcasting):
        try:
            loc = drone.get_state(GpsLocationChanged)
            state = drone.get_state(FlyingStateChanged)
            speed = drone.get_state(AirSpeedChanged)
            payload = {"data": {"tag": tag, "lat": loc["latitude"], "lng": loc["longitude"], "alt": loc["altitude"], "spd": speed["airSpeed"], "state": state["state"]}, "droneid": tag}
            r = requests.post("https://drone-transponder.ue.r.appspot.com/update", json=payload)
            time.sleep(0.1)
        except:
            # This means the data is not available just yet. Olympe will raise a runtime error if any of the
            # get_state() calls fail.
            pass
    # Delete the drone to cleanup.
    r = requests.post("https://drone-transponder.ue.r.appspot.com/delete", json={"droneid": tag})

if __name__ == "__main__":
    drone = olympe.Drone(DRONEIP)
    drone.connect()
    transponder = threading.Thread(target=transponder_thread, args=(drone, NAME))
    # Take off and start the transponder.
    time.sleep(3)
    drone(TakeOff())
    transponder.start()
    drone(FlyingStateChanged(state="hovering", timeout=5)).wait().success()
    # FOR DEMO --- wait so the drone can be found on the map.
    time.sleep(5)
    # Now, complete the flight path (square).
    #drone(moveBy(10, 0, 0, 0) >> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
    #drone(moveBy(0, 10, 0, 0) >> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
    #drone(moveBy(-10, 0, 0, 0) >> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
    #drone(moveBy(0, -10, 0, 0) >> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
    # Land the drone.
    drone(Landing()).wait().success()
    # Turn off the transponder.
    broadcasting = False
    transponder.join()
    drone.disconnect()

