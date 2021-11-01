#/usr/bin/python3
import olympe
import time
import math
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy
from olympe.messages.ardrone3.PilotingState import GpsLocationChanged
from olympe.messages.gimbal import set_target


if __name__ == "__main__":
        
    #eventually IP will be specified depending on what drone is chosen
    IP = "192.168.53.1" 
    drone = olympe.Drone(IP)
    drone.connect()
    drone(TakeOff()).wait().success()

    time.sleep(5)

    # Move up 2 meters
    drone(moveBy(0, 0, -2, 0)).wait().success()
    # Shift gimbal down
    drone(set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=-34,
            roll_frame_of_reference="none",
            roll=0.0,
        )
        >> attitude(pitch_absolute=-34, _policy="wait", _float_tol=(1e-3, 1e-1))).wait().success()
    # Time sleep
    time.sleep(5)
    # Reset Gimbal
    drone(set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=0,
            roll_frame_of_reference="none",
            roll=0.0,
        )
        >> attitude(pitch_absolute=0, _policy="wait", _float_tol=(1e-3, 1e-1))).wait().success()
    
    ## NOTE: MOVE UP

    # Move up 2 meters
    drone(moveBy(0, 0, -2, 0)).wait().success()
    # Shift gimbal down
    drone(set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=-54,
            roll_frame_of_reference="none",
            roll=0.0,
        )
        >> attitude(pitch_absolute=-54, _policy="wait", _float_tol=(1e-3, 1e-1))).wait().success()
    # Time sleep
    time.sleep(5)
    # Reset Gimbal
    drone(set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=0,
            roll_frame_of_reference="none",
            roll=0.0,
        )
        >> attitude(pitch_absolute=0, _policy="wait", _float_tol=(1e-3, 1e-1))).wait().success()


    drone(Landing()).wait().success()
    drone.disconnect()
