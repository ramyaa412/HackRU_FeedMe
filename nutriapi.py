import requests

nutID = '69aa5a36'
nutKey = '6b0fc2d970c3bc1c5783f2bc9ae575ea'


url = 'https://api.nutritionix.com/v1_1/search/'
item = 'Big%20Mac'
urlnext = '?fields=item_name%2Citem_id%2Cbrand_name%2Cnf_calories%2Cnf_total_fat&appId=' + nutID
urlthird = '&appKey=' + nutKey

class Nutrition():
	def __init__(self, nam, cal, fats):
		self.name = nam
		self.calories = cal
		self.fat = fats

def return_nutri_complex(itemname):
	itemname = itemname.split(" ")
	itemname = "%20".join(itemname)
	#print(itemname)
	rawNutri = requests.request('GET', url+itemname+urlnext+urlthird)
	response = rawNutri.json()

	print("In decreasing order of relevance to your search, here are some details about your choice:")
	n = 0
	for i in response['hits']:
		print("Item " + str(n + 1) + ": " + i['fields']['item_name'])
		print("Brand: " + i['fields']['brand_name'])
		print("Calories: " + str(i['fields']['nf_calories']))
		print("Fat: " + str(i['fields']['nf_total_fat']))
		input()
		n += 1
		if (n > 5): 
			print("Skipping the remaining results!")
			break

def return_nutri_simple(itemname):
	itemname = itemname.split(" ")
	itemname = "%20".join(itemname)
	#print(itemname)
	rawNutri = requests.request('GET', url+itemname+urlnext+urlthird)
	response = rawNutri.json()
	#print(response)
	for i in response['hits']:
		n = i['fields']['item_name']
		c = i['fields']['nf_calories']
		f = i['fields']['nf_total_fat']
		#print(n, c, f)
		return Nutrition(n, c, f)

#print(return_nutri_simple('tomatos'))