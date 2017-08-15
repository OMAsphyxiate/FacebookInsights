import facebook, requests, csv, os, unicodecsv as csv

def WriteFile(filename,*args):
    try:
        os.remove(filename)  # Remove CSV file if already exists
    except OSError:
        pass
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(args)

def PrintValues(*args):
    print(args)

def CheckType(*args):
    print(type(args))

def StoreList(*args):
    list_values = []

def declare_values(post):
    var1 = post['id']
    var2 = post['permalink_url']
    try:
        var3 = post['message']
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
        var8 = post['insights']['data'][0]['values'][0]['value']['video play']
    except:
        var8 = 0
    try:
        var9 = post['insights']['data'][0]['values'][0]['value']['other clicks']
    except:
        var9 = 0
    try:
        var10 = post['insights']['data'][0]['values'][0]['value']['photo view']
    except:
        var10 = 0
    try:
        var11 = post['insights']['data'][0]['values'][0]['value']['link clicks']
    except:
        var11 = 0
    #WriteFile('KeyMetrics.csv', var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)
    #WriteFile('KeyMetrics.txt', var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)
    #PrintValues(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)
    #CheckType(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)
    #return(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)
    StoreList(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)

list_values=[]
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'EAACEdEose0cBAEg9wlmWdmuGIDLZBTP88BZAeWf1RqOJk35ZCLuHjZB2pqYODM1euIFX4DlRKSMgZBt49Pn73jjgWsXhWOkht9mjE7I5qFfs4ag4kO24ImtD6jxqnoZADZCPEeSbvhwkCvNTb74wpRZBJ7GTAvp6sAOC8xkLy6rEQRJZA7SYWMN3AzyPHNtPaOchrLRW3JOukxQZDZD'
# Look at Bill Gates's profile for this example by using his Facebook id.
user = 'OKCSouthDDS'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts?fields=id,permalink_url,message,type,created_time,insights.metric(post_consumptions_by_type_unique).period(lifetime)')

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