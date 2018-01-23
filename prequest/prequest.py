import requests
import json

class Prequest():

	PARENT_API_URL = "https://t4oqhh4fk6.execute-api.us-east-1.amazonaws.com/beta?url={}?returnS3Url={}"

	# def __init__(self): 
		# with open('config.json') as json_data_file:
		# 	self.data = json.load(json_data_file)

	def get(self,url):

		response = requests.get(url)
		print(self.PARENT_API_URL)
	
		if(response.status_code == 200):
			#everything went through
			#check if data is cached online, Fetch API. 
			check_cache_response = requests.get(self.PARENT_API_URL.format(url, False))


			print("cache_response.....")
			print(cache_response.json())
			#create a cache if needed, Write API
			# requests.post(self.PARENT_API_URL+url)
			return response
		else:
			#Errors 404,400,500, and so on...
			#can write sub cases if need be
			requests.get(self.PARENT_API_URL.format(url, True))
			
			#check if S3 bucket has this data cached, if so, return the cached dataset
			#Call the "Fetch API" of AWS


			#If not, assume data was never cached. This is the first request; and the data is unavailable. Send back response as is.
			return response





#Sample call
pq = Prequest()
# response =  pq.get("https://data.boston.gov/export/296/8e2/2968e2c0-d479-49ba-a884-4ef523ada3c0.json");
response = pq.get("https://data.boston.gov/export/f12/3e6/f123e65d-dc0e-4c83-9348-ed46fec498c0.tsv");
print(response)

####Alternative approach#####
# class Prequest(requests.request):
# 	def __init__(self):
# 	# def get(url):
# 		return "hello"
# 	# 	return requests.get(url)


# pq = Prequest.get("http://www.google.com");
# print(pq.status_code)
