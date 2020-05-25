class DoesNotExist(Exception):
      pass
class MultipleObjectsReturned(Exception):
      pass
class InvalidField(Exception):
      pass
class Student:
      def __init__(self,name,age,score):
            self.name=name
            self.age=age
            self.score=score
            self.student_id=None
            
      def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)

      @staticmethod
      def get(student_id=0,name='',age=0,score=0,**kwargs):
            membership=[student_id,name,age,score]
            if student_id in membership and student_id!=0:
                  record=read_data(f"SELECT * FROM Student WHERE student_id={student_id}")
            elif name in membership and name!='':
                  record=read_data(f"SELECT * FROM Student WHERE name='{name}'")
            elif age in membership and age!=0:
                   record=read_data(f"SELECT * FROM Student WHERE age={age}")
            elif score in membership and score!=0:
                  record=read_data(f"SELECT * FROM Student WHERE score={score}")
            else:
                  raise InvalidField
            if len(record)==0:
                  raise DoesNotExist
            elif len(record)>1:
                  raise MultipleObjectsReturned
            else:
                  x=Student(record[0][1],record[0][2],record[0][3])
                  x.student_id=record[0][0]
                  return x
                  
      def delete(self):
            record=(f"DELETE FROM Student WHERE student_id={self.student_id}")
            write_data(record)
            
      def save(self):
            import sqlite3
            connection = sqlite3.connect("selected_students.sqlite3")
            crsr = connection.cursor()
            crsr.execute("PRAGMA foreign_keys=on;") 
            if self.student_id == None:
                  crsr.execute(f"INSERT INTO Student(name,age,score) VALUES ('{self.name}',{self.age},{self.score})") 
                  self.student_id=crsr.lastrowid
            else:
                  if self.checking(self.student_id):
                        crsr.execute(f"UPDATE Student SET name='{self.name}',age={self.age},score={self.score} WHERE student_id={self.student_id}")
                  else:
                        if self.checking(self.student_id):
                              crsr.execute(f"UPDATE Student SET name='{self.name}',age={self.age},score={self.score} WHERE student_id={self.student_id}")
                        else:
                              crsr.execute(f"INSERT INTO Student(student_id,name,age,score) VALUES ({self.student_id},'{self.name}',{self.age},{self.score})") 
            connection.commit() 
            connection.close()
      
      @staticmethod
      def checking(student_id):
            query=read_data(f"SELECT student_id FROM Student WHERE student_id={student_id}")
            if len(query)!=0:
                  return True
            else:
                  return False
      
      @staticmethod            
      def filter(**kwargs):
            field_list=['student_id','name','age','score']
            for key,value in kwargs.items():
                  k=key
                  v=value
            field=k.split("__")
            #print(field)
            if field[0] not in field_list:
                  raise InvalidField  
            elif k in field_list:
                  if field[0]!='name':
                        record=read_data(f"SELECT * FROM Student WHERE {k}={v}") 
                  else:
                        record=read_data(f"SELECT * FROM Student WHERE {field[0]}='{v}'") 
            elif field[0] in field_list and field[1]=='lt':
                  record=read_data(f"SELECT * FROM Student WHERE {field[0]}<{v}")
            elif field[0] in field_list and field[1]=='lte':
                  record=read_data(f"SELECT * FROM Student WHERE {field[0]}<={v}")
            elif field[0] in field_list and field[1]=='gt':
                  record=read_data(f"SELECT * FROM Student WHERE {field[0]}>{v}")
            elif field[0] in field_list and field[1]=='gte':
                  record=read_data(f"SELECT * FROM Student WHERE {field[0]}>={v}")
            elif field[0] in field_list and field[1]=='neq':
                  if field[0]!='name':
                        record=read_data(f"SELECT * FROM Student WHERE {field[0]}!={v}") 
                  else:
                        record=read_data(f"SELECT * FROM Student WHERE {field[0]}!='{v}'")
            elif field[0] in field_list and field[1]=='in':
                  record=read_data(f"SELECT * FROM Student WHERE {field[0]} in {tuple(v)}")
            elif field[0] in field_list and field[1]=='contains':
                  record=read_data(f"SELECT * FROM Student WHERE name like '%{v}%'")
             
            record_list=[]    
            if len(record)>0:
                  for i in record:
                        x=Student(i[1],i[2],i[3])
                        x.student_id=i[0]
                        record_list.append(x)
                  return record_list
            else:
                  return record_list
      
      '''@staticmethod
      def filter(**kwargs):
            out=[]
            for key,value in kwargs.items():
                  if (key=='age' or key=='score' or key=='student_id' or key=='name'):
                        record=(f"SELECT * FROM Student WHERE {key}='{value}'")
                  elif (key=='age__lt' or key=='score__lt' or key=='student_id__lt' or key=='name'):
                        k=key.split("__")
                        record=(f"SELECT * FROM Student WHERE {k[0]}<{value}")
                  elif (key=='age__lte' or key=='score__lte' or key=='student_id__lte' or key=='name'):
                        k=key.split("__")
                        record=(f"SELECT * FROM Student WHERE {k[0]}<={value}")
                  elif (key=='age__gt' or key=='score__gt' or key=='student_id__gt' or key=='name'):
                        k=key.split("__")
                        record=(f"SELECT * FROM Student WHERE {k[0]}>{value}")
                  elif (key=='age__gte' or key=='score__gte' or key=='student_id__gte' or key=='name'):
                        k=key.split("__")
                        record=(f"SELECT * FROM Student WHERE {k[0]}>={value}")
                  elif (key=='age__neq' or key=='score__neq' or key=='student_id__neq' or key=='name__neq'):
                        k=key.split("__")
                        record=(f"SELECT * FROM Student WHERE {k[0]}!='{value}'")
                  elif (key=='age__in' or key=='score__in' or key=='student_id__in' or key=='name__in'):
                        value=tuple(value)
                        k=key.split("__")
                        record=(f"SELECT * FROM Student WHERE {k[0]} in {value}")
                  elif (key=='name__contains'):
                        record=(f"SELECT * FROM Student WHERE name like '%{value}'")
                  else:
                        raise InvalidField
                  results=read_data(record)
                  for i in results:
                        student_obj=Student(i[1],i[2],i[3])
                        student_obj.student_id=i[0]
                        out.append(student_obj)
            return out'''
          
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()      
                        
def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans      



        
