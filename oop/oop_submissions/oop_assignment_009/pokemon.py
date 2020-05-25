class Pokeman:
      
      sound=''
      running=''
      flying=''
      swimming=''
      def __init__(self,name,level):
            self._name=name
            self._level=level
            self._magnitude_attack=0
            if self._name=='':
                  raise ValueError('name cannot be empty')
            if self._level<=0:
                  raise ValueError('level should be > 0')
            self._master=None
            
      @property
      def master(self):
            if self._master==None:
                  print("No Master")
            else:
                  return self._master
      @property
      def name(self):
            return self._name
      @property
      def level(self):
            return self._level
      @property
      def magnitude_attack(self):
            return self._magnitude_attack
      
      def __str__(self):
            return '{} - Level {}'.format(self._name,self._level)
      
      @classmethod      
      def make_sound(cls):
            print(cls.sound)
      @classmethod
      def run(cls):
            print(cls.running)
      @classmethod
      def fly(cls):
            print(cls.flying)
      @classmethod
      def swim(cls):
            print(cls.swimming)
            
      def attack(self):
           self._magnitude_attack+=10*self.level 
           print('Electric attack with {} damage'.format(self._magnitude_attack))

class Pikachu(Pokeman):
      
      sound='Pika Pika'
      running='Pikachu running...'
      
class Squirtle(Pokeman):
      
      sound='Squirtle...Squirtle'
      running='Squirtle running...'
      swimming='Squirtle swimming...'
            
      def attack(self):
           self._magnitude_attack+=9*self.level 
           print('Water attack with {} damage'.format(self._magnitude_attack))
          
class Pidgey(Pokeman):
      
      sound='Pidgey...Pidgey'
      flying='Pidgey flying...'

      def attack(self):
           self._magnitude_attack+=5*self.level 
           print('Air attack with {} damage'.format(self._magnitude_attack))

class Swanna(Pokeman):
      
      sound='Swanna...Swanna'
      flying='Swanna flying...'
      swimming='Swanna swimming...'      
            
      def attack(self):
           self._magnitude_attack+=9*self.level 
           print('Water attack with {} damage'.format(self._magnitude_attack))
           self._magnitude_attack=0
           self._magnitude_attack+=5*self.level 
           print('Air attack with {} damage'.format(self._magnitude_attack))   
 
class Zapdos(Pokeman):
      
      sound='Zap...Zap'
      flying='Zapdos flying...'
            
      def attack(self):
           self._magnitude_attack+=10*self.level 
           print('Electric attack with {} damage'.format(self._magnitude_attack))
           self._magnitude_attack=0
           self._magnitude_attack+=5*self.level 
           print('Air attack with {} damage'.format(self._magnitude_attack))    
    
class Island:
      island_list=[]
      def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
            self._name=name
            self._max_no_of_pokemon=max_no_of_pokemon
            self._total_food_available_in_kgs=total_food_available_in_kgs
            self._pokemon_left_to_catch=0
            self.pokeman_list=[]
            self.island_list.append(self)
            
      @property
      def name(self):
          return self._name
      @property
      def max_no_of_pokemon(self):
            return self._max_no_of_pokemon
      @property
      def total_food_available_in_kgs(self):
            return self._total_food_available_in_kgs
      @property
      def pokemon_left_to_catch(self):
            return self._pokemon_left_to_catch
      
      def __str__(self):
            return '{} - {} pokemon - {} food'.format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
    
      def add_pokemon(self,pokeman):
            self.pokeman_list.append(pokeman)
            if len(self.pokeman_list)<=self.max_no_of_pokemon:
                self._pokemon_left_to_catch+=1  
            else:
                  print('Island at its max pokemon capacity')
      
      @classmethod    
      def get_all_islands(cls):
            return cls.island_list
          
class Trainer:
      def __init__(self,name):
            self._name=name
            self._experience=100
            self._max_food_in_bag=10*self._experience
            self._food_in_bag=0
            self._current_island=None
            self.pokeman_list=[]
      @property
      def name(self):
            return self._name
      @property
      def experience(self):
            return self._experience
      @property
      def max_food_in_bag(self):
            return self._max_food_in_bag
      @property
      def food_in_bag(self):
            return self._food_in_bag
      def __str__(self):
            return '{}'.format(self._name)
      @property
      def current_island(self):
            if self._current_island==None:
                  print('You are not on any island')
            else:
                  return self._current_island
                  
      def move_to_island(self,island):
            self._current_island=island
                  
      def collect_food(self):
            if self._current_island==None or self.current_island._total_food_available_in_kgs==0:
                  print('Move to an island to collect food')
            elif self.current_island._total_food_available_in_kgs<self._max_food_in_bag:
                 self._food_in_bag=self.current_island._total_food_available_in_kgs
                 self.current_island._total_food_available_in_kgs=0
            elif self._food_in_bag==self._max_food_in_bag:
                  self._food_in_bag=self._food_in_bag
                  self.current_island._total_food_available_in_kgs=self.current_island._total_food_available_in_kgs
            else:
                  self.current_island._total_food_available_in_kgs=self.current_island._total_food_available_in_kgs-self._max_food_in_bag 
                  self._food_in_bag=self._max_food_in_bag
            
      def catch(self,poke):
            if self._experience>=100*poke.level:
                  self.pokeman_list.append(poke)
                  print('You caught {}'.format(poke.name))
                  self._experience+=poke.level*20
                  poke._master=self
            else:
                  print('You need more experience to catch {}'.format(poke.name))

      def get_my_pokemon(self):
            return self.pokeman_list
            
 
 

 

