import csv, facebook, datetime, os, sys, pyodbc
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

FileName = Connect.FBPath + "ImpressionFrequencyDistribution.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in Connect.UserList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_posts_impressions_frequency_distribution?since=%s' %daterange)

    for post in posts['data']:
        var1 = post['name']
        var2 = post['period']
        var3 = post['title']
        var4 = post['description']
        var5 = post['id']
        for value in post['values']:
            try:
                var20 = value['value']['1']
            except:
                var20 = 0
            try:
                var21 = value['value']['2']
            except:
                var21 = 0
            try:
                var22 = value['value']['3']
            except:
                var22 = 0
            try:
                var23 = value['value']['4']
            except:
                var23 = 0
            try:
                var24 = value['value']['5']
            except:
                var24 = 0
            try:
                var25 = value['value']['6-10']
            except:
                var25 = 0
            try:
                var26 = value['value']['11-20']
            except:
                var26 = 0
            try:
                var27 = value['value']['21+']
            except:
                var27 = 0
            var28 = value['end_time']
            Functions.WriteFile('ImpressionFrequencyDistribution', str(item), var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
            #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)