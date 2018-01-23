import requests
import json

class Prequest():

	def __init__(self): 
		with open('config.json') as json_data_file:
			self.data = json.load(json_data_file)

	def is_url_whitelisted(self,url):
		return url.split("/")[0] in self.data["whitelisted_urls"];

	def get(self,url):

		#Check url whitelist, and return if not whitelisted
		if not is_url_whitelisted(url):
			return "Error! Please get the url whitelisted"


		response = requests.get(url)
		print(self.data["api_parent_url"])
	
		if(response.status_code == 200):
			#everything went through
			#check if data is not cached online, Fetch API
			#create a cache if needed, Write API
			requests.post(self.data["api_parent_url"]+url)
			return response
		else:
			#Errors 404,400,500, and so on...
			#can write sub cases if need be
			
			#check if S3 bucket has this data cached, if so, return the cached dataset
			#Call the "Fetch API" of AWS


			#If not, assume data was never cached. This is the first request; and the data is unavailable. Send back response as is.
			return response





#Sample call
# pq = Prequest()
# response = pq.get("https://data.boston.gov/export/f12/3e6/f123e65d-dc0e-4c83-9348-ed46fec498c0.tsv");
# print(response)

####Alternative approach#####
# class Prequest(requests.request):
# 	def __init__(self):
# 	# def get(url):
# 		return "hello"
# 	# 	return requests.get(url)


# pq = Prequest.get("http://www.google.com");
# print(pq.status_code)
