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
            connection = sqlite3.connect("students.sqlite3")
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
                  
      def filter(self):
            li=[]
            if self.student_id==None:
                  return li
                  
                
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



'''student_object = Student.get(student_id=1)
student_object.student_id
#1
print(student_object.name)
#Raj
print(student_object.age)
#20
print(student_object.score)
#100
student_object = Student.get(student_id=1)
print(student_object.delete())
student_object = Student(name="Rajini", age=19, score=95)
print(student_object.save())'''