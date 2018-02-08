.PHONY: test

init:
	pip install --quiet --requirement=requirements.txt
	pip install --quiet --requirement=test-requirements.txt

test:
	nosetests
	flake8 --ignore=E501 prequest

publish:
	pip install 'twine>=1.5.0'
	pip install wheel
	twine upload dist/*
	python setup.py sdist bdist_wheel
	rm -fr build dist .egg requests.egg-info
