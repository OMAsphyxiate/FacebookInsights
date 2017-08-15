import facebook, requests, csv, os, unicodecsv as csv

access_token = 'EAACEdEose0cBAGKPcPJUU4LcYCI3OEO4EtOrcw0Tj2UHdZAAt28NCK7WgiiqFhxZCtvZC95g3ZBqiAMhHHQim5CjOuWVTCHFK6R71STzNl7AMQgGVAv8mHTG9siSlHBso2nnFSFDZCoInYR9p1mLRZB7tHfNYDO8ZA4IWzayQAVw8TKZCpF85Emr3gNtEofRbjMZD'
user = '159442580756185' #Page ID

def WriteFile(filename,*args): #Write file in network storage
    FilePath = "//10.10.10.252/datafiles/Dashboard/Facebook Data/%s.txt" %filename
    if os.path.exists(FilePath): #Append if file Exists
        append_check = 'ab'
    else: #Else create file
        append_check = 'wb'
    with open(FilePath, append_check) as csvfile: #Write rows to file
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(args)

def PrintValues(*args): #Testing API data in print console
    print(args)

def CheckType(*args): #Verifying variable types
    print(type(args))

def declare_values(post):
    var1 = post['id']
    var2 = post['permalink_url']
    try:
        var3 = post['message'].replace('\n',' ')
    except:
        var3 = 'No Message'
    try:
        var4 = post['type']
    except:
        var4 = 'No Type'
    var5 = post['created_time']
    try:
        var6 = post['insights']['data'][0]['name']
    except:
        var6 = 'No Insights Name'
    try:
        var7 = post['insights']['data'][0]['period']
    except:
        var7 = 'No Insights Period'
    try:
        var8 = post['insights']['data'][0]['values'][0]['value']['like']
        if var8 == "":
            var8=0
        else:
            pass
    except:
        var8 = 0
    try:
        var9 = post['insights']['data'][0]['values'][0]['value']['comment']
        if var9 == "":
            var9=0
        else:
            pass
    except:
        var9 = 0
    try:
        var10 = post['insights']['data'][0]['values'][0]['value']['share']
        if var10 == "":
            var10=0
        else:
            pass
    except:
        var10 = 0

    WriteFile('StoryActionType', user,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10) #Write data to file
    #PrintValues(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10)
    #CheckType(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
# Look at Bill Gates's profile for this example by using his Facebook id.
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts?fields=id,permalink_url,message,type,created_time,insights.metric(post_story_adds_by_action_type).period(lifetime)')

# Wrap this block in a while loop so we can keep paginating requests until
# finished.


while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [declare_values(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break