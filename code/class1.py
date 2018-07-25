'''
9-1 餐馆 ： 创建一个名为Restaurant 的类， 其方法__init__() 设置两个属性： restaurant_name 和cuisine_type 。 创建一个名
为describe_restaurant() 的方法和一个名为open_restaurant() 的方法， 其中前者打印前述两项信息， 而后者打印一条消息， 指出餐馆正在营业。
根据这个类创建一个名为restaurant 的实例， 分别打印其两个属性， 再调用前述两个方法。
9-2 三家餐馆 ： 根据你为完成练习9-1而编写的类创建三个实例， 并对每个实例调用方法describe_restaurant() 。
'''
class restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def describe_restaurant(self):
        print(self.name.title(),self.type.title())
    def cuisine_type(self):
        print(self.name.title(),'正在营业！')

restaurant1 = restaurant('A','111')
restaurant1.describe_restaurant()
restaurant1.cuisine_type()
restaurant2 = restaurant('B','345')
restaurant2.describe_restaurant()
restaurant2.cuisine_type()