class Car:
    sound="Beep Beep"
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self._color=color
        self._max_speed=max_speed 
        if self._max_speed < 0:
            raise ValueError('Invalid value for max_speed')
        self._acceleration=acceleration
        if self._acceleration<0:
            raise ValueError('Invalid value for acceleration')
        self._tyre_friction=tyre_friction
        if self._tyre_friction<0:
            raise ValueError('Invalid value for tyre_friction')
        self._is_engine_started=False
        self._current_speed=0
        
    @property
    def color(self):
        return self._color
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def current_speed(self):
        return self._current_speed
     
    def start_engine(self):
        self._is_engine_started=True 
        
    def accelerate(self) :
        if self._is_engine_started==True:
            if self._max_speed>self._current_speed+self._acceleration:
                self._current_speed+=self._acceleration
            else:
                self._current_speed=self._max_speed
        else:
            print('Start the engine to accelerate')
    
    def apply_brakes(self):
        self._current_speed-=self._tyre_friction
        if self._current_speed<0:
            self._current_speed=0
        
    def sound_horn(self):
        if self._is_engine_started==True:
            print(self.sound)
        else:
            print('Start the engine to sound_horn')
    
    def stop_engine(self):
        self._is_engine_started=False

import math    

class RaceCar(Car):
    sound="Peep Peep\nBeep Beep"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
    
    @property
    def nitro(self):
        return self._nitro

        
    def apply_brakes(self):
        if self._current_speed>self._max_speed/2:
            self._nitro+=10
        super().apply_brakes()
            
    def accelerate(self):
        if self._nitro!=0:
            self._current_speed+=math.ceil(0.3*self._acceleration)
            self._nitro-=10
        super().accelerate()
        
    '''def sound_horn(self):
        if self._is_engine_started==True:
            print("Peep Peep")
            print("Beep Beep")
        else:
            print('Start the engine to sound_horn')'''
            
            

    
    
        