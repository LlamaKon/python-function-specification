def print_name_local():
	first_name = 'Taro'
	last_name = 'Yamada'
	print(f"I'm {first_name} {last_name}")

print_name_local()

# I'm Taro Yamada


# 関数内で定義された値は関数内でのみ使用可能　
# -> ローカル変数


# グローバル変数
age = 30

def print_age():
	age = 20
	print(f"I'm {age} years old")

print_age()

# I'm 20 years old


print(age)

# 30



# ローカル変数が定義されていない場合、グローバル変数から値を取得
def print_global_age():
	print(f"I'm {age} years old")

print_global_age()

# I'm 30 years old



def use_global_age():
	global age
	age = 20
	print(f"I'm {age} years old")

use_global_age()

# I'm 20 years old