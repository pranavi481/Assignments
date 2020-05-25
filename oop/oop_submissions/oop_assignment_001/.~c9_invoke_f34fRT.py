class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed 
        if max_speed < 0:
            raise ValueError('Invalid value for max_speed')
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_stared=False
        self.current_speed=0
    def start_engine(self):
       self.is_engine_stared=True
    
    def accelerate(self) :
        if self.max_speed>=self.current_speed:
                self.current_speed+=self.acceleration
        else:
            print('Start the engine to accelerate')
            
    def apply_brakes(self):
        self.current_speed-=self.tyre_friction
        
    def sound_horn(self):
        if self.is_engine_stared==True:
            return 'Beep Beep'
        else:
            print('Start the engine to sound_horn')
    def stop_engine(self):
        self.is_engine_stared=False