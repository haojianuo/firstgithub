
f = open('D:/workspase/frstPython/firstgithub/code/test.txt','a')
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            f.write("%d*%d=%2d " % (i,j,i*j))
    f.write ('\n')