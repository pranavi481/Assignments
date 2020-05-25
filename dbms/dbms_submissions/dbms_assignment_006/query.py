Q1="SELECT fname,lname from Actor INNER JOIN Cast ON pid=id WHERE mid = 12148;"
Q2="SELECT COUNT(mid) from Actor INNER JOIN Cast ON id=pid WHERE fname='Harrison (I)' and lname='Ford';"
Q3="SELECT DISTINCT pid from Cast INNER JOIN Movie ON mid=id WHERE name LIKE 'Young Latin Girls%';"
Q4="SELECT COUNT(DISTINCT pid) FROM Cast INNER JOIN Movie ON mid=id WHERE year BETWEEN 1990 and 2000;"

