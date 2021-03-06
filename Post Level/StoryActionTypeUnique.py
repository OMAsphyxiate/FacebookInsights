import csv, facebook, datetime, os, sys, pyodbc
import Connect #Import connection file
from FacebookInsights import Functions #Import Functions for creating file
from DatabaseSyncs import DBFunctions as dbf

FileName = Connect.FBPath + "StoryActionTypeUnique.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in dbf.FacebookList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'posts?fields=id,permalink_url,message,type,created_time,insights.metric(post_story_adds_by_action_type_unique).period(lifetime)')
    for post in posts['data']:
        var1 = post['id']
        var2 = post['permalink_url']
        try:
            var3 = post['message'].replace('\n',' ')
        except:
            var3 = 'No Message'
        try:
            var4 = post['type']
        except:
            var4 = 'No Type'
        var5 = post['created_time']
        try:
            var6 = post['insights']['data'][0]['name']
        except:
            var6 = 'No Insights Name'
        try:
            var7 = post['insights']['data'][0]['period']
        except:
            var7 = 'No Insights Period'
        try:
            var8 = post['insights']['data'][0]['values'][0]['value']['like']
            if var8 == "":
                var8=0
            else:
                pass
        except:
            var8 = 0
        try:
            var9 = post['insights']['data'][0]['values'][0]['value']['comment']
            if var9 == "":
                var9=0
            else:
                pass
        except:
            var9 = 0
        try:
            var10 = post['insights']['data'][0]['values'][0]['value']['share']
            if var10 == "":
                var10=0
            else:
                pass
        except:
            var10 = 0

        Functions.WriteFile(FileName, str(item),var1,var2,var3,var4,var5,var6,var7,var8,var9,var10) #Write data to file
