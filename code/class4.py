'''
9-4 就餐人数 ： 在为完成练习9-1而编写的程序中， 添加一个名为number_served 的属性， 并将其默认值设置为0。 根据这个类创建一个名为restaurant 的实
例； 打印有多少人在这家餐馆就餐过， 然后修改这个值并再次打印它。
添加一个名为set_number_served() 的方法， 它让你能够设置就餐人数。 调用这个方法并向它传递一个值， 然后再次打印这个值。
添加一个名为increment_number_served() 的方法， 它让你能够将就餐人数递增。 调用这个方法并向它传递一个这样的值： 你认为这家餐馆每天可能接待的就
餐人数。
'''
class restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number_served=3
    def describe_restaurant(self):
        print(self.name.title(),self.type.title())
        print('营业人数：',str(self.number_served))
    def cuisine_type(self):
        print(self.name.title(),'正在营业！')
    def set_number_served(self,people):
        self.number_served = people
    def increment_number_served(self,people):
        self.number_served += people


    
restaurant = restaurant('金拱门','快餐')
restaurant.set_number_served(10)
restaurant.increment_number_served(2)
restaurant.describe_restaurant()
