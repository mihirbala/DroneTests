import olympe
from olympe.messages.camera import set_camera_mode, set_photo_mode, take_photo
from olympe.messages.gimbal import set_target, set_offsets, start_offsets_update, stop_offsets_update, offsets, attitude
import olympe.enums.camera as camera
import olympe.enums.gimbal as gimbal
import time


DRONEIP = "192.168.42.1"

if __name__ == "__main__":
    drone = olympe.Drone(DRONEIP)
    drone.connect()
    # Move to photo destination
    # Rotate to correct bearing
    # Move gimbal to proper orientation (pitch variable is what to change)
    drone(set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=-90.0,
            roll_frame_of_reference="none",
            roll=0.0,
        )
        >> attitude(pitch_absolute=-90.0, _policy="wait", _float_tol=(1e-3, 1e-1))).wait().success()
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
    # Proceed with flight path
    drone.disconnect()
