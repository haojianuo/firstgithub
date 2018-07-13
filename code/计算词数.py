st=input('请输入一句话（中英文都可以）')
a=0
b=0
for x in st:
        if x!=' ':
            a=a+1
        else:
            b=b+1
   
print('这句话中一共有'+ str(a) +'个单词')
print(str(b),'个空格')