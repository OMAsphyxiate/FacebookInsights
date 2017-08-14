import facebook, requests

def some_action(post):
    print(post['id'])
    print(post['permalink_url'])
    try:
        print(post['message'])
    except:
        print("No Message")
    try:
        print(post['type'])
    except:
        print("No Type")
    print(post['created_time'])
    try:
        print(post['insights']['data'][0]['name'])
    except:
        print("No Insights Name")
    try:
        print(post['insights']['data'][0]['period'])
    except:
        print("No Insights Period")
    try:
        print(post['insights']['data'][0]['values'][0]['value']['video play'])
    except:
        print("0")
    try:
        print(post['insights']['data'][0]['values'][0]['value']['other clicks'])
    except:
        print("0")
    try:
        print(post['insights']['data'][0]['values'][0]['value']['photo view'])
    except:
        print("0")
    try:
        print(post['insights']['data'][0]['values'][0]['value']['link clicks'])
    except:
        print("0")


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'EAACEdEose0cBAPZAJLS49LvK76RglQP7R7b9Sj1dGxuvzdO2MQCiOgdcFj0SEfCi1yuZAKA1MR2m8UDXHq73IEr7bbpjjrv5M0wkFuGLxe9fGTzlx1zXZAUbt1SSdRrqsfTYZBYQwUFOE2Fcco5Mgttqrwp6NEP1652ZAZBvtZBOtejijzo3au9vxOYl2SmcmkZD'
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
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break