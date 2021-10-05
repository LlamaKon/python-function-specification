# 参照渡し(byref) <-> 値渡し(byvalue)

def add_nums(a, b):
	print(f"第一引数aのID:{id(a)}")
	print(f"第二引数bのID:{id(b)}")
	return a + b


one = 1
two = 2
print(f"oneのID:{id(one)}")
print(f"twoのID:{id(two)}")
print(add_nums(one, two))

# oneのID:4338460976
# twoのID:4338461008
# 第一引数aのID:4338460976
# 第二引数bのID:4338461008
# 3



def add_one(num):
	print(f"変更前のID: {id(num)}")
	num += 1
	print(f"変更後のID: {id(num)}")
	return num

one = 1
print(id(one))
print(f"関数呼び出し前のone: {one}")
add_one(one)
print(f"関数呼び出し後のone: {one}")

# 4373502256
# 関数呼び出し前のone: 1
# 変更前のID: 4373502256
# 変更後のID: 4373502288
# 関数呼び出し後のone: 1



def add_fruit(fruits, fruit):
	print(f"変更前のID：{id(fruits)}")
	fruits.append(fruit)
	print(f"変更後のID：{id(fruits)}")
	return fruits

myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'

print(f"関数呼び出し前のmyfruits: {myfruits}")
add_fruit(myfruits, myfruit)
print(f"変更呼び出し後のmyfruits: {myfruits}")

# 関数呼び出し前のmyfruits: ['apple', 'banana', 'peach']
# 変更前のID：4380063040
# 変更後のID：4380063040
# 変更呼び出し後のmyfruits: ['apple', 'banana', 'peach', 'lemon']

