names = '请输入你的姓名：'
places = '请输入你想去的地点：'
dics = {}
ac = True
while ac:
	name = input(names)
	place = input(places)
	dics[name] = place
	repeat = input('是否继续录入？（是/否）')
	if repeat == '否':
		ac = False
print(dics)