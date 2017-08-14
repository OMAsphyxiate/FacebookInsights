import requests, facebook, urllib3, pprint, json, csv, io, os


def PullAPIData(requestFields,locationID,accessToken):
	url = 'https://graph.facebook.com/v2.10/'+ locationID +'/posts?fields='
	request_post = requests.get(url + requestFields + "&access_token=" + access_token)  # Sent REST request to GET data

	json_data = json.loads(request_post.text)  # Load JSON string into dictionary

	print (json.dumps(json_data, indent=4, sort_keys=True))



def CreateCSV(objectDef,paraFields):
	CSVFile = objectDef+'PostLevel.csv'
	#Open CSV file
	review_data = open(CSVFile, 'w', newline='', encoding="utf-8")

	#Create CSV writer object
	csv_writer = csv.DictWriter(review_data,delimiter="|",fieldnames=paraFields)
	csv_writer.writeheader()
	csv_writer.writerows(review_parse) #review_parse is the preloaded JSON data file


#Define Access Token
access_token = "EAACEdEose0cBAKdIP91ZA7yIJIt5AMCySGCP1ZCs3ikC5YegmdZAsDq28hQ0ZC4tpTub7ZBCn7hTqTw59xjbAlBTjyZAW1OFElQNJkx1YIynQGYCssOXhSCBh02qlY4fZAgzj47CSpApATrLTf0Ju3RZBXGZBC2Lk1Bh7Yw34iwPeh9N0yNb9Hvr51YX8qnZA3mWMZD" 

keyMetricFields = ('id,permalink_url,message,type,created_time,targeting,insights.metric(post_consumptions_by_type_unique).period(lifetime)')


#Call API Request function for Post Level key Metrics
PullAPIData(keyMetricFields,'OKCSouthDDS',access_token)
