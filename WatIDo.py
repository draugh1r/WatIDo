from time import localtime

activities = {8: 'Sleeping',
              13: 'School',
              14: 'Launch',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              21: 'Resting',
              24: 'I am Hacking bitches!',
              6: 'I am Hacking bitches!' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print (activities[activity_time])
        break
else:
    print ('Unknown, AFK or sleeping!')
input()

#KEKW
