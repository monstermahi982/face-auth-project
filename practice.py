# name = "maheshgaikwad8892@gmail.com"
# print(name.split('@')[0])

import datetime
  
# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2017, 6, 21, 3, 45, 30)
b = datetime.datetime(2017, 6, 21, 3, 35, 30)
  
# returns a timedelta object
c = a-b 
print('Difference: ', c)
  
minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)
  
# returns the difference of the time of the day
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)


# app.config['MONGO_URI'] = "mongodb+srv://monsterwalamess:mi71H7kdyVK4PAT8@cluster0.ia9b4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"