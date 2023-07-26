#!/usr/bin/env python
import time
from flyt_python import api

# instance of flyt droneigation class
drone = api.navigation(timeout=120000)  

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print ("taking off")
drone.take_off(10.0)

print ("flying in triangle")
drone.position_set(10.0, 0, 0, relative=True)
drone.position_set(-5.0, 8.66, 0, relative=True)
drone.position_set(-5.0, -8.66, 0, relative=True)

print ("landing")
drone.land(False)
print ("mission complete!")

# shutdown the instance
drone.disconnect()
