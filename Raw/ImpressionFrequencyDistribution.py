import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBAK6jLxZC2ofnOng8T5ZCw9PDx8g9X23fGVIukXHDZAOnmDRU7azrG1nEEqRJZB4dgDeX9CBPdUhqEPEcKpJ1dyf0hZBwx9ZCP3xzkVIVwacnqsRCP1U2NPVNgVGOTJDuv0ZCF4ueKMiuExRY7OZCaGAylGKMsXRGZC7QsD6ZBvCblzEZA1OItn0I6sZD'
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
posts = graph.get_connections(profile['id'], 'insights/page_posts_impressions_frequency_distribution?since=%s' %daterange)

for post in posts['data']:
    var1 = post['name']
    var2 = post['period']
    var3 = post['title']
    var4 = post['description']
    var5 = post['id']
    for value in post['values']:
        try:
            var20 = value['value']['1']
        except:
            var20 = 0
        try:
            var21 = value['value']['2']
        except:
            var21 = 0
        try:
            var22 = value['value']['3']
        except:
            var22 = 0
        try:
            var23 = value['value']['4']
        except:
            var23 = 0
        try:
            var24 = value['value']['5']
        except:
            var24 = 0
        try:
            var25 = value['value']['6-10']
        except:
            var25 = 0
        try:
            var26 = value['value']['11-20']
        except:
            var26 = 0
        try:
            var27 = value['value']['21+']
        except:
            var27 = 0
        var28 = value['end_time']
        WriteFile('ImpressionFrequencyDistribution', user, var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)