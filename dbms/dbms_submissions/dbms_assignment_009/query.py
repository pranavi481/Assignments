Q1="SELECT AVG(age) FROM Player;"

Q2="SELECT match_no, play_date FROM Match WHERE audience>50000 ORDER BY match_no ASC;"

Q3="SELECT team_id,COUNT(win_lose) as Win from MatchTeamDetails WHERE win_lose='W' GROUP BY team_id ORDER by Win DESC,team_id ASC;"
      
Q4='''SELECT match_no,play_date FROM Match WHERE stop1_sec > 
      (SELECT AVG(stop1_sec) 
      FROM Match) 
      ORDER BY match_no DESC;'''

Q5='''SELECT match_no,t.name,p.name FROM MatchCaptain as mc
      INNER JOIN Team as t ON t.team_id=mc.team_id
      INNER JOIN Player as p ON mc.captain=p.player_id
      ORDER BY match_no,t.name ASC;'''

Q6="SELECT m.match_no,p.name,p.jersey_no FROM Match as m INNER JOIN Player AS p ON m.player_of_match=p.player_id ORDER BY m.match_no;"

Q7="SELECT Team.name,AVG(Player.age) AS average_age FROM Player INNER JOIN Team ON Player.team_id=Team.team_id GROUP BY Team.name Having average_age>26 ORDER BY Team.name ASC;"

Q8='''SELECT p.name,p.jersey_no,p.age,count(goal_id) as count_goal_id
      from player as p INNER JOIN goaldetails as gd on gd.player_id=p.player_id 
      where p.age<=27 GROUP BY p.player_id  order  by count(goal_id) desc,p.name asc;'''

Q9 = "SELECT team_id,COUNT(goal_id)*100.0/(SELECT COUNT(goal_id) FROM GoalDetails) FROM GoalDetails GROUP BY team_id;"

Q10='''SELECT AVG(C) FROM
      (SELECT COUNT(*) AS C FROM GoalDetails GROUP BY team_id);'''

Q11='''SELECT p.player_id,p.name,p.date_of_birth
      FROM Player as p
      WHERE NOT EXISTS(
            SELECT player_id FROM GoalDetails as gd WHERE p.player_id=gd.player_id)'''
            
Q12='''SELECT Team.name,Match.match_no,Match.audience,
      Match.audience-(
      SELECT AVG(audience) FROM Match INNER JOIN MatchTeamDetails
      ON Match.match_no=MatchTeamDetails.match_no 
      WHERE MatchTeamDetails.team_id=Team.team_id GROUP BY `MatchTeamDetails`.team_id)
      FROM Team INNER JOIN MatchTeamDetails INNER JOIN Match
      ON Team.team_id=MatchTeamDetails.team_id AND Match.match_no=MatchTeamDetails.match_no ORDER BY `match`.match_no ASC;'''
            

