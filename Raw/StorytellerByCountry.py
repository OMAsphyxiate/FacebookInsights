import csv, facebook, datetime, os

access_token = 'EAACEdEose0cBAIGoZBLinsChqrzP53iz4zsE2U8YG64wfaONXjg7SJcVX7Rj2rFPwsZBAXgvf6W7lYKVzZAcyusHVfoGix74xyMtqgaNMMPTUIeBrSRX1nnec7qprrOZCcNI4tZCG29eWPqFZAa56yrfaHbNtHOBBEqipYtc2OZBCzibqGi3wa02rOKhX8vD40kfZBiBdlZCXaQZDZD'
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
posts = graph.get_connections(profile['id'], 'insights/page_storytellers_by_country?since=%s' %daterange)

for post in posts['data']:
    for entry in post['values']:
        for key, value in entry['value'].items():
            WriteFile('StorytellerByCountry',user,post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])
            #PrintValues(user,post['name'],post['period'],post['title'],post['description'],post['id'],key,value,entry['end_time'])