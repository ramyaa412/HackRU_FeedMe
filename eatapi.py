import requests
import nutriapi

class Restaurant():

	def __init__(self, aKey, eatname, typeFood):
		self.apiK = aKey
		self.name = eatname
		self.types = typeFood
		self.meals = []


def menus(street, city, state):
	urladd1 = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?method=both&street-address='
	#urladdinput = '339+Witherspoon+St.,+Princeton,+NJ'
	urladdinput = street + ",+" + city + ",+" + state
	urlmenu1 = 'https://api.eatstreet.com/publicapi/v1/restaurant/'
	urlmenu2 = '/menu?includeCustomizations=false'
	urladd = '&access-token=15a3fa4ab9e83cad'
	header = 'X-Access-Token: 15a3fa4ab9e83cad'
	rawRestaurants = requests.request('GET', urladd1+urladdinput+urladd)
	response = rawRestaurants.json()
	restaurants = []
	for i in response['restaurants']:
		temp = Restaurant(i['apiKey'],
				i['name'],
				i['foodTypes'])
		restaurants.append(temp)

	for i in restaurants:
		rID = i.apiK
		tempmenu = requests.request('GET', urlmenu1+rID+urlmenu2+urladd)
		menu = tempmenu.json()
		for j in menu:
			nutri = nutriapi.return_nutri_simple(j['name'])
			print(nutri.name, nutri.calories, nutri.fat)
			i.meals.append(nutri)
			break
		
	for i in restaurants:
		print(i.name)
		for j in i.meals:
			if j is None: break
			print(j.name, j.calories, j.fat)

menus('339+Witherspoon+St.', 'Princeton', 'NJ')
	
