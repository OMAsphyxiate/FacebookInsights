import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBAIgGYwUkawU1ki6TSl8nNUHbOZCZBXbAtSiTngoZARNorE0VFBGBOOA7NrgHNGlosISeFxZBKHrolZApi14VrYMFvH0dkDqaOBVjBFrPxZBa4eGTV3JI1TR1XuZA0Kz1DNlgH4TxHF9IS7pHj4dX8X4yQzIGqHQ32F3lizhqOOtyeQCS5Dddg0ZD'
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
posts = graph.get_connections(profile['id'], 'posts?fields=id,permalink_url,message,type,created_time,insights.metric(post_impressions_unique,post_impressions_organic_unique,post_impressions_paid_unique,post_impressions_organic,post_impressions_paid,post_engaged_users,post_consumptions_unique,post_consumptions,post_negative_feedback,post_impressions_fan,post_impressions_fan_unique,post_impressions_fan_paid,post_impressions_fan_paid_unique,post_engaged_fan,post_video_complete_views_organic_unique,post_video_complete_views_organic,post_video_complete_views_paid_unique,post_video_complete_views_paid,post_video_views_organic_unique,post_video_views_organic,post_video_views_paid_unique,post_video_views_paid,post_video_avg_time_watched,post_video_length).period(lifetime)')

for post in posts['data']:
    try:
        var1 = post['message']
    except:
        var1 = "No Message"
    for key in post['insights']:
        for entry in post['insights']['data']:
            for value in entry['values']:
                WriteFile('KeyMetricsPost',user,post['id'],post['permalink_url'],var1,post['type'],post['created_time'],\
                entry['name'],entry['period'],entry['title'],entry['description'],entry['id'],value['value'])
        #WriteFile('FansByCity', user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)