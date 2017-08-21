import csv, facebook, datetime, os, sys, pyodbc
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

FileName = Connect.FilePath + "FansByCity.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in Connect.UserList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_fans_city?since=%s' %daterange)

    for post in posts['data']:
        for entry in post['values']:
            for key, value in entry['value'].items():
                Functions.WriteFile('FansByCity',str(item),post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])
            #WriteFile('FansByCity', user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
            #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)