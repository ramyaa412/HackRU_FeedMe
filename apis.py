import yelpapi
import googapi
import zomatoapi
import requests
import bank

class Restaurant():

	def __init__(self, googid, googname, googcoordinates, googaddress):
		self.id = googid
		self.name = googname
		self.coordinates = googcoordinates
		self.address = googaddress

	def setPrice(self, gPrice, yPrice):
		if gPrice == "na": gPrice = len(yPrice)
		self.price = (gPrice + len(yPrice)) / 2

	def setRating(self, gRating, yRating):
		if gRating == "na": gRating = yRating
		self.rating = (float(gRating) + float(yRating)) / 2

	def setReviews(self, gReviews, yReviews, yNumReviews):
		googReviews = []
		for i in gReviews:
			googReviews.append(i[1])
		self.reviews = googReviews + yReviews
		self.numReviews = int(yNumReviews)

	def setType(self, yType):
		self.type = yType

	def setHours(self, forhours):
		self.hours = forhours

	def setATMs(self):
		self.atms = bank.get_atms(str(self.coordinates[0])[:9], str(self.coordinates[1])[:9])

	def zomUpdate(self, zom):
		self.price = ((self.price * 2) + float(zom.price)) / 3
		self.rating = ((self.rating * 2) + float(zom.rating)) / 3
		self.numReviews = self.numReviews + zom.votes
		self.type = list(set(list(self.type)) | set(list(zom.type)))

	def printFormatted(self):
		print("Name: " + self.name)
		print("Latitude: " + str(self.coordinates[0])[:9] + "; " + "Longitude: " + str(self.coordinates[1])[:9])
		types = ""
		for i in self.type:
			types = types + " " + i
		print("Type of restaurant: " + types)
		print("Address: " + self.address)
		print("Price range: " + str(self.price))
		print("Rating: " + str(self.rating))
		print("Number of reviews: " + str(self.numReviews))
		print("Opening hours:")
		for i in range(7):
			print("  " + self.hours[i])
		print("Number of nearby ATMs: " + str(self.atms))

def get_restaurants(kind, place, dist):

	newadditions = []

	#grestlist = googapi.get_google_restaurants("Pizza", "Princeton, New Jersey", 700)
	grestlist = googapi.get_google_restaurants(kind, place, dist)

	zomlist = zomatoapi.extract()
	zomset = set()
	for i in zomlist:
		zomset.add(i.name)
	#for i in zomset:
	#	print(i)

	for i in grestlist:
		rest = Restaurant(i.id, i.name, i.location, i.address)
		yrest = yelpapi.askfor(i.name, i.address)
		rest.setPrice(i.price, yrest.price)
		rest.setRating(i.rating, yrest.rating)
		rest.setType(yrest.types)
		rest.setReviews(i.review, yrest.review, yrest.revcount)
		rest.setHours(i.hours)
		rest.setATMs()
		newadditions.append(rest)
		found = False
		for j in zomlist:
			if (rest.name == j.name): 
				#print("exists: " + j.name)
				rest.zomUpdate(j)
				#rest.printFormatted()
				found = True
				break
		#if (found == False): print("doesn't exist: " + rest.name)

		#print(rest.name)

	return newadditions
	#for i in newadditions:
	#	i.printFormatted()
	#	print()
	#	print()