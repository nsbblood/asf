class Motorcycle:  #python classes are capitilized
    is_engine_on=False
    is_headlight_on=False
    make= None
    model= None
    isDriving= False



    def __init__(self,make,model):
        self.make=make
        self.model=model

    def __repr__(self): #learn more here!!!
        return(f'{self.make} {self.model} with engine '
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

    def lean(self,direction):
        if not self.isDriving:
            print('You leaned while not driving and crushed')
            return
        
        print(f'leaning {direction}')

    def turn_handlebars(self,direction):
        print(f'Turning handlebars {direction}')

    def turn(self,direction):
        if direction=='Left':
            self.turn_handlebars('right')
            self.lean('left')
            
        elif direction=='right':
            self.turn_handlebars('left')
            self.lean('right')
        else:
            print("Didn't understand that direction")


   


moto =Motorcycle('BMW','Moto')  # we are assigning it to moto variable
print(moto)
moto.turn_engine_on()
moto.turn_headlight_on()
moto.start_driving()
moto.turn('left')
moto.turn('right')
print(moto)
moto.stop_driving()
moto.turn_engine_off()
moto.turn_headlight_off()

