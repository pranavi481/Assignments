class InvalidField(Exception):
      pass
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
        
    @classmethod
    def avg(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        value_list=['student_id__lt','name__lt','age_lt','score_lt','student_id__lt','name__lt','age_lt','score_lt',]
        for key,value in kwargs.items():
            if field not in field_list:
                raise InvalidField
            elif field not in value_list:
                raise InvalidField
            else:
                record=read_data("SELECT avg(age) FROM Student;")
            
    @classmethod
    def min(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        else:
            record=read_data("SELECT min(age) FROM Student;")
            
    @classmethod
    def max(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        else:
            record=read_data("SELECT max(age) FROM Student;")
            
    @classmethod
    def sum(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        else:
            record=read_data("SELECT sum(age) FROM Student;")
    
    @classmethod
    def count(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        else:
            record=read_data("SELECT count(age) FROM Student;")
                
        
        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans