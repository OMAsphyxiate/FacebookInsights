import csv, facebook, datetime, os, sys, pyodbc
import Connect #Import connection file
from FacebookInsights import Functions #Import Functions for creating file
from DatabaseSyncs import DBFunctions as dbf

FileName = Connect.FBPath + "StoryByCountryUnique.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in dbf.FacebookList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_story_adds_by_country_unique?since=%s' %daterange)

    for post in posts['data']:
        for entry in post['values']:
            for key, value in entry['value'].items():
                Functions.WriteFile(FileName,str(item),post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])
                #PrintValues(user,post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])