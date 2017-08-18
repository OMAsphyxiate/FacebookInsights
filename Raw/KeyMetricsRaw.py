import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBABzpk8xky2l5wXq7ZCiD2KsQZBNLUwCTOPWvnL8WEgbCKb85idAkkm92Ykbqes5kmFOPy3kv7cfGY0VxoZAg2u7iZCY1PD6wWZANJrAnHCtgHTSm8SqZBwiAVOvaAGrAeK079YTDvW68OjQY1fZAKEqnvKRKXYUixoxojqZArdZAaYyZB5bn48N9AZD'
user = '159442580756185' #Page ID

def PrintValues(*args): #Testing API data in print console
    print(args)

def WriteFile(filename,*args): #Write file in network storage
    FilePath = "//10.10.10.252/datafiles/Dashboard/Facebook Data/%s.txt" %filename
    if os.path.exists(FilePath): #Append if file Exists
        append_check = 'a'
    else: #Else create file
        append_check = 'w'
    with open(FilePath, append_check) as csvfile: #Write rows to file
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(args)

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'insights/page_fans,page_fan_adds_unique,page_fan_removes_unique,page_engaged_users,page_engaged_users,page_impressions_unique,page_impressions_unique,page_impressions_organic_unique,page_impressions_organic_unique,page_impressions_paid_unique,page_impressions_paid_unique,page_impressions,page_impressions,page_impressions_organic,page_impressions_organic,page_impressions_paid,page_impressions_paid,page_views_logged_in_total,page_views_logged_in_unique,page_posts_impressions_unique,page_posts_impressions_unique,page_posts_impressions_organic_unique,page_posts_impressions_organic_unique,page_posts_impressions_paid_unique,page_posts_impressions_paid_unique,page_posts_impressions,page_posts_impressions,page_posts_impressions_organic,page_posts_impressions_organic,page_posts_impressions_paid,page_posts_impressions_paid,page_consumptions_unique,page_consumptions_unique,page_consumptions,page_consumptions,page_negative_feedback_unique,page_negative_feedback_unique,page_negative_feedback,page_negative_feedback,page_places_checkin_total,page_places_checkin_total,page_places_checkin_total_unique,page_places_checkin_total_unique,page_places_checkin_mobile,page_places_checkin_mobile,page_places_checkin_mobile_unique,page_places_checkin_mobile_unique,page_video_views,page_video_views,page_video_views_autoplayed,page_video_views_autoplayed,page_video_views_paid,page_video_views_paid,page_video_views_organic,page_video_views_organic?period(day)')

for post in posts['data']:
    for entry in post['values']:
        WriteFile('KeyMetricsRaw',user,post['name'],post['period'],post['title'],post['description'],post['id'],\
        entry['value'],entry['end_time'])
        #WriteFile('FansByCity', user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)