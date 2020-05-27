class InvalidField(Exception):
      pass
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
        
    @classmethod   
    def filter(cls,**kwargs):
        dic={'neq':'!=','lt':'<','lte':'<=','gt':'>','gte':'>=','in':'in','contains':'contains'}
        l=[]
        for k,v in kwargs.items():
            key=k.split("__")
            if key[0] not in ['student_id','name','age','score']:
                raise InvalidField
            if len(key)==1:
                dt=f"{k}='{v}'"
            elif key[1]=='contains':
                dt=f"{key[0]} like '%{v}%'"
            elif key[1]=='in':
                dt=f"{key[0]} {dic[key[1]]} {tuple(v)}"
            else:
                dt=f"{key[0]} {dic[key[1]]} '{v}'"
            l.append(dt)
            temp=' and '.join(l)
            query=' '+temp
        return query
        
    @classmethod
    def avg(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        
        if len(kwargs)>=1:
            condition=Student.filter(**kwargs)
            record=(f"SELECT avg({field}) from Student WHERE {condition};")
        else:
            record=(f"SELECT avg({field}) from Student;")
        return read_data(record)[0][0]
        
    @classmethod
    def min(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        
        if len(kwargs)>=1:
            condition=Student.filter(**kwargs)
            record=(f"SELECT min({field}) from Student WHERE {condition};")
        else:
            record=(f"SELECT min({field}) from Student;")
        return read_data(record)[0][0]
        
    @classmethod
    def max(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
            
        if len(kwargs)>=1:
            condition=Student.filter(**kwargs)
            record=(f"SELECT max({field}) from Student WHERE {condition};")
        else:
            record=(f"SELECT max({field}) from Student;")
        return read_data(record)[0][0]
    
    @classmethod
    def sum(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        else:
            if len(kwargs)>=1:
                condition=Student.filter(**kwargs)
                record=(f"SELECT sum({field}) from Student WHERE {condition};")
            else:
                record=(f"SELECT sum({field}) from Student;")
        return read_data(record)[0][0]
    
    @classmethod
    def count(cls,field=None,**kwargs):
        field_list=['student_id','name','age','score']
        if field==None:
            record="SELECT count() FROM Student"
        elif field not in field_list:
            raise InvalidField
        else:
            if len(kwargs)>=1:
                condition=Student.filter(**kwargs)
                record=(f"SELECT count({field}) from Student WHERE {condition};")
            else:
                record=(f"SELECT count({field}) from Student;")
        return read_data(record)[0][0]

        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
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
	