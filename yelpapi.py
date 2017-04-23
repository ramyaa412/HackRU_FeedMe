#appid = 'sX_6k9Oa267UYCk-mcK83g'
#secret = 'PGjGTWbDts9jAdUmCcqTGiwUUcdWFJL6EHLC3lC1shSAXp9bp7oDwHFHHJuFWikp'
# stuff taken from https://github.com/Yelp/yelp-fusion/blob/master/fusion/python/sample.py

from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode


# OAuth credential placeholders that must be filled in by users.
CLIENT_ID = 'sX_6k9Oa267UYCk-mcK83g'
CLIENT_SECRET = 'PGjGTWbDts9jAdUmCcqTGiwUUcdWFJL6EHLC3lC1shSAXp9bp7oDwHFHHJuFWikp'


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

# Defaults for our simple example.
DEFAULT_TERM = 'agricola'
DEFAULT_LOCATION = 'Princeton, NJ'
SEARCH_LIMIT = 3


class yelpRestaurant():
    def __init__(self, idkey, restname, restloc, pric, rat, add, rev, hour, rcount, rtype):
        self.id = idkey
        self.name = restname
        self.location = restloc
        self.price = pric
        self.rating = rat
        self.address = add
        self.review = rev
        self.hours = hour
        self.revcount = rcount
        self.types = rtype


def obtain_bearer_token(host, path):
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def request(host, path, bearer_token, url_params=None):
    """Given a bearer token, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        bearer_token (str): OAuth bearer token, obtained using client_id and client_secret.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }
    #print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(bearer_token, term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)


def get_business(bearer_token, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, bearer_token)

def get_reviews(bearer_token, business_id):

	review_path = BUSINESS_PATH + business_id + "/reviews"
	return request(API_HOST, review_path, bearer_token)


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)

    response = search(bearer_token, term, location)

    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    #print(u'{0} businesses found, querying business info ' \
    #    'for the top result "{1}" ...'.format(
    #        len(businesses), business_id))
    response = get_business(bearer_token, business_id)
    revs = get_reviews(bearer_token, business_id)
    reviews = [revs['reviews'][0]['text'],
    			revs['reviews'][1]['text'],
    			revs['reviews'][2]['text']]

    #print(u'Result for business "{0}" found:'.format(business_id))
    #pprint.pprint(response, indent=2)
    
    types = []
    for i in range(len(response['categories'])):
    	types.append(response['categories'][i]['title'])

    rest = yelpRestaurant(response['id'],
    					response['name'],
    					[response['coordinates']['latitude'], response['coordinates']['longitude']],
    					response['price'],
    					response['rating'],
    					", ".join(response['location']['display_address']), #.join(', '),
    					reviews,	
    					response['hours'],
    					response['review_count'],
    					types
    					)

    return rest

    '''print(rest.id, rest.name, rest.location, rest.address)
    print(rest.price, rest.rating, rest.revcount)
    print(rest.review)
    print(rest.types)
    print()'''
    
	#idkey, restname, restloc, pric, rat, add, rev, hour, review_count, types
	# var names: id, name, location, price, rating, address, review, hours, revcount, types


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

def askfor(searchname, locname):
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=searchname,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=locname, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        return query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )


if __name__ == '__main__':
    main()