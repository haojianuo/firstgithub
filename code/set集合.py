student={'Tom','Li Hua','Jerry','Tom','John'}
print(student)              #集合中，重复元素会被删除

# 成员测试
if('Jerry' in student) :
    print('Jerry 在集合中')
else :
    print('Jerry 不在集合中')

#集合运算
a=set('dsfsajikas')
b=set('dsafdsqfdv')
print(a)
 
print(a - b)     # a和b的差集
 
print(a | b)     # a和b的并集
 
print(a & b)     # a和b的交集
 
print(a ^ b)     # a和b中不同时存在的元素
input('按下enter可退出')