# for reference: https://github.com/slimkrazy/python-google-places
from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyDtQGw9JcQ4Y5310naHgO3rP5reI2uacL0'

google_places = GooglePlaces(YOUR_API_KEY)

class googRestaurant():
    def __init__(self, idkey, restname, restloc, pric, rat, add, rev, hour, web):
        self.id = idkey
        self.name = restname
        self.location = restloc
        self.price = pric
        self.rating = rat
        self.address = add
        self.review = rev
        self.hours = hour
        self.url = web

def get_google_restaurants(searchterm, place, rad):
#query_result = google_places.nearby_search(
#        location='Princeton, New Jersey', keyword='Pizza',
#        radius=500, types=[types.TYPE_FOOD])
    query_result = google_places.nearby_search(
        location=place, keyword=searchterm,
        radius=rad, types=[types.TYPE_FOOD])

    restlist = []

    if query_result.has_attributions:
        print (query_result.html_attributions)

    for place in query_result.places:

        place.get_details()

        #print(place.name)
        reviews = []
        try:
            num = len(place.details['reviews'])
            for i in range(num):
                reviews.append([place.details['reviews'][i]['rating'],
                            place.details['reviews'][i]['text'],
                            place.details['reviews'][i]['relative_time_description'],
                            place.details['reviews'][i]['time']
                            ])
        except:
            reviews = []
   
        try:
            pricelvl = place.details['price_level']
        except:
            pricelvl = 'na'

        try:
            website = place.details['website']
        except:
            website = 'na'

        try:
            rating = place.details['rating']
        except:
            rating = 'na'
        
        try:
            hours = place.details['opening_hours']
        
            fhours = []
            for i in hours['weekday_text']:
                loc = i[-5 -i[-4::-1].index(" ")]
                temp = []
                for k in range(len(i)):
                    if i[k] != loc: temp.append(i[k])
                    else: temp.append("-")
                temp = "".join(temp)
                #fhours.append(i.replace("?", "-"))
                fhours.append(temp)

        except:
            hours = 'na'


        restlist.append(googRestaurant(place.place_id, 
            place.name, 
            [float(place.geo_location['lat']), float(place.geo_location['lng'])],
            pricelvl,
            rating,
            place.details['formatted_address'],
            reviews,
            fhours,
            website,
            ))        
       
        #print (place.details) # A dict matching the JSON response from Google.
        #print (place.local_phone_number)
        
    #for i in restlist:
    #    print(i.name, i.id, i.location, i.address, i.url)
    #    #print(i.hours)
    #    print(i.price, i.rating)
    #    print(i.review)
    #    print()
    #    print()

    # Are there any additional pages of results?
    if query_result.has_next_page_token:
        query_result_next_page = google_places.nearby_search(
                pagetoken=query_result.next_page_token)

    return restlist

#get_google_restaurants("Conte", "Princeton, NJ", 500)