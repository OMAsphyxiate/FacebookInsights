import csv, facebook, datetime, os, sys, pyodbc
import Connect #Import connection file
from FacebookInsights import Functions #Import Functions for creating file
from DatabaseSyncs import DBFunctions as dbf

FileName = Connect.FBPath + "KeyMetricsRaw.txt"

try:
    os.remove(FileName)
except OSError:
    pass

daterange = datetime.datetime.now() - datetime.timedelta(days=60)
graph = facebook.GraphAPI(Connect.FACEBOOK_USER_TOKEN)

for item in dbf.FacebookList:
    profile = graph.get_object(str(item))
    posts = graph.get_connections(profile['id'], 'insights/page_fans,page_fan_adds_unique,page_fan_removes_unique,page_engaged_users,page_engaged_users,page_impressions_unique,page_impressions_unique,page_impressions_organic_unique,page_impressions_organic_unique,page_impressions_paid_unique,page_impressions_paid_unique,page_impressions,page_impressions,page_impressions_organic,page_impressions_organic,page_impressions_paid,page_impressions_paid,page_views_logged_in_total,page_views_logged_in_unique,page_posts_impressions_unique,page_posts_impressions_unique,page_posts_impressions_organic_unique,page_posts_impressions_organic_unique,page_posts_impressions_paid_unique,page_posts_impressions_paid_unique,page_posts_impressions,page_posts_impressions,page_posts_impressions_organic,page_posts_impressions_organic,page_posts_impressions_paid,page_posts_impressions_paid,page_consumptions_unique,page_consumptions_unique,page_consumptions,page_consumptions,page_negative_feedback_unique,page_negative_feedback_unique,page_negative_feedback,page_negative_feedback,page_places_checkin_total,page_places_checkin_total,page_places_checkin_total_unique,page_places_checkin_total_unique,page_places_checkin_mobile,page_places_checkin_mobile,page_places_checkin_mobile_unique,page_places_checkin_mobile_unique,page_video_views,page_video_views,page_video_views_autoplayed,page_video_views_autoplayed,page_video_views_paid,page_video_views_paid,page_video_views_organic,page_video_views_organic?since=%s' %daterange)

    for post in posts['data']:
        for entry in post['values']:
            try:
                Functions.WriteFile(FileName,str(item),post['name'],post['period'],post['title'],post['description'],post['id'],\
                entry['value'] or 0,entry['end_time'].replace('T07:00:00+0000',''))
            except:
                e = sys.exc_info()[0]
                print( "<p>Error on ID-%s: %s</p>" % (str(item),e) )