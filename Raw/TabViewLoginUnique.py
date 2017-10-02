import csv, facebook, datetime, os, sys, pyodbc
import Connect #Import connection file
from FacebookInsights import Functions #Import Functions for creating file
from DatabaseSyncs import DBFunctions as dbf

FileName = Connect.FBPath + "TabViewLoginUnique.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=60)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in dbf.FacebookList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_tab_views_login_top_unique?since=%s' %daterange)

    for post in posts['data']:
        var1 = post['name']
        var2 = post['period']
        var3 = post['title']
        var4 = post['description']
        var5 = post['id']
        for value in post['values']:
            try:
                var20 = value['value']['about']
            except:
                var20 = 0
            try:
                var21 = value['value']['community']
            except:
                var21 = 0
            try:
                var22 = value['value']['custom']
            except:
                var22 = 0
            try:
                var23 = value['value']['home']
            except:
                var23 = 0
            try:
                var24 = value['value']['photos']
            except:
                var24 = 0
            try:
                var25 = value['value']['posts']
            except:
                var25 = 0
            try:
                var26 = value['value']['profile_home']
            except:
                var26 = 0
            try:
                var27 = value['value']['profile_reviews']
            except:
                var27 = 0
            try:
                var28 = value['value']['reviews']
            except:
                var28 = 0
            try:
                var29 = value['value']['services']
            except:
                var29 = 0
            try:
                var30 = value['value']['videos']
            except:
                var30 = 0
            try:
                var31 = value['value']['notes']
            except:
                var31 = 0
            try:
                var32 = value['value']['album']
            except:
                var32 = 0
            var33 = value['end_time'].replace('T07:00:00+0000','')
            Functions.WriteFile(FileName,str(item),var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33)
            #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)