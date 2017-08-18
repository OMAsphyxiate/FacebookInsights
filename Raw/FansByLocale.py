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
posts = graph.get_connections(profile['id'], 'insights/page_fans_locale?since=%s' %daterange)

for post in posts['data']:
    for entry in post['values']:
        if 'value' in entry:
            for key, value in entry['value'].items():
                WriteFile('FansByLocale',user,post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])
        else:
            pass
        #WriteFile('FansByCity', user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)