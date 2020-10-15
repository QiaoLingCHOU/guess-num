import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = input('請輸入數字:')
	num = int(num)
	if num == r:
		print('終於猜對答案了!')
		print('這是您猜的第', count, '次!')
		break
	else:
		if num > r:
			print('您猜的數字比正確答案大!')
		elif num < r:
			print('您猜的數字比正確答案小!')
	print('這是您猜的第', count, '次!')