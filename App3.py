import json
import requests
import facebook

# Load data from file
def PullAPIData(requestFields,locationID,accessToken):
	url = 'https://graph.facebook.com/v2.10/'+ locationID +'/posts?fields='
	request_post = requests.get(url + requestFields + "&access_token=" + access_token)  # Sent REST request to GET data

	json_data = json.loads(request_post.text)  # Load JSON string into dictionary

	return(json_data)
	#print (json.dumps(json_data, indent=4, sort_keys=True))
keyMetricFields = ('id,permalink_url,message,type,created_time,targeting,insights.metric(post_consumptions_by_type_unique).period(lifetime)')
access_token = "EAACEdEose0cBAOSo04hkX1IZCehbgMXdK0UozKpdpvcqp0xw5F7JAJGgqshiYf1rzCZATjZByfiIxsE0Kv6vaM3bXjEIMFfdDbJgKzfK9ZAElFHrsnUub9QXsokeZBr8FhPZB8u9fa0IFEYJmPkt1XuhOfnES5aJy24W0qTYyDVoXdStVwQ07I3xBbm1Ko4wMZD"
page = "OKCSouthDDS"

# Store records for later use
records = [];

# Keep track of headers in a set
headers = set([]);


jsonParsed = PullAPIData(keyMetricFields,page,access_token)


for line in jsonParsed.split("\n"):
    line = line.strip();

    # Parse each line as JSON
    parsedJson = json.loads(line)

    records.append(parsedJson)

    # Make sure all found headers are kept in the headers set
    for header in parsedJson.keys():
        headers.add(header)

# You only know what headers were there once you have read all the JSON once.

#Now we have all the information we need, like what all possible headers are.

outfile = open('output_json_to_csv.csv','w')

# write headers to the file in order
outfile.write(",".join(sorted(headers)) + '\n')

for record in records:
    # write each record based on available fields
    curLine = []