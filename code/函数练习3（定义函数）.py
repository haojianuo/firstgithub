import math

def quadratic(a, b, c):
        delta= pow(b,2)-(4*a*c)
        if delta < 0:
            return None
        else:
            sprt=math.sqrt(delta)
            x1=(-b+sprt)/(2*a)
            x2=(-b-sprt)/(2*a)
            return(x1,x2)

print('欢迎使用二次方程求解系统')
a=float(input('请输入a的值:'))
b=float(input('请输入b的值:'))
c=float(input('请输入c的值:'))
result=quadratic(a,b,c)
if  result is not None:
    print('解为x1=%.2f,x2=%.2f'%result)
else:
    print('方程无解')

input('按下回车以退出')