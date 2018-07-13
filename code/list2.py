names = []
names.append('张学友')
names.append('奥黛丽赫本')
names.append('Michel Jackson')

for x in range(0,3):
    print('Dear ' + names[x] + ',Can you come to my dinner?')
print(names[1],'cannot attend')

print('I found a bigger table.')

names.insert(0,'周杰伦')
names.insert(2,'陈奕迅')
names.append('Justin Biber')
for i in range(0,len(names)):
    print('Dear ' + names[i] + ',Can you come to my dinner?')

X = len(names)
for x in range(0,X-2):
    popped_name = names.pop()
    print('实在抱歉，' + popped_name +'我不能与你共进晚餐了！')

for x in range(0,len(names)):
    print('Dear ' + names[x] + ',我依然邀请你来与我共进晚餐！')