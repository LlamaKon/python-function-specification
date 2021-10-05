# Decorator: 関数に機能を付属する（デコレートする）

def greeting(func):
	def inner(*args, **kwargs):
		print('Hello!')
		func(*args, **kwargs)
		print('Nice to meet you!')

	return inner


@greeting
def say_name(name):
	print(f"I'm {name}")


say_name('Jiro')

# Hello!
# I'm Jiro
# Nice to meet you!


@greeting
def say_name_and_origin(name, origin):
	print(f"I'm {name}, I'm from {origin}")

say_name_and_origin('Taro', 'Tokyo')

# Hello!
# I'm Taro, I'm from Tokyo
# Nice to meet you!