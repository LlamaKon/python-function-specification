call_count = 0


def print_count1():
	global call_count
	call_count += 1
	print(f"関数１: {call_count}回目")



def print_count2():
	global call_count
	call_count += 1
	print(f"関数2: {call_count}回目")


print_count1()
print_count2()

print_count1()
print_count2()

print_count1()
print_count2()

print(call_count)

# 関数１: 1回目
# 関数2: 2回目
# 関数１: 3回目
# 関数2: 4回目
# 関数１: 5回目
# 関数2: 6回目
# 6

