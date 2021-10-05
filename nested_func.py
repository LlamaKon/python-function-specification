# 関数の中で関数を定義　（nested function)

def outer():

	outer_param = 'outer arg'
	
	def inner():
	
		print("This is inner function")
		print(outer_param)

	inner()

outer()

# This is inner function
# outer arg


msg = 'I am global'


def outer_func():

	msg = "I am outer"

	def inner_func():

		msg = 'I am inner'
		print("This is inner function")
		print(msg) # I am inner

	inner_func()
	print(msg) # I am outer

outer_func()
print(msg) # I am global

# This is inner function
# I am inner
# I am outer
# I am global



def outer_func_non():

	msg = "I am outer"

	def inner_func_non():

		nonlocal msg
		msg = 'I am inner'
		print("This is inner function")
		print(msg)

	inner_func_non()
	print(msg)

outer_func_non()
print(msg)

# This is inner function
# I am inner
# I am inner
# I am global