import olympe
from olympe.messages.camera import set_camera_mode, take_photo

DRONEIP = "192.168.42.1"

if __name__ == "__main__":
    drone = olympe.Drone(DRONEIP)
    drone.connect()
    drone(set_camera_mode(cam_id=0, value=1) >> take_photo(cam_id=0)).wait().success()
    drone.disconnect()
