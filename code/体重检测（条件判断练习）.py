h=input('输入您的身高(单位：cm)')
height=float(h)/100
w=input("输入你的体重(单位：Kg)")
weight=float(w)

bmi=(weight/(height**2))
print('您的BMI为：%.2f'%(bmi))

if bmi>32:
    print('你真的太重啦！！！')
elif bmi>28 and bmi<32:
    print('你的体型肥胖哦。')
elif bmi>25 and bmi<28:
    print('你有点小沉。')
elif bmi>18.5 and bmi<25:
    print('哇！完美的体重！')
else:
    print('你太轻了= =')  

input('按下enter可退出')