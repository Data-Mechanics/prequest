import requests

class Prequest(requests.requests):
	# def __init__(self):
	def get(url):
		response = requests.get(url)
	
		if(response.status_code == 200):
			#everything went through
			#check if data is not cached online, Fetch API
			#create a cache if needed, Write API
			return response
		else:
			#Errors 404,400,500, and so on...
			#can write sub cases if need be
			
			#check if S3 bucket has this data cached, if so, return the cached dataset
			#Call the "Fetch API" of AWS


			#If not, assume data was never cached. This is the first request; and the data is unavailable. Send back response as is.
			return response



pq = Prequest.get("http://www.google.com");
print(pq.status_code)

####Alternative approach#####
# class Prequest(requests.request):
# 	def __init__(self):
# 	# def get(url):
# 		return "hello"
# 	# 	return requests.get(url)


# pq = Prequest.get("http://www.google.com");
# print(pq.status_code)
