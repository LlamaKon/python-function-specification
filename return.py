def print_dict(input_dict):

	for k, v in input_dict.items():
	
		print(f"key:{k}, value{v}")


a = {"one": 1, "two": 2}

print_dict(a)

# key:one, value1
# key:two, value2



def get_first_last_word(text):
	
	text.replace(",", "")
	
	words = text.split()
	
	return words[0], words[-1]


text = "Hello My name is Mike"

first, last = get_first_last_word(text)

print(f"first word is {first}, last word is {last}")

# first word is Hello, last word is Mike

# returnで複数の値が返ってくる際は、タプルで返ってくるs