import csv, facebook, datetime, os, sys, pyodbc
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

FileName = Connect.FBPath + "NegativeFeedbackByTypeUnique.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in Connect.UserList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_negative_feedback_by_type_unique?since=%s' %daterange)

    for post in posts['data']:
        var1 = post['name']
        var2 = post['period']
        var3 = post['title']
        var4 = post['description']
        var5 = post['id']
        for value in post['values']:
            try:
                var20 = value['value']['hide_all_clicks']
            except:
                var20 = 0
            try:
                var21 = value['value']['hide_clicks']
            except:
                var21 = 0
            try:
                var22 = value['value']['unlike_page_clicks']
            except:
                var22 = 0
            try:
                var23 = value['value']['report_spam_clicks']
            except:
                var23 = 0
            try:
                var24 = value['value']['xbutton_clicks']
            except:
                var24 = 0
            var25 = value['end_time']
            Functions.WriteFile('NegativeFeedbackByTypeUnique', str(item), var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25)
            #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)