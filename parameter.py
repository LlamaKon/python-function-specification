# 引数(parameter)

def func(first, second, third):
	print(f"first: {first}, second: {second}, third: {third}")


# 引数に与える値のことを　「argument」という
func("1", "2", "3")

# first: 1, second: 2, third: 3


func("1", third="3", second="2")

# first: 1, second: 2, third: 3



# 引数にデフォルトの値を与えることが可能
# デフォルトの値を与える際は、引数の最後の値にのみ与える必要がある

def defaultValue(first, second, third="3"):
	print(f"first: {first}, second: {second}, third: {third}")

defaultValue('1', '2')

# first: 1, second: 2, third: 3


defaultValue('1', '2', '33')

# first: 1, second: 2, third: 33