import csv, facebook, datetime, os, sys, pyodbc
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

FileName = Connect.FBPath + "KeyMetricsPost.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in Connect.UserList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'posts?fields=id,permalink_url,message,type,created_time,insights.metric(post_impressions_unique,post_impressions_organic_unique,post_impressions_paid_unique,post_impressions_organic,post_impressions_paid,post_engaged_users,post_consumptions_unique,post_consumptions,post_negative_feedback,post_impressions_fan,post_impressions_fan_unique,post_impressions_fan_paid,post_impressions_fan_paid_unique,post_engaged_fan,post_video_complete_views_organic_unique,post_video_complete_views_organic,post_video_complete_views_paid_unique,post_video_complete_views_paid,post_video_views_organic_unique,post_video_views_organic,post_video_views_paid_unique,post_video_views_paid,post_video_avg_time_watched,post_video_length).period(lifetime)')

    for post in posts['data']:
        try:
            var1 = post['message']
        except:
            var1 = "No Message"
        for key in post['insights']:
            for entry in post['insights']['data']:
                for value in entry['values']:
                    Functions.WriteFile('KeyMetricsPost',str(item),post['id'],post['permalink_url'],var1,post['type'],post['created_time'],\
                    entry['name'],entry['period'],entry['title'],entry['description'],entry['id'],value['value'])