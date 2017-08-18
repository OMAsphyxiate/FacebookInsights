import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBAFxRz1bSwcKPl00YZA4Yj2YFLKnekeNgZAgguwYP6asmKGuhwT9nuIYCZATdMcumu5g7rubn2GTbU63gZCTAbsruhKCTDYuPlDaU6zhKNLc2n00lsMj5nWZBYrjfwNyIDOfYvn3S9LDXfxmE20PZAHBkyEZBp561hswCKLG6XKPw9VZBnTTAs8kZD'
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

daterange = datetime.datetime.now() - datetime.timedelta(days=30)
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'insights/page_stories_by_story_type?since=%s' %daterange)

for post in posts['data']:
    var1 = post['name']
    var2 = post['period']
    var3 = post['title']
    var4 = post['description']
    var5 = post['id']
    for value in post['values']:
        try:
            var20 = value['value']['user post']
        except:
            var20 = 0
        try:
            var21 = value['value']['checkin']
        except:
            var21 = 0
        try:
            var22 = value['value']['fan']
        except:
            var22 = 0
        try:
            var23 = value['value']['question']
        except:
            var23 = 0
        try:
            var24 = value['value']['coupon']
        except:
            var24 = 0
        try:
            var25 = value['value']['event']
        except:
            var25 = 0
        try:
            var26 = value['value']['mention']
        except:
            var26 = 0
        try:
            var27 = value['value']['other']
        except:
            var27 = 0
        var28 = value['end_time']
        WriteFile('StoriesByStoryType', user, var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)