"""Restaurant rating lister."""
def open_file(filename):
	file = open(filename)
	return file

def create_dictionary(file):
	restaurant_dict = {}
	#restaurant_list = []
	

	for line in file:
		line = tuple(line.rstrip().split(":"))
		restaurant_dict[line[0]] = line[1]

	for k,v in sorted(restaurant_dict.items()):
		print (k + " is rated at " + v + ".")


file = open_file("scores.txt")
create_dictionary(file)