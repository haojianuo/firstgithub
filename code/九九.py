for i in range(1,10):
    for j in range(1,10):
        if i>=j:
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print ()
input('press enter to exit')