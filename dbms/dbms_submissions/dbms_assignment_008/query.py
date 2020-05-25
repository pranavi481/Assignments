Q1='''SELECT d.id,d.fname from Director as d
      WHERE NOT EXISTS(
            SELECT md.did 
            FROM MovieDirector as md INNER JOIN Movie as m ON md.mid=m.id
            WHERE md.did=d.id AND m.year<2000)
      AND EXISTS(
            SELECT md.did 
            FROM MovieDirector as md INNER JOIN Movie as m ON md.mid=m.id
            WHERE md.did=d.id AND m.year>2000)
      ORDER BY d.id ASC;'''
      



Q3='''SELECT * FROM Actor as a
      WHERE NOT EXISTS(
            SELECT `m`.id
            FROM Movie as m INNER JOIN Cast as c ON `m`.id=`c`.mid
            WHERE `a`.id=`c`.pid AND `m`.year BETWEEN 1990 AND 2000)
      ORDER BY id DESC LIMIT 100 '''      
      
Q2='''SELECT fname,(SELECT name FROM Movie as m INNER JOIN MovieDirector as md ON m.id=md.mid
      WHERE md.did=d.id ORDER BY rank DESC LIMIT 1) FROM Director as d LIMIT 100;
      '''
      

      
