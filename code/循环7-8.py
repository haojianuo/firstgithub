
while True:
	msg = input('请输入一种披萨配料，输入‘quit’后会退出程序，请输入：')
	if msg=='quit':
		break
	else:
		print('我们会在比萨中添加这种配料: ' + msg)