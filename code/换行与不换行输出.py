                            #以下是换行输出。默认为换行
x='a'
y='b'
print(x)
print(y)
print("Hello")
print('World')
                                 #以下是不换行输出
print(x,end=' ')
print(y)                             #输入end代表以什么为结尾，无则换行
print("Hello",end=',')
print('World')
input('按下enter可退出')