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
	street = street.split(" ")
	street = "+".join(street)
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


def menusForInterface(street, city, state):
	urladd1 = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?method=both&street-address='
	#urladdinput = '339+Witherspoon+St.,+Princeton,+NJ'
	street = street.split(" ")
	street = "+".join(street)
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

	print("How many restaurants would you like to see?")
	totRest = int(input())
	print("How many meals would you want to see in each restaurant?")
	totMeals = int(input())
	m = 0
	for i in restaurants:
		rID = i.apiK
		tempmenu = requests.request('GET', urlmenu1+rID+urlmenu2+urladd)
		menu = tempmenu.json()
		n = 0
		for j in menu:
			nutri = nutriapi.return_nutri_simple(j['name'])
			#print(nutri.name, nutri.calories, nutri.fat)
			i.meals.append(nutri)
			n += 1
			if n > totMeals: break
		m += 1
		if m > totRest: break
	
	m = 0	
	for i in restaurants:
		print("Restaurant " + str(m+1) + ": " + i.name)
		for j in i.meals:
			if j is None: break
			print("   " + j.name + ": " + str(j.calories) + " calories, and " + str(j.fat) + " grams of fat per serving.")
		input("Hit any key to continue...")
		print()	
		m += 1
		if m >= totRest: break



#menus('339+Witherspoon+St.', 'Princeton', 'NJ')
	
