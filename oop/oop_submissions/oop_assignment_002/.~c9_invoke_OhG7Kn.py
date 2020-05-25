class Car:
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
            print("Beep Beep")
        else:
            print('Start the engine to sound_horn')
    
    def stop_engine(self):
        self._is_engine_started=False
    

class Truck(Car):
    def __init__(self,color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self.current_speed=0
        self.is_engine_started=False
        '''self.load=0
        if self.load<0:
            raise ValueError('Invalid value for cargo_weight')'''
    def sound_horn(self):
        if is_engine_started==True
        
        