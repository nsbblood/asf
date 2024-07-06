import time
import pytest
from classes1 import Motorcycle 
from classes1 import Car

car =Car('BMW','m4')  # we are assigning it to moto variable
moto=Motorcycle('BMW','Wow')
car1=Car('Bmw','m5')
moto2=Motorcycle('Kawazaki','The best')
for vehicle in [moto,car,car1,moto2]:  # I have added other objects later.
    print(f'The time is {time.time()}')
    print(vehicle)    
    vehicle.turn_engine_on()
    vehicle.turn_headlight_on()
    vehicle.start_driving()
    vehicle.turn('left')
    vehicle.turn('right')
    vehicle.stop_driving()
    vehicle.turn_engine_off()
    vehicle.turn_headlight_off()   
    print() #this is a blank...
    time.sleep(1) # We imported time so we can use it's features. 
