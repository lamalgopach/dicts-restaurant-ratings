"""Restaurant rating lister."""
def open_file(filename):
	"""Opens a file
	"""
	file = open(filename)
	return file


def create_dictionary(file):
	"""Creates a dictionary from a file
	"""
	restaurant_dict = {}
	#restaurant_list = []
	

	for line in file:
		line = line.rstrip().split(":")
		restaurant_dict[line[0]] = int(line[1])

	for k,v in sorted(restaurant_dict.items()):
		print("{} is rated at {}.".format(k,v))

	return restaurant_dict


def ask_restaurant():
	"""Ask user about a restaurant
	"""
	restaurant = input("Please tell us the name of the restaurant you want to rate. ")
	return restaurant


def ask_rate():
	"""Ask user to rate the restaurant
	"""
	rate = input("Please tell us the rating of that restaurant. ")
	return rate


def add_to_dictionary(restaurant_name,rating,restaurant_dict):
	"""Add restaurant to pre-existing dictionary
	"""
	restaurant_dict[restaurant_name] = rating
	sorted(restaurant_dict)

	for k,v in sorted(restaurant_dict.items()):
		print("{} is rated at {}.".format(k,v))

	return restaurant_dict


file = open_file("scores.txt")
restaurant_dict = create_dictionary(file)

restaurant_name = ask_restaurant()
rating = ask_rate()
add_to_dictionary(restaurant_name, rating, restaurant_dict)
