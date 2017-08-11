import requests, facebook, urllib3, pprint, json, csv, io, os

CSVFile = "OKCSouthDDS_Lifetime_Post_Consumer.csv"

access_token = ""

postData = requests.get("https://graph.facebook.com/v2.10/OKCSouthDDS/posts?access_token=" + access_token)

url = 'https://graph.facebook.com/v2.10/OKCSouthDDS/posts?fields='

csv_fields = ["ClinicID", "id", "permalink_url", "message", "type", "created_time", "targeting", "video play",
              "other clicks", "photo view", "link clicks"]
postFields = (
'id,permalink_url,message,type,created_time,targeting,insights.metric(post_consumptions_by_type_unique).period(lifetime)')

request_post = requests.get(url + postFields + "&access_token=" + access_token)  # Sent REST request to GET data

try:
    os.remove('OKCSouthDDS_Lifetime_Post_Consumer.csv')  # Remove CSV file if already exists
except OSError:
    pass

json_data = json.loads(request_post.text)  # Load JSON string into dictionary


print(json_data['data'][0]['id']) #Print ID of first data row
print(json_data['data'][0]['permalink_url']) #Print permalink of first data row
print(json_data['data'][0]['message']) #Print message of first data row
print(json_data['data'][0]['type']) #Print type of first data row
print(json_data['data'][0]['created_time']) #Print created time of first data row
#print(json_data['data'][0]['targeting']) #Print targeting for first data row
print(json_data['data'][0]['insights']['data'][0]['values'][0]['value']['video play']) #Print Video Play of first data
print(json_data['data'][0]['insights']['data'][0]['values'][0]['value']['other clicks']) #Print other clicks of first data
print(json_data['data'][0]['insights']['data'][0]['values'][0]['value']['photo view']) #Print photo views of first data
print(json_data['data'][0]['insights']['data'][0]['values'][0]['value']['link clicks']) #Print link clicks of first data
