#/usr/bin/python3
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo
import olympe.enums.move as mode
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged, moveToChanged
from olympe.enums.ardrone3.PilotingState import MoveToChanged_Status as status

if __name__ == "__main__":
        
    #eventually IP will be specified depending on what drone is chosen
    IP = "192.168.42.1" 
    drone = olympe.Drone(IP)
    drone.connect()
    drone(TakeOff()).wait().success()
    
    drone(
        moveTo(40.4153709, -79.949308, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4153709, longitude=-79.949308, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(
        moveTo(40.4155755, -79.9494166, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4155755, longitude=-79.9494166, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(
        moveTo(40.4152855, -79.949717, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4152855, longitude=-79.949717, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(
        moveTo(40.4153709, -79.949308, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4153709, longitude=-79.949308, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(
        moveTo(40.4153702, -79.9493077, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4153702, longitude=-79.9493077, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(
        moveTo(40.4150833, -79.9496285, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4150833, longitude=-79.9496285, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(
        moveTo(40.4151711, -79.949202, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4151711, longitude=-79.949202, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(
        moveTo(40.4153702, -79.9493077, 6.0, mode.orientation_mode.to_target, 0.0)
        >> moveToChanged(latitude=40.4153702, longitude=-79.9493077, altitude=6.0, orientation_mode=mode.orientation_mode.to_target, status=status.DONE)
    ).wait().success()
    
    drone(Landing()).wait().success()
    drone.disconnect()
