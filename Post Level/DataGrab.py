import requests
import facebook
import urllib3
import pprint
import json
import csv
import os
import io

CSVFile = "OKCSouthDDS_Lifetime_Post_Consumer.csv"

access_token = "EAACEdEose0cBACpr4VCnxUExlYEqKj236jn5Q6itnytH2otTBKRO2vnY8x1ZBbeuROQZBJBXNuVVNg8bOTs1ZCHO6CkBovkkTsCQWwueEoYwwASZA2bqQE8qrHJzbu028GkVUmImlA154E4kgNxzZBOYtA081whMjnVnaqoDEqtoUJa7A8ncKZBPaBj7cf8ZCUZD"


postData = requests.get("https://graph.facebook.com/v2.10/OKCSouthDDS/posts?access_token="+access_token)


url = 'https://graph.facebook.com/v2.10/OKCSouthDDS/posts?fields='

csv_fields = ["ClinicID","id","permalink_url","message","type","created_time","targeting","video play","other clicks","photo view","link clicks"]
postFields = ('id,permalink_url,message,type,created_time,targeting,insights.metric(post_consumptions_by_type_unique).period(lifetime)')

request_post = requests.get(url+postFields+"&access_token="+access_token)

try:
	os.remove('OKCSouthDDS_Lifetime_Post_Consumer.csv')
except OSError:
	pass

with open(CSVFile, 'wb') as fd:
	for chunk in request_post.iter_content(chunk_size=128):
		fd.write(chunk)