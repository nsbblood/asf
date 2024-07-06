class Vehicle:
    is_engine_on=False
    is_headlight_on=False
    make= None
    model= None
    isDriving= False



    def __init__(self,make,model):
        self.make=make
        self.model=model

    def __repr__(self): #learn more here!!
        return(f'{self.make} {self.model} with meine schatzzz with engine '
               f'{"on" if self.is_engine_on else "off" }'
               f' and headhlight {"on" if self.is_engine_on else "off"}')

    def turn_engine_on(self):
        print('Turning engine on')
        self.is_engine_on=True

    def turn_engine_off(self):
        print('Turning engine off')
        if self.isDriving:
            print('You tried to turn off the engine and '
                  'crushed')

            return

        self.is_engine_on=False


    def turn_headlight_on(self):
        print('Turning headlight on')
        self.is_headlight_on=True

    def turn_headlight_off(self):
        print('Turning headlights off')
        self.is_engine_on=False

    def start_driving(self):
        if not self.is_engine_on:
            print("You can't drive without turning the engine on!")
            return
        
        print('Starting to drive')
        self.isDriving=True

    def stop_driving(self):
        print('Stopping')
        self.isDriving=False



class Car(Vehicle):  #python classes are capitilized
   

    def turn_steering_wheel(self, direction):
        print(f'Turning steering wheel {direction}')

    def turn(self, direction):
        if direction in ['left', 'right']:
            self.turn_steering_wheel(direction)
        else:
            print("Didn't understand that direction")


class Motorcycle(Vehicle):


  def lean(self,direction):
     if not self.isDriving:
            print('You leaned while not driving and crushed')
            return
        
     print(f'leaning {direction}')

  def turn_handlebars(self, direction):
        print(f"Turning handlebars {direction}")

  def turn(self, direction):
        if direction in ["left", "right"]:
            self.turn_handlebars(direction)
            self.lean(direction)  # Assuming you have a 'lean' method
        else:
            print("Didn't understand that direction")



#car =Car('BMW','m4')  # we are assigning it to moto variable
#moto=Motorcycle('BMW','Wow')

#for vehicle in [moto,car]:
#    print(vehicle)
#    vehicle.turn_engine_on()
#    vehicle.turn_headlight_on()
#    vehicle.start_driving()
#    vehicle.turn('left')
#    vehicle.turn('right')
#    vehicle.stop_driving()
#    vehicle.turn_engine_off()
#    vehicle.turn_headlight_off()
#    print() #this is a blank...


   

#Bisiklet(Moving) in this case bicycle inherits from moving
#so it takes Moving class' attributes and methods