class Animal:
      sound=''
      age_grow=0
      def __init__(self,age_in_months,breed,required_food_in_kgs):
            self._age_in_months=age_in_months
            if self._age_in_months!=1:
                  raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
            self._breed=breed
            self._required_food_in_kgs=required_food_in_kgs
            if self._required_food_in_kgs<=0:
                  raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
      @property
      def age_in_months(self):
            return self._age_in_months
      @property
      def breed(self):
            return self._breed
      @property
      def required_food_in_kgs(self):
            return self._required_food_in_kgs
            
      def grow(self):
            self._age_in_months+=1
            self._required_food_in_kgs+=self.age_grow
            
      @classmethod      
      def make_sound(cls):
            print(cls.sound)
            
class LandAnimal:   
      @classmethod
      def breathe(cls):
            print("Breathe in air")
            
class WaterAnimal:
      @classmethod
      def breathe(cls):
            print("Breathe oxygen from water")
            
class HuntingAnimals:
      def hunt(self,hunts):
            count=0
            for animal in hunts.zoo_list:
                  if animal.__class__==Deer:
                        count+=1
                        hunts.zoo_list.remove(animal)
            if count==0:
                  print('No deers to hunt')
            
class Deer(Animal,LandAnimal):
      age_grow=2
      sound="Buck Buck"
      
class Lion(Animal,LandAnimal,HuntingAnimals):
      age_grow=4
      sound="Roar Roar"
      
class Shark(Animal,WaterAnimal):
      age_grow=8
      sound="Shark Sound"
      def hunt(self,hunts):
            count=0
            for animal in hunts.zoo_list:
                  if animal.__class__==GoldFish:
                        count+=1
                        hunts.zoo_list.remove(animal)
            if count==0:
                  print('No GoldFish to hunt')
      
class GoldFish(Animal,WaterAnimal):
      age_grow=0.2
      sound="Hum Hum"
      
class Snake(Animal,LandAnimal,HuntingAnimals):
      age_grow=0.5
      sound="Hiss Hiss"
      
class Zoo:
      total_animals_in_all_zoos=[]
      def __init__(self):
            self._reserved_food_in_kgs=0
            self.zoo_list=[]
            
      @property
      def reserved_food_in_kgs(self):
            return self._reserved_food_in_kgs
      
      def add_food_to_reserve(self,food):
            self._reserved_food_in_kgs+=food
            
      def count_animals(self):
          return len(self.zoo_list)

      def add_animal(self,animal):
           self.zoo_list.append(animal)
           self.total_animals_in_all_zoos.append(animal)
            
      def feed(self,animal):
            feed_required=animal._required_food_in_kgs
            if self._reserved_food_in_kgs>0:
                  self._reserved_food_in_kgs-=feed_required   
                  animal.grow()
                  
      @staticmethod
      def count_animals_in_given_zoos(zoos_animals):
            count=0
            for animal in zoos_animals:
                  count+=animal.count_animals()
            return count
      
      @classmethod
      def count_animals_in_all_zoos(cls):
            return len(cls.total_animals_in_all_zoos)
      

      