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
    

class Truck(Car):
    
    sound="Honk Honk"
    
    def __init__(self,color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        self._cargo_weight=0
        self._cargo=0
        if self._max_cargo_weight < 0:
            raise ValueError('Invalid value for max_cargo_weight')
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    def load(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')  
        if self._current_speed==0:
            if self._cargo+cargo_weight<=self._max_cargo_weight:
                self._cargo+= cargo_weight
            elif self._cargo+cargo_weight>self._max_cargo_weight:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
        elif self._cargo+ cargo_weight>self._max_cargo_weight:
            print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))   
        else:
            print("Cannot load cargo during motion")  
    
    def unload(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')  
        elif self._current_speed>0:
            print("Cannot unload cargo during motion")
        else:
            self._cargo-=cargo_weight
    