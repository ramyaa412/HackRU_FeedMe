import pymongo
import pprint
import apis
import json
import requests


nessie = 'bb01280025a5265f4df7f929091cc677'
urlbase = 'api.reimaginebanking.com/enterprise'

customerId = '58fcb3e9a73e4942cdafd565' # Jerald
#customerId = '58fcb3e9a73e4942cdafd566' # Sabrina
#customerId = '58fcb3e8a73e4942cdafd564' # Elliott
apiKey = nessie

fullurl = 'http://api.reimaginebanking.com/customers/' + customerId + '/accounts?key=' + nessie

def get_balance(cust):
	fullurl = 'http://api.reimaginebanking.com/customers/' + cust + '/accounts?key=' + nessie
	rawAccount = requests.request('GET', fullurl)
	response = rawAccount.json()
	if len(response) == 1: balance = response[0]['balance']
	elif len(response) == 0: balance = 'na'
	else: 
		balance = 0
		for i in response:
			balance += i['balance']
	#print("Your balance is: " + str(balance))
	return balance

#print(get_balance('58fcb3e9a73e4942cdafd565'))
#print(get_balance('58fcb3e9a73e4942cdafd566'))
#print(get_balance('58fcb3e8a73e4942cdafd564'))