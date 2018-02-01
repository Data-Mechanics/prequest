import requests
import json

class Prequest():

	PARENT_API_URL = "https://t4oqhh4fk6.execute-api.us-east-1.amazonaws.com/beta?url={}?returnS3Url={}"

	def get(self,url):

		#Fetch from data source as a default
		response = requests.get(url)
		print(self.PARENT_API_URL)
		cache_response = []

		if(response.status_code == 200):
			#everything went through
			#check if data is cached online, Fetch API. 
			#Pass returnS3Url as False, implies we dont care for any url to be returned. We just want to check existence
			print("Everything went OK. Checking S3 for pre existing cache")

			cache_response = requests.get(self.PARENT_API_URL.format(url, False))
			print("cache response status code:" + cache_response.status_code)

			if(cache_response.status_code != 200):
				#create a cache, call writeData
				requests.post(self.PARENT_API_URL+url)
				#else let it be. A cache already exists for this dataset.

			return response
		else:
			#Errors 404,400,500, and so on...
			#Now we need to request S3 url from the cache and proceed to GET it ourselves.
			#Call the "Fetch API" of AWS
			#Pass returnS3Url as True, implies we care for a url to be returned. 

			print("Original data not found. Checking S3 for pre existing cache")

			cache_response = requests.get(self.PARENT_API_URL.format(url, True))
			cache_response =  cache_response.json()

			#If cache response is 200, return cached data. If not, implies cache was never created in the first place. Return original response.
			return cache_response.status_code == 200 ? requests.get(cache_response.url) : response 




#Sample call
# pq = Prequest()
#Does not exist yet.
# response =  pq.get("https://data.boston.gov/export/35f/ad2/35fad26c-1400-46b0-846c-3bb6ca8f74d0.json");
# response = pq.get(url);

