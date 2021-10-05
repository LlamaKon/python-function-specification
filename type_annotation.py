# Type annotation
# 引数にデータ型を指定することが可能
# -> の後に記述されているのは返されるデータ型を指定している　
# 指定した文字列以外の値を引数に指定してもエラーにはならない

def add_nums(num1: int, num2: int) -> int:
	return num1 + num2

print(add_nums(1, 2))

# 3


print(add_nums("1", "2"))

# 12