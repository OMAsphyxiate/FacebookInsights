import requests, facebook, urllib3, pprint, json, csv, io, os

CSVFile = "OKCSouthDDS_Lifetime_Post_Consumer.csv"

access_token = "EAACEdEose0cBAAMViesknnPGUXZBdbP64iOR2kZAbrNkjq6ne43rQNiTTZBCCANXZAmDkc5h6FcYZBWKsxd1H2Q9pgtE1ExcoAWguoCDDpNA2t5NKZA6cboWTwZCDgBdeUJKpaaS5xUf61jCZBEvfvPYqM79KndzTOaF882nIQZBnGEQJeju3GP9N4CZCBXptWtaQZD"


postData = requests.get("https://graph.facebook.com/v2.10/OKCSouthDDS/posts?access_token="+access_token)


url = 'https://graph.facebook.com/v2.10/OKCSouthDDS/posts?fields='

csv_fields = ["ClinicID","id","permalink_url","message","type","created_time","targeting","video play","other clicks","photo view","link clicks"]
postFields = ('id,permalink_url,message,type,created_time,targeting,insights.metric(post_consumptions_by_type_unique).period(lifetime)')

request_post = requests.get(url+postFields+"&access_token="+access_token) #Sent REST request to GET data

try:
	os.remove('OKCSouthDDS_Lifetime_Post_Consumer.csv') #Remove CSV file if already exists
except OSError:
	pass

json_data = json.loads(request_post.text) #Load JSON string into dictionary

print (json_data['data']['id'])
print (json_data['permalink_url'])
print (json_data['message'])
print (json_data['type'])
print (json_data['created_time'])
print (json_data['targeting'])
print (json_data['insights']['video play'])
print (json_data['insights']['other clicks'])
print (json_data['insights']['photo view'])
print (json_data['insights']['link clicks'])