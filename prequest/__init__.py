from .prequest import Prequest
from requests import Response

__version__ = '0.0.1'


def get(url: str) -> Response:
    """
    Get dataset hosted at a given url
    :param url: Url to fetch data from
    :return: response obtained by data service
    """
    with Prequest() as pq:
        return pq.get(url)
