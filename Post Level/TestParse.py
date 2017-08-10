import requests
import facebook
import urllib3
import pprint
import json
import csv
import os
import io

CSVFile = "OKCSouthDDS_Lifetime_Post_Consumer.csv"

access_token = "EAACEdEose0cBAAthyla6qU10t3eKQIik85sfzdf9SlvlnQeYukjSRfNqnmODgZA5KLwZA7RjqYYb1WVQgrQajUh1uzQB1Bi7ObbtTFAGmYanVE1fgESjVQ2DXz4M0Pr7pr6EeZC5WxtbhjZCbj2LrJOZBeOOot69Hi3jDqD6Xse6eqBpZAZAMis6AQhFWBm2qIZD"


postData = requests.get("https://graph.facebook.com/v2.10/OKCSouthDDS/posts?access_token="+access_token)


url = 'https://graph.facebook.com/v2.10/OKCSouthDDS/posts?fields='

csv_fields = ["ClinicID","id","permalink_url","message","type","created_time","targeting","video play","other clicks","photo view","link clicks"]
postFields = ('id,permalink_url,message,type,created_time,targeting,insights.metric(post_consumptions_by_type_unique).period(lifetime)')

request_post = requests.get(url+postFields+"&access_token="+access_token)

data = json.loads(request_post.text)

review_parse = data['data']
try:
	os.remove('OKCSouthDDS_Lifetime_Post_Consumer.csv')
except OSError:
	pass

#Open file to write JSON data in CSV format
review_data = open(CSVFile, 'w', newline='', encoding="utf-8")

#Create CSV writer object
csv_writer = csv.DictWriter(review_data,delimiter="|",fieldnames=csv_fields)
csv_writer.writeheader()
csv_writer.writerows(review_parse)