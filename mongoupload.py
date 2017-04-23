import pymongo
import pprint
import apis

#client = pymongo.MongoClient("mongodb://wwww:1111@hackru2017feedme-shard-00-00-bsyox.mongodb.net:27017,hackru2017feedme-shard-00-01-bsyox.mongodb.net:27017,hackru2017feedme-shard-00-02-bsyox.mongodb.net:27017/hackru2017feedme?ssl=true&replicaSet=hackru2017feedme-shard-0&authSource=admin")
#client = pymongo.MongoClient('mongodb://heroku_s13dqq10:c5b7hlbujuecnetp4mppna4p43@ds057386.mlab.com:57386/heroku_s13dqq10')
client = pymongo.MongoClient("mongodb://test:test@ds115411.mlab.com:15411/heroku_btbprq1d")

db = client.test
posts = db.posts
#db.posts.remove({"author": "Lee3"})
#pprint.pprint(posts.find_one())
post = {"author": "Lee3",
	"text": "blah",
	"tags": "python"}
posts = db.posts
#ost_id = posts.insert_one(post).inserted_id
#print(post_id)	# gibberish
#pprint.pprint(posts.find_one())

#for i in posts.find():
#	print(i)
pprint.pprint(db.collection_names())

collection=db['users']
cursor = collection.find({})
for document in cursor:
    print(document)



restaurants = db.restaurants
'''
restlist = apis.get_restaurants("Pizza", "Princeton, New Jersey", 700)
for i in restlist:
	newdict = {}
	newdict["listing"] = "restaurant"
	newdict["name"] = i.name
	newdict["coordinates"] = [i.coordinates[0], i.coordinates[1]]
	newdict["price"] = i.price
	newdict["rating"] = i.rating
	newdict["type"] = i.type
	newdict["numReviews"] = i.numReviews
	newdict["hours"] = i.hours
	newdict["reviews"] = i.reviews
	#print(newdict)
	restaurant_id = restaurants.insert_one(newdict).inserted_id
'''
#for i in restaurants.find():
	#print(i)



#print(db.users.find_one({"_id": "1"}))
#print(db.users.find_one({"_id": "1"}))

