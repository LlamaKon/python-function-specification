# *args
# 不特定多数の値を渡すことが可能

def number_print(*args):
	print(*args)

number_print(1, 2, 3, 4, 5)

# 1 2 3 4 5



def number_print2(*args):
	print(args)

number_print2(1, 2, 3, 4, 5)

# (1, 2, 3, 4, 5)



def get_average(*args):
	num = len(args)

	if num == 0:
		return 0

	total = sum(args)
	return total / num

average = get_average(1, 2, 3, 4, 5, 6, 7, 8)
print(average)

# 4.5





# **kwargs
# 辞書型で返す

def kwargs_func(**kwargs):
	print(kwargs)

kwargs_func(param1=10, param2=6, param3=100)

# {'param1': 10, 'param2': 6, 'param3': 100}



def kwargs_func2(**kwargs):
	param1 = kwargs.get('param1', 1)
	param2 = kwargs.get('param2', 2)
	param3 = kwargs.get('param3', 3)

	print(f"param1: {param1}, param2: {param2}, param3: {param3}")

kwargs_func2(param1=33, param2=66, param3=99)