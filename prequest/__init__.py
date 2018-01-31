from . import Prequest


def get(url):
	"""
    Get dataset hosted at a given url
    :param url: Url to fetch data from
    :return: response obtained by data service
    """
	pq = Prequest()
	#Does not exist yet.
	response =  pq.get("https://data.boston.gov/export/35f/ad2/35fad26c-1400-46b0-846c-3bb6ca8f74d0.json");
	response = pq.get(url);
	return response