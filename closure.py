# Closure: クロージャ
# Pythonでは関数もオブジェクトとして扱う


def compute_square(num):
	return num * num

print(compute_square)

# <function compute_square at 0x10cce4160>


f = compute_square
print(type(f))
print(f(10))

# <class 'function'>
# 100

function_list = ['1', 1, True, f]
print(function_list[-1](10))

# 100



# 関数も引数として渡せる
def execute_func(func, param):
	return func(param)


print(execute_func(f, 10))

# 100



# 関数をreturnする
def return_func():

	def inner_func():
		print('This is an inner function')

	return inner_func

rf = return_func()
print(rf)
print(type(rf))
rf()

# <function return_func.<locals>.inner_func at 0x1033be9d0>
# <class 'function'>
# This is an inner function



# Closure: 状態をキープした関数を作成可能　

# 状態が静的の場合 --->
def power(exponent):
	 def inner_power(base):
	 	return base ** exponent

	 return inner_power

power_four = power(4)
print(power_four)
print(power_four(2))

# <function power.<locals>.inner_power at 0x10b4afa60>
# 16


power_five = power(5)
print(power_five(2))

# 32



# 状態が動的の場合 --->
def average():
	nums = []

	def inner_average(num):
		nums.append(num)
		return sum(nums) / len(nums)

	return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))

# 5.0
# 10.0
