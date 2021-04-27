import olympe

DRONEIP = "192.168.42.1"

if __name__ == "__main__":
    drone = olympe.Drone(DRONEIP)
    drone.connect()
    drone.disconnect()
