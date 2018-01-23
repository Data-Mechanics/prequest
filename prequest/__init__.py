from . import Prequest

def get(url):
	"""
    Get dataset hosted at a given url
    :param url: Url to fetch data from
    :return: response obtained by data service
    """
	pq = Prequest()
	# response =  pq.get("https://data.boston.gov/export/296/8e2/2968e2c0-d479-49ba-a884-4ef523ada3c0.json");
	response = pq.get(url);
	return response