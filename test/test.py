import pytest
from prequest.py import Prequest

def test_url_must_be_whitelisted():
	obj = Prequest()
	url = "http://randomurl.org"
	assert obj.is_url_whitelisted(url) == false