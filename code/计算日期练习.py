print('此程序可以计算这一天是一年的第几天')
year = int(input('年份:'))
month = int(input('月份:'))
day = int(input('日期:'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print ('错误！')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print ('这是今年的第%d天' % sum)

input('按下enter可退出')