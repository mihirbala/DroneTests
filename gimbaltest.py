import olympe
from olympe.messages import gimbal, camera
import requests

DRONE_IP = "192.168.42.1"

if __name__ == "__main__":
    with olympe.Drone(DRONE_IP) as drone:
        drone.connect()
        cameraAction = drone(gimbal.set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=-45.0,
            roll_frame_of_reference="none",
            roll=0.0,
        )).wait()
        if not cameraAction.success():
            assert False
        r = requests.get("https://www.google.com")
        print("REQUEST JSON: {0}".format(r.status_code))
        drone.disconnect()

