import requests
import json

class Prequest():

	PARENT_API_URL = "https://t4oqhh4fk6.execute-api.us-east-1.amazonaws.com/beta?url={}?returnS3Url={}"
	# def __init__(self): 
		# with open('config.json') as json_data_file:
		# 	self.data = json.load(json_data_file)

	def get(self,url):

		#Fetch from data source as a default
		response = requests.get(url)
		print(self.PARENT_API_URL)
		cache_response = []

		if(response.status_code == 200):
			#everything went through
			#check if data is cached online, Fetch API. 
			#Pass returnS3Url as False, implies we dont care for any url to be returned. We just want to check existence
			
			cache_response = requests.get(self.PARENT_API_URL.format(url, False))
			print("Everything went OK. Checking S3 for pre existing cache")
			print(cache_response.status_code)
			cache_response =  cache_response.json()
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

			cache_response = requests.get(self.PARENT_API_URL.format(url, True))
			cache_response =  cache_response.json()
			print("Original data not found. Checking S3 for pre existing cache")
			print(cache_response.json())

			if(cache_response.status_code !=200):		
				#If not, assume data was never cached. This is the first request; and the data is unavailable. Send back response as is.
				print("Oops! S3 does not have a cache for your data.")
				return response
			else:
				#proceed to download actual data from S3 url
				print("S3 catch found for your data. Downloading...")
				actual_data = requests.get(cache_response.url)
				return actual_data





#Sample call
pq = Prequest()
#Does not exist yet.
response =  pq.get("https://data.boston.gov/export/35f/ad2/35fad26c-1400-46b0-846c-3bb6ca8f74d0.json");
response = pq.get(url);

####Alternative approach#####
# class Prequest(requests.request):
# 	def __init__(self):
# 	# def get(url):
# 		return "hello"
# 	# 	return requests.get(url)


# pq = Prequest.get("http://www.google.com");
# print(pq.status_code)
