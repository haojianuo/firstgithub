'''
如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的） ， 你会邀请哪些人？ 请创建一个列表， 其中包含至少3个你想邀请的人；
使用这个列表打印消息， 邀请这些人来与你共进晚餐。
你刚得知有位嘉宾无法赴约， 因此需要另外邀请一位嘉宾。
以完成练习3-4时编写的程序为基础， 在程序末尾添加一条print 语句， 指出哪位嘉宾无法赴约。
修改嘉宾名单， 将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
再次打印一系列消息， 向名单中的每位嘉宾发出邀请。
3-6 添加嘉宾 ： 你刚找到了一个更大的餐桌， 可容纳更多的嘉宾。 请想想你还想邀请哪三位嘉宾。
以完成练习3-4或练习3-5时编写的程序为基础， 在程序末尾添加一条print 语句， 指出你找到了一个更大的餐桌。
使用insert() 将一位新嘉宾添加到名单开头。
使用insert() 将另一位新嘉宾添加到名单中间。
使用append() 将最后一位新嘉宾添加到名单末尾。
打印一系列消息， 向名单中的每位嘉宾发出邀请。
3-7 缩减名单 ： 你刚得知新购买的餐桌无法及时送达， 因此只能邀请两位嘉宾。
以完成练习3-6时编写的程序为基础， 在程序末尾添加一行代码， 打印一条你只能邀请两位嘉宾共进晚餐的消息。
使用pop() 不断地删除名单中的嘉宾， 直到只有两位嘉宾为止。 每次从名单中弹出一位嘉宾时， 都打印一条消息， 让该嘉宾知悉你很抱歉， 无法邀请他来共进
晚餐。
对于余下的两位嘉宾中的每一位， 都打印一条消息， 指出他依然在受邀人之列。
使用del 将最后两位嘉宾从名单中删除， 让名单变成空的。 打印该名单， 核实程序结束时名单确实是空的。
'''
names = []
names.append('张学友')
names.append('奥黛丽赫本')
names.append('Michel Jackson')                  #

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