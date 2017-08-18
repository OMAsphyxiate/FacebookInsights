import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBAOzR56ZByTauMIe64hYPAMyNkZCZC96EHpmfs4BApNMMAWD0lzIy96hvZCBr5tQOsys5AKxV05Ik404HprsZBbdX2otDg3k40gTCVnmaq0SNsqUfDrl5ZB3PqH9coeGBvS1KX036bjwBzhlrGSSveVS3DtPcvnxoGjGrTQcH9J3ZA6YbsTqiZBQZD'
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
posts = graph.get_connections(profile['id'], 'insights/page_positive_feedback_by_type?since=%s' %daterange)

for post in posts['data']:
    var1 = post['name']
    var2 = post['period']
    var3 = post['title']
    var4 = post['description']
    var5 = post['id']
    for value in post['values']:
        try:
            var20 = value['value']['link']
        except:
            var20 = 0
        try:
            var21 = value['value']['like']
        except:
            var21 = 0
        try:
            var22 = value['value']['comment']
        except:
            var22 = 0
        try:
            var23 = value['value']['claim']
        except:
            var23 = 0
        try:
            var24 = value['value']['answer']
        except:
            var24 = 0
        try:
            var25 = value['value']['other']
        except:
            var25 = 0
        var26 = value['end_time']
        WriteFile('PositiveFeedbackByType', user, var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)