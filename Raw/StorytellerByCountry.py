import csv, facebook, datetime, os, sys, pyodbc
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

FileName = Connect.FBPath + "StorytellerByCountry.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in Connect.UserList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_storytellers_by_country?since=%s' %daterange)

    for post in posts['data']:
        for entry in post['values']:
            for key, value in entry['value'].items():
                Functions.WriteFile('StorytellerByCountry',str(item),post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])
                #PrintValues(user,post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])