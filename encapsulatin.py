# カプセル化(encapsulatin)：外からアクセスできないようにする

def casino_entrance(age, min_age=21):

	if age < min_age:
		print(f"{min_age}歳未満お断り")
		return

	def inner_casino_entrance():
		print('ようこそカジノへ')


	return inner_casino_entrance()

casino_entrance(28)

# ようこそカジノへ


