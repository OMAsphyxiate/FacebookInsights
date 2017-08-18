import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBAEB4VWvpZCa1rL81kVLWAiHUt3ofQd91FQUv9mrSnHn8ZCxbcElRKZAzReWrh7ppdyFu3XuZApV6EVKmwy0MgdBEeFL5WqD2o5hwLXU1475cOwPbpvezZClEcUiS8qS4jyycApxMOSJYlz7UvS551RMurUxZC2xJ4UgZCQHktsBoENl6V0YFVUZD'
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
        WriteFile('ConsumptionByType', user, var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)