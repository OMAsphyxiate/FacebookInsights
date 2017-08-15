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
posts = graph.get_connections(profile['id'], 'insights/page_consumptions_by_consumption_type?since=%s' %daterange)

for post in posts['data']:
    var1 = post['name']
    var2 = post['period']
    var3 = post['title']
    var4 = post['description']
    var5 = post['id']
    for value in post['values']:
        try:
            var20 = value['value']['video play']
        except:
            var20 = 0
        try:
            var21 = value['value']['other clicks']
        except:
            var21 = 0
        try:
            var22 = value['value']['photo view']
        except:
            var22 = 0
        try:
            var23 = value['value']['link clicks']
        except:
            var23 = 0
        try:
            var24 = value['value']['button clicks']
        except:
            var24 = 0

        var25 = value['end_time']
        WriteFile('ConsumptionsByType', user, var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)