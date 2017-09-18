import csv, facebook, datetime, os, sys, pyodbc
import Connect #Import connection file
from FacebookInsights import Functions #Import Functions for creating file
from DatabaseSyncs import DBFunctions as dbf

FileName = Connect.FBPath + "PositiveFeedbackByType.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in dbf.FacebookList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_positive_feedback_by_type?since=%s' %daterange)

    for post in posts['data']:
        var1 = post['name']
        var2 = post['period']
        var3 = post['title']
        var4 = post['description']
        var5 = post['id']
        for value in post['values']:
            try:
                var20 = value['value']['link']
            except:
                var20 = 0
            try:
                var21 = value['value']['like']
            except:
                var21 = 0
            try:
                var22 = value['value']['comment']
            except:
                var22 = 0
            try:
                var23 = value['value']['claim']
            except:
                var23 = 0
            try:
                var24 = value['value']['answer']
            except:
                var24 = 0
            try:
                var25 = value['value']['other']
            except:
                var25 = 0
            var26 = value['end_time']
            Functions.WriteFile(FileName, str(item), var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26)
            #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)