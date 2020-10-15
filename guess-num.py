import random
r = random.randint(1, 100)
while True:
	num = input('請輸入數字:')
	num = int(num)
	if num == r:
		print('終於猜對答案了!')
		break
	else:
		if num > r:
			print('您猜的數字比正確答案大!')
		elif num < r:
			print('您猜的數字比正確答案小!')