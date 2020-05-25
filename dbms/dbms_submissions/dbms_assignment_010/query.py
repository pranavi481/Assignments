Q1='''SELECT p.player_id,p.team_id,p.jersey_no,p.name,p.date_of_birth,p.age
      FROM MatchCaptain as mc INNER JOIN Player as p ON mc.captain=p.player_id AND p.team_id=mc.team_id WHERE p.player_id 
      NOT IN (SELECT player_id FROM GoalDetails);'''

Q2="SELECT team_id,COUNT(team_id) as no_of_games FROM MatchTeamDetails GROUP BY team_id;"

Q3='''SELECT team_id,COUNT(goal_id)*1.0/(SELECT
      COUNT(player_id) FROM Player GROUP BY team_id) 
      FROM GoalDetails GROUP BY team_id;'''

Q4="SELECT captain,COUNT(captain) as no_of_times_captain FROM MatchCaptain GROUP BY captain;"

Q5='''SELECT COUNT(DISTINCT captain) FROM MatchCaptain as mc INNER JOIN Match as m ON m.match_no=mc.match_no WHERE mc.captain=m.player_of_match;'''

Q6='''SELECT DISTINCT captain FROM MatchCaptain as mc
      WHERE EXISTS(SELECT player_id FROM Player as p WHERE mc.captain=p.player_id)
      AND NOT EXISTS(SELECT player_of_match FROM Match as m WHERE mc.captain=m.player_of_match)'''

Q7="SELECT strftime('%m',play_date),COUNT(match_no) FROM Match GROUP BY strftime('%m',play_date);"

Q8="SELECT jersey_no,COUNT(captain) as no_captains FROM Player as p INNER JOIN MatchCaptain as mc ON mc.captain=p.player_id  GROUP BY jersey_no ORDER BY no_captains DESC,jersey_no DESC;"

Q9="SELECT player_id,AVG(audience) as avg_audience FROM Match as m INNER JOIN MatchTeamDetails as mtd ON m.match_no=mtd.match_no INNER JOIN Player as p ON p.team_id=mtd.team_id GROUP BY player_id ORDER BY avg_audience DESC,player_id DESC;"

Q10="SELECT team_id,AVG(age) FROM Player GROUP BY team_id;"

Q11="SELECT AVG(age) FROM Player as p INNER JOIN MatchCaptain as mc ON mc.captain=p.player_id;"

Q12="SELECT strftime('%m',date_of_birth) as month,COUNT(player_id) as no_of_players FROM Player GROUP BY month ORDER BY no_of_players DESC,month DESC;"

Q13='''SELECT captain,COUNT(win_lose) as no_of_wins FROM MatchCaptain as mc INNER JOIN MatchTeamDetails as mtd ON mc.match_no=mtd.match_no 
      WHERE win_lose='W' AND mc.team_id=mtd.team_id GROUP BY captain ORDER BY no_of_wins DESC;'''
      


      