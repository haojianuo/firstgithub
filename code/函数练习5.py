def ave(nums):
    i=0
    l=0
    for x in nums:
        i=x+i
        l=l+1
    print(i/l)
number = [1,2,3,4,5,6,7,8,9,10,41]
ave(number)