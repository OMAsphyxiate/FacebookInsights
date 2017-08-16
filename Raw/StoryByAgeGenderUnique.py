import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBAF0bSHeELrojEOLIQuZBaGNVCw4xNGkVYGq3KgWNbdPIxXHhP3eYyftR5nG8JpHPQKWajXRGDCZCeeMidiXBEZB84hWaknurUDidy52sM7nxNb3Hiq6pTXxkSwiv2RwLkgU7rCOVJmCY7pG9vPTeruvi7JRhnqa0sil4BCNnxEzx26jS4UZD'
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
posts = graph.get_connections(profile['id'], 'insights/page_story_adds_by_age_gender_unique?since=%s' %daterange)

for post in posts['data']:
    var1 = post['name']
    var2 = post['period']
    var3 = post['title']
    var4 = post['description']
    var5 = post['id']
    for value in post['values']:
        try:
            var20 = value['value']['F.13-17']
        except:
            var20 = 0
        try:
            var21 = value['value']['F.18-24']
        except:
            var21 = 0
        try:
            var22 = value['value']['F.25-34']
        except:
            var22 = 0
        try:
            var23 = value['value']['F.35-44']
        except:
            var23 = 0
        try:
            var24 = value['value']['F.45-54']
        except:
            var24 = 0
        try:
            var25 = value['value']['F.55-64']
        except:
            var25 = 0
        try:
            var26 = value['value']['F.65+']
        except:
            var26 = 0
        try:
            var27 = value['value']['M.13-17']
        except:
            var27 = 0
        try:
            var28 = value['value']['M.18-24']
        except:
            var28 = 0
        try:
            var29 = value['value']['M.25-34']
        except:
            var29 = 0
        try:
            var30 = value['value']['M.35-44']
        except:
            var30 = 0
        try:
            var31 = value['value']['M.45-54']
        except:
            var31 = 0
        try:
            var32 = value['value']['M.55-64']
        except:
            var32 = 0
        try:
            var33 = value['value']['M.65+']
        except:
            var33 = 0
        try:
            var34 = value['value']['U.13-17']
        except:
            var34 = 0
        try:
            var35 = value['value']['U.18-24']
        except:
            var35 = 0
        try:
            var36 = value['value']['U.25-34']
        except:
            var36 = 0
        try:
            var37 = value['value']['U.35-44']
        except:
            var37 = 0
        try:
            var38 = value['value']['U.45-54']
        except:
            var38 = 0
        try:
            var39 = value['value']['U.55-64']
        except:
            var39 = 0
        try:
            var40 = value['value']['U.65+']
        except:
            var40 = 0
        var41 = value['end_time']
        WriteFile('StoryByAgeGenderUnique', user, var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41)
        #PrintValues(user,var1,var2,var3,var4,var5,var20,var21,var22,var23,var24,var25,var26,var27,var28)