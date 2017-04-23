import requests

zomatoKey = 'c55ce2360709568de507e7d20ec9c47f'
#curl -X GET --header "Accept: application/json" --header "user-key: c55ce2360709568de507e7d20ec9c47f" "https://developers.zomato.com/api/v2.1/restaurant?res_id=16774318"
baseUrl = 'https://developers.zomato.com/api/v2.1/restaurant?res_id='
header = {'user-key': zomatoKey}
restID = '16774318'
url = baseUrl + restID


cityID = '3977&entity_type=city' # Princeton 				# NYC = 280, Princeton = 3977 
baseCityURL = 'https://developers.zomato.com/api/v2.1/search?entity_id='
cityURL = baseCityURL + cityID

menuURL = 'https://developers.zomato.com/api/v2.1/dailymenu?res_id='



class zomatoRestaurant():
	def __init__(self, idkey, nam, pric, rat, typ, vote):
		self.id = idkey
		self.name = nam
		self.correctName(nam)
		self.price = pric
		self.rating = rat
		self.type = typ
		self.votes = int(vote)

	def printRest(self):
		print("ID: " + str(self.id))
		print("Name: " + self.name)
		print("Price: " + str(self.price))
		print("Rating: " + str(self.rating))
		print("Types: " + self.type)
		print("Votes: " + str(self.votes))

	def correctName(self, nam):
		if nam == "Conte's": self.name = "Conte's Pizza"

def getRestaurantsFromCity(url):
	rawRestaurants = requests.request('GET', url, headers=header)
	response = rawRestaurants.json()
	restList = []
	for i in response["restaurants"]:
		rest = zomatoRestaurant(
			i["restaurant"]["id"], 
			i["restaurant"]["name"],
			i["restaurant"]["price_range"],
			i["restaurant"]["user_rating"]["aggregate_rating"],
			i["restaurant"]["cuisines"],
			i["restaurant"]["user_rating"]["votes"]
			)
		#menu = requests.request('GET', menuURL + i["restaurant"]["id"], headers=header)
		#print(menu.json())
		restList.append(rest)
	return restList
		
def extract():
	return getRestaurantsFromCity(cityURL)

#rlist = getRestaurantsFromCity(cityURL)
#for i in rlist:
#	i.printRest()


'''
raw_response = requests.request('GET', url, headers=header)
response = raw_response.json()
rest = zomatoRestaurant(
	response["id"],
	response["name"],
	response["price_range"],
	response["user_rating"]["aggregate_rating"],
	response["cuisines"],
	response["user_rating"]["votes"]
	)

rest.printRest()
'''