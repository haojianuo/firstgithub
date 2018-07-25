number = int(input('num='))
for i in range(2,number+1):
    if number%i == 0:             
        break  
if i==number:
    print('True Primery')
else:
    print('False')