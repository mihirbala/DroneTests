import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo
import olympe.enums.move as mode
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged, moveToChanged
if __name__ == "__main__":
	IP = "192.168.42.1"
	drone = olympe.Drone(IP)
	drone.connect()
	drone(TakeOff()>> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
	drone(moveTo(40.4154519, -79.9491731, 5.0, mode.orientation_mode.to_target, 0.0) >> moveToChanged(latitude=40.4154519, longitutde=-79.9491731, altitude=5.0, orientation_mode=mode.orientation_mode.to_target, status='DONE', _policy='wait') >> FlyingStateChanged(state="hovering", _timeout=5)).wait().success()
	drone(Landing()).wait().success()
	drone.disconnect()
