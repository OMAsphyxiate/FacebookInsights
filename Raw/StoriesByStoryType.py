import csv, facebook, datetime, os, sys, pyodbc
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

FileName = Connect.FilePath + "StoriesByStoryType.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in Connect.UserList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_stories_by_story_type?since=%s' %daterange)

    for post in posts['data']:
        var1 = post['name']
        var2 = post['period']
        var3 = post['title']
        var4 = post['description']
        var5 = post['id']
        for value in post['values']:
            try:
                var20 = value['value']['user post']
            except:
                var20 = 0
            try:
                var21 = value['value']['checkin']
            except:
                var21 = 0
            try:
                var22 = value['value']['fan']
            except:
                var22 = 0
            try:
                var23 = value['value']['question']
            except:
                var23 = 0
            try:
                var24 = value['value']['coupon']
            except:
                var24 = 0
            try:
                var25 = value['value']['event']
            except:
                var25 = 0
            try:
                var26 = value['value']['mention']
            except:
                var26 = 0
            try:
                var27 = value['value']['other']
            except:
                var27 = 0
            var28 = value['end_time']
            Functions.WriteFile('StoriesByStoryType', str(item), var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
            #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)