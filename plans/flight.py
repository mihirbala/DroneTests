import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, MoveTo
if __name__ == "__main__":
	IP = 192.168.42.1
	drone = olympe.Drone(IP)
	drone.connect()
	drone(TakeOff()).wait().success()
	drone(moveTo(40.4154519, -79.9491731, 10.0, 1, 0.0, 2.0, 1.0, 10.0)).wait().success
	drone(moveTo(40.4153334, -79.9497565, 10.0, 1, 0.0, 2.0, 1.0, 10.0)).wait().success
	drone(moveTo(40.4152466, -79.9494252, 10.0, 1, 0.0, 2.0, 1.0, 10.0)).wait().success
	drone(moveTo(40.4150342, -79.9496116, 10.0, 1, 0.0, 2.0, 1.0, 10.0)).wait().success
	drone(moveTo(40.4151537, -79.9490484, 10.0, 1, 0.0, 2.0, 1.0, 10.0)).wait().success
	drone(moveTo(40.4154519, -79.9491731, 10.0, 1, 0.0, 2.0, 1.0, 10.0)).wait().success
	drone(Landing()).wait().success()
	drone.disconnect()
