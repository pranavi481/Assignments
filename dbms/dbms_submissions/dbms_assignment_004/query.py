Q1="SELECT COUNT(year) FROM Movie WHERE year=2002 and name LIKE 'Ha%'and rank>2;"
Q2="SELECT MAX(rank) FROM Movie WHERE name LIKE 'Autom%' and (year=1983 or year=1994);"
Q3="SELECT COUNT(id) FROM Actor WHERE gender='M' and (fname LIKE '%ei' or lname LIKE 'ei%');"
Q4="SELECT AVG(rank) as average_rank_of_movies FROM Movie WHERE (year=1993 or year=1995 or year=2000) and rank>=4.2;"
Q5="SELECT SUM(rank) FROM Movie WHERE name LIKE '%Hary%' and (year BETWEEN 1981 and 1984 ) and rank<9;"
Q6="SELECT MIN(year) FROM Movie WHERE rank=5;"
Q7="SELECT COUNT(id) FROM Actor WHERE gender='F' or fname=lname;"
Q8="SELECT DISTINCT fname FROM Actor WHERE lname LIKE '%ei' ORDER BY fname ASC LIMIT 100; "
Q9="SELECT id,name as movie_title,year FROM Movie WHERE year IN (2001, 2002, 2005, 2006) Limit 25 OFFSET 10;"
Q10="SELECT DISTINCT lname FROM Director WHERE fname IN ('Yeud', 'Wolf', 'Vicky') ORDER BY lname ASC LIMIT 5;"




#WHERE score BETWEEN (50, 80);
#SELECT name, age from Student WHERE age > 21 ORDER BY age ASC;
#SELECT name, age, score from Student Limit 4 OFFSET 3;
#SELECT DISTINCT age FROM Student;