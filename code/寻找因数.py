num=int(input('number='))
i=2
while True:
    if num%i == 0:
        print(i)
        num=num/i
    else:
        i+=1
    if num == 1:
        break
print(num)