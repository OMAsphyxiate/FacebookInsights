import facebook, requests

def some_action(post):
    print(post['insights'][''])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'EAACEdEose0cBADXXo5YCNgaC0nAWKWPvVZCaK2UuKmVwLOuZAC8TtJWgqQ3PTUhDz0KAtOWzlCRvqZAuVQRsUoegqZAlgEwkwC1halCZA9yw8MgsX9vFu2S13KgY37B4UHOHrxr364U1dXCr9OBVLDvskpZCfNQaN7V7RzWTToP8EnuFy0KXoziKPZCC9ZAH2YUZD'
# Look at Bill Gates's profile for this example by using his Facebook id.
user = 'OKCSouthDDS'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts', )

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