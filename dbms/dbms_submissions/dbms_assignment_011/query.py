Q1='''SELECT Actor.id,fname,lname,gender FROM Actor INNER JOIN Cast ON `Actor`.`id`=`Cast`.`pid` 
      INNER JOIN Movie ON `Movie`.`id`=`Cast`.`mid` 
      WHERE name LIKE 'Annie%';'''
      
Q2='''SELECT m.id,name,rank,year FROM Movie as m INNER JOIN MovieDirector as md ON
      m.id=md.mid INNER JOIN Director as d ON d.id=md.did WHERE d.fname='Biff'
      AND d.lname='Malibu' AND year IN (1999, 1994, 2003) ORDER BY rank DESC,year ASC;'''

Q3='''SELECT year,COUNT(id) as no_of_movies FROM Movie GROUP BY year HAVING
      (SELECT AVG(rank) FROM Movie)<AVG(rank) ORDER BY year ASC;'''
      
Q4='''SELECT * FROM Movie WHERE year = 2001 AND rank<(SELECT AVG(rank) FROM Movie )
      ORDER BY rank DESC LIMIT 10;'''
      
"""Q5='''SELECT m.id as movie_id,COUNT(gender='F') AS no_of_female_actors,COUNT(gender='M') AS no_of_male_actors
      FROM Actor as a INNER JOIN Cast as c ON a.id=c.pid
      INNER JOIN Movie as m ON c.mid=m.id GROUP BY m.id ORDER BY m.id ASC LIMIT 100;''' """ 
  
Q6='''SELECT DISTINCT a.id FROM Actor as a INNER JOIN Cast as c ON a.id=c.pid
      INNER JOIN Movie as m ON m.id=c.mid GROUP BY a.id,m.id HAVING COUNT(DISTINCT role) >1 ORDER BY a.id ASC LIMIT 100;'''  
   
Q7="SELECT fname,COUNT(id) FROM Director GROUP BY fname HAVING COUNT(fname)>1;"      
      
Q8='''SELECT id,fname,lname FROM Director as d INNER JOIN MovieDirector as md ON d.id=md.mid
      INNER JOIN Cast as c ON md.mid=c.mid
      GROUP BY d.id HAVING COUNT(DISTINCT c.pid)>100;'''
"""      
Q5='''SELECT m.id as movie_id,(SELECT COUNT(gender) FROM Actor as a INNER JOIN Cast as c ON a.id=c.pid WHERE gender='F' AND c.mid=m.id) AS no_of_female_actors,
      (SELECT COUNT(gender) FROM Actor as a INNER JOIN Cast as c ON a.id=c.pid WHERE gender='M' AND c.mid=m.id) AS no_of_male_actors
      FROM Movie as m ORDER BY m.id ASC LIMIT 100;''' """
       
Q8='''SELECT id,fname,lname FROM Director as d
      WHERE EXISTS(SELECT * FROM MovieDirector as md INNER JOIN Cast as c ON md.mid=c.mid WHERE d.id=md.did
      GROUP BY md.did HAVING COUNT(DISTINCT c.pid)>=100)
      AND NOT EXISTS(SELECT * FROM MovieDirector as md INNER JOIN Cast as c ON md.mid=c.mid WHERE d.id=md.did
      GROUP BY md.did,c.mid HAVING COUNT(DISTINCT c.pid)<100)'''

Q5="""SELECT m.id,  
      FROM(
            )as female_actors
      ;"""
      
      