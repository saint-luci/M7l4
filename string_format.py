team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

print("In master's command %s members" % team1_num)
print("In commands: %s, %s - members" % (team1_num, team2_num))
print("Wizard's command made {score} exercises".format(score=score2))
print("Wizards time is {time}".format(time=team1_time))
print(f"Comands made {score1} and {score2} exercises")

challenge_result = ""
task_total = score1 + score2
time_avg = (team1_time + team2_time) / (score1 + score2)

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = "Мастера кода!"
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = "Волшебники Данных!" 
else:
    challenge_result = "Ничья!"
print(f"Winner is: {challenge_result}")
print(f"Number of exercices : {task_total} - average time for one task: {round(time_avg, 1)}")
