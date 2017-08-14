import requests, facebook, urllib3, pprint, json, csv, io, os


def PullAPIData(requestFields,locationID,accessToken):
	url = 'https://graph.facebook.com/v2.10/'+ locationID +'/posts?fields='
	request_post = requests.get(url + requestFields + "&access_token=" + access_token)  # Sent REST request to GET data

	json_data = json.loads(request_post.text)  # Load JSON string into dictionary

	#print (json.dumps(json_data, indent=4, sort_keys=True))


def CreateCSV(objectDef,paraFields):
	CSVFile = objectDef+'PostLevel.csv'
	#Open CSV file
	review_data = open(CSVFile, 'w', newline='', encoding="utf-8")

	review_parse = json_data['data']

	#Create CSV writer object
	csv_writer = csv.DictWriter(review_data,delimiter="|",fieldnames=paraFields)
	csv_writer.writeheader()
	csv_writer.writerows(review_parse) #review_parse is the preloaded JSON data file


def CreateCSV(CSVName,csvFields,jsonLoaded):
	#Open CSV file
	review_data = open(CSVName, 'w', newline='', encoding="utf-8")

	review_parse = jsonLoaded['data']

	#Create CSV writer object
	csv_writer = csv.DictWriter(review_data,delimiter="|",fieldnames=csvFields)
	csv_writer.writeheader()
	csv_writer.writerows(review_parse) #review_parse is the preloaded JSON data file



#Define Access Token
access_token = "EAACEdEose0cBADXXo5YCNgaC0nAWKWPvVZCaK2UuKmVwLOuZAC8TtJWgqQ3PTUhDz0KAtOWzlCRvqZAuVQRsUoegqZAlgEwkwC1halCZA9yw8MgsX9vFu2S13KgY37B4UHOHrxr364U1dXCr9OBVLDvskpZCfNQaN7V7RzWTToP8EnuFy0KXoziKPZCC9ZAH2YUZD" 

keyMetricFields = ('id,permalink_url,message,type,created_time,targeting,insights.metric(post_consumptions_by_type_unique).period(lifetime)')

jsonFile = 'TestData.json'
CSVFile = 'KMPostLevel.csv'

def TestJSONFile(inputFile,outputFile):

	all_fields = ["id", "permalink_url", "message", "type", "created_time", "video play", "other clicks", "photo view", "link clicks"]

	with open(inputFile) as review_file: #Open JSON file
		review_load = json.load(review_file) #Load JSON data into parser

	review_parse = review_load['data']

	CreateCSV(CSVFile,all_fields,review_parse)

TestJSONFile(jsonFile,CSVFile)