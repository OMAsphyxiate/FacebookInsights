import csv, facebook, datetime, os, sys, pyodbc
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

FileName = Connect.FilePath + "FansLikedOnline.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in Connect.UserList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_fans_online?since=%s' %daterange)

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
                var25 = value['value']['6']
            except:
                var25 = 0
            try:
                var26 = value['value']['7']
            except:
                var26 = 0
            try:
                var27 = value['value']['8']
            except:
                var27 = 0
            try:
                var28 = value['value']['9']
            except:
                var28 = 0
            try:
                var29 = value['value']['10']
            except:
                var29 = 0
            try:
                var30 = value['value']['11']
            except:
                var30 = 0
            try:
                var31 = value['value']['12']
            except:
                var31 = 0
            try:
                var32 = value['value']['13']
            except:
                var32 = 0
            try:
                var33 = value['value']['14']
            except:
                var33 = 0
            try:
                var34 = value['value']['15']
            except:
                var34 = 0
            try:
                var35 = value['value']['16']
            except:
                var35 = 0
            try:
                var36 = value['value']['17']
            except:
                var36 = 0
            try:
                var37 = value['value']['18']
            except:
                var37 = 0
            try:
                var38 = value['value']['19']
            except:
                var38 = 0
            try:
                var39 = value['value']['20']
            except:
                var39 = 0
            try:
                var40 = value['value']['21']
            except:
                var40 = 0
            try:
                var41 = value['value']['22']
            except:
                var41 = 0
            try:
                var42 = value['value']['23']
            except:
                var42 = 0
            var43 = value['end_time']
            Functions.WriteFile('FansLikedOnline', str(item), var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43)
            #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)