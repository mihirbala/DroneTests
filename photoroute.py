import olympe
from olympe.messages.camera import set_camera_mode, set_photo_mode, take_photo
from olympe.messages.gimbal import set_target, set_offsets, start_offsets_update, stop_offsets_update, offsets, attitude
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing, moveTo, NavigateHome
from olympe.messages.ardrone3.PilotingSettings import MaxTilt
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged, GpsLocationChanged, SpeedChanged, moveToChanged
import olympe.enums.move as mode
import olympe.enums.camera as camera
import olympe.enums.gimbal as gimbal
import time
import math


DRONEIP = "192.168.42.1"

def take_drone_photo(drone, pitch, heading_offset):
    drone(moveBy(0.0, 0.0, 0.0, heading_offset)).wait().success()
    # Move gimbal to proper orientation (pitch variable is what to change)
    drone(set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=pitch,
            roll_frame_of_reference="none",
            roll=0.0,
        )
        >> attitude(pitch_absolute=pitch, _policy="wait", _float_tol=(1e-3, 1e-1))).wait().success()
    # Take photo
    drone(set_camera_mode(0, camera.camera_mode.photo)).wait().success()
    drone(set_photo_mode(0,
            camera.photo_mode.single,
            camera.photo_format.full_frame,
            camera.photo_file_format.jpeg,
            camera.burst_value.burst_14_over_4s,
            camera.bracketing_preset.preset_1ev,
            0.0)).wait().success()
    drone(take_photo(0)).wait().success()
    # Reset gimbal
    drone(set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=0.0,
            roll_frame_of_reference="none",
            roll=0.0,
        )
        >> attitude(pitch_absolute=0.0, _policy="wait", _float_tol=(1e-3, 1e-1))).wait().success()

if __name__ == "__main__":
    drone = olympe.Drone(DRONEIP)
    drone.connect()
    # Move to photo destination
    # Rotate to correct bearing
    drone(TakeOff()).wait().success()
    drone(moveTo(40.4140206, -79.9495953, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4140206, longitude=-79.9495953, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status='DONE')).wait().success()
    take_drone_photo(drone, -90.0, math.pi / 3.0)
    drone(moveTo(40.4137225, -79.9494827, 6.0, mode.orientation_mode.to_target, 0.0)
            >> moveToChanged(latitude=40.4137225, longitude=-79.9494827, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status='DONE')).wait().success()
    take_drone_photo(drone, -15.0, math.pi / 2.0)
    drone(moveTo(40.4137552, -79.9491233, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4137552, longitude=-79.9491233, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status='DONE')).wait().success()
    take_drone_photo(drone, -45.0, math.pi / 4.0)
    drone(NavigateHome(1)).wait().success()
    drone(Landing()).wait().success()
    # Proceed with flight path
    drone.disconnect()
