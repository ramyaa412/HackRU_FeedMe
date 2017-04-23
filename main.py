import apis, nutriapi
import eatapi
import bank


def main():
	print("Welcome to the backend of Feed Me, the unique integrated application that solves all your food issues!")
	print("Please select your choice from the following menu:")
	print("1. Metareviews of restaurants in a location")
	print("2. Nutrition value of foods and meals")
	print("3. Figure out how much money do you have in the bank (can you afford to splurge today?!)")
	inp = input()
	while (inp != '1' and inp != '2' and inp != '3'):
		print("I didn't get that, please select again!")
		inp = input()
	if inp == '1': metaReview()
	if inp == '2': nutritionValue()
	if inp == '3': balance()

def metaReview():
	print("Select the type of restaurant you are interestd in:")
	food = input()
	print("Select the place you would like to search around:")
	place = input()
	print("Select the radius in which you would like to search, in yards:")
	rad = int(input())
	restaurants = apis.get_restaurants(food, place, rad)
	print("I found %s restaurants, how many would you like to hear about?" % len(restaurants))
	overall = int(input())
	if overall > len(restaurants): overall = len(restaurants)
	for i in range(overall):
		print("Restaurant #%s" % (i + 1))
		print("Name: " + restaurants[i].name)
		print("Coordinates: " + "[" + str(restaurants[i].coordinates[0]) + ', ' + str(restaurants[i].coordinates[1]) + ']')
		print("Price level: " + str(restaurants[i].price))
		print("Rating: " + str(restaurants[i].rating))
		print("Type of food: " + ", ".join(restaurants[i].type))
		print("Number of reviews: " + str(restaurants[i].numReviews))
		print("Opening hours: ") 
		for j in range(7):
			print("  " + restaurants[i].hours[j])
		print("Number of nearby ATMs: " + str(restaurants[i].atms))
		print("Not displaying reviews.")
		print()
		print("Click any key to continue")
		input()
	print()
	main()

def nutritionValue():
	print("What would you like to do?")
	print("1. Receive nutrition values about a specific meal?")
	print("2. Get nutrition values for some meals in restaurants in an area.")
	inp = input()
	while (inp != '1' and inp != '2'):
		print("I didn't get that, please select again!")
		inp = input()
	if inp == '1': specificMeal()
	if inp == '2': restaurantMeals()

def specificMeal():
	print("Please input the food you would like to receive specific nutrition values about:")
	meal = input()
	nutriapi.return_nutri_complex(meal)
	print()
	main()

def restaurantMeals():
	print("Please input the address (number and street) of the area you want to search around:")
	street = input()
	print("Please input the city in which you want to search:")
	city = input()
	print("Please input the state in which you want to search:")
	state = input()
	eatapi.menusForInterface(street, city, state)
	print()
	main()

def balance():
	print("Ideally this would be individual for each customer.")
	print("However, since we received only three customer IDs,")
	print("please select whose account do you want to check?")
	print("1. Jerald")
	print("2. Sabrina")
	print("3. Elliott")
	cus = int(input())
	while (cus != 1 and cus != 2 and cus != 3):
		print("I didn't get that, please select again!")
		cus = int(input())
	if cus == 1: balance = bank.get_balance('58fcb3e9a73e4942cdafd565')
	elif cus == 2: balance = bank.get_balance('58fcb3e9a73e4942cdafd566')
	else: balance = bank.get_balance('58fcb3e8a73e4942cdafd564')
	customers = ["Jerald", "Sabrina", "Elliott"]
	if balance == 'na': comment = "you do not have an account. It might be better to save some?"
	elif balance < 10000: comment = "you have less than $10,000. Think twice before splurging!"
	else: comment = "your account's balance is great. Might it be time to treat yourself and your loved ones?"
	print()
	print("Hi " + str(customers[cus-1]) + "! According to our information, " + comment)
	print()
	input("Press any key to continue...")
	print()
	main()

main()
