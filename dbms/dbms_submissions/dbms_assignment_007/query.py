Q1="SELECT COUNT(id) FROM Movie WHERE year< 2000;"

Q2="SELECT AVG(rank) FROM Movie WHERE year=1991;"

Q3="SELECT MIN(rank) FROM Movie WHERE year=1991;"

Q4="SELECT fname,lname FROM Actor INNER JOIN Cast ON pid=id WHERE mid = 27;"

Q5="SELECT COUNT(mid) FROM Actor INNER JOIN Cast ON id=pid WHERE fname='Jon' and lname='Dough';"

Q6="SELECT name FROM Movie WHERE name LIKE 'Young Latin Girls%' and (year>=2003 and year<=2006) ;"

Q7="SELECT fname,lname FROM MovieDirector INNER JOIN Director ON MovieDirector.did =Director.id INNER JOIN Movie ON Movie.id =MovieDirector.mid WHERE name LIKE 'Star Trek%';"

Q8="SELECT name FROM Movie INNER JOIN Cast ON `Movie`.id = `Cast`.mid INNER JOIN Actor ON `Cast`.pid = `Actor`.id INNER JOIN MovieDirector ON `Movie`.id = `MovieDirector`.mid INNER JOIN Director ON `MovieDirector`.did = `Director`.id WHERE `Director`.fname='Jackie (I)' and `Director`.lname='Chan' and (`Actor`.fname='Jackie (I)' and `Actor`.lname='Chan') ORDER BY name ASC"

Q9="SELECT fname,lname FROM Director INNER JOIN MovieDirector on Director.id = did INNER JOIN Movie ON Movie.id=mid WHERE year=2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER BY fname ASC,lname DESC;"

Q10="SELECT gender,COUNT(*) FROM Actor GROUP BY gender ORDER BY gender ASC;"

Q11="SELECT MovieName1.name,MovieName2.name,MovieName1.rank,MovieName1.year FROM Movie as MovieName1 INNER JOIN Movie as MovieName2 ON MovieName1.name<>MovieName2.name AND MovieName1.year=MovieName2.year AND MovieName1.rank==MovieName2.rank ORDER BY MovieName1.name ASC LIMIT 100;"

Q12="SELECT fname,year,AVG(rank) FROM Movie INNER JOIN Cast ON `Movie`.`id`=`Cast`.`mid` INNER JOIN Actor ON `Actor`.`id`=`Cast`.`pid` GROUP BY Actor.id,year ORDER BY fname ASC,year DESC LIMIT 100;"

Q13="SELECT Actor.fname,Director.fname,AVG(rank) as score FROM Movie INNER JOIN Cast ON `Movie`.`id`=`Cast`.`mid` INNER JOIN Actor ON `Actor`.`id`=`Cast`.`pid` INNER JOIN MovieDirector ON `MovieDirector`.`mid`=`Cast`.`mid` INNER JOIN Director ON `Director`.`id`=`MovieDirector`.`did` GROUP BY `Actor`.`id`,`Director`.`id` HAVING COUNT(`Movie`.`id`)>=5 ORDER BY score DESC,Director.fname ASC,Actor.fname DESC LIMIT 100;" 















