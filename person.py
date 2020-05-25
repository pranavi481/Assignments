#class Person:
 #   pass
#class Person:
    #def say_hello(self):
       # print("Hello")
        #print(self)
#class Person:
 #   def greet(self,name='Person'):
  #      return "Hello {}".format(name)
'''class Person:
    def __init__(self,name):
        print("Hello, I'm {}!".format(name))
    def say_hello(self):
        print("Hii")'''
'''class Person:
    def __init__(self,full_name):
        self.name=full_name'''
class String:
    def __init__(self,string):
        self.string=string
    def __repr__(self,other):
        return 'object:{}'.format(self.string)
strn=String("pranavi")
print(strn.string)
        
        