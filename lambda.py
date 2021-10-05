# lambda関数(無名関数)

def square(x):
	return x * x


print(square(3))

# 9



s = lambda x: x * x
print(s(5))

# 25


# def power(exponent):
# 	def inner_power(base):
# 		return base ** exponent
# 	return inner_power


# third_power = power(3)
# print(third_power(2))

# # 8


def power(exponent):
	return lambda base: base ** exponent

third_power = power(3)
print(third_power(2))

# 8



numbers = [6, 2, 5, 43, 5, 36, 67, 2]


def filter_func(num):
	return num % 2

for num in numbers:
	print(filter_func(num))


# filter関数はTrueに該当するもののみ返す
filtered_num = filter(filter_func, numbers)
print(list(filtered_num))

# [5, 43, 5, 67]



lambda_num = filter(lambda num: num % 2, numbers)
print(list(lambda_num))

# [5, 43, 5, 67]