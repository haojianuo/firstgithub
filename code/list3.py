'''
1.想出至少5个你渴望去旅游的地方。
2.将这些地方存储在一个列表中， 并确保其中的元素不是按字母顺序排列的。
3.按原始排列顺序打印该列表。 不要考虑输出是否整洁的问题， 只管打印原始Python列表。
4.使用sorted() 按字母顺序打印这个列表， 同时不要修改它。
5.再次打印该列表， 核实排列顺序未变。
6.使用sorted() 按与字母顺序相反的顺序打印这个列表， 同时不要修改它。
7.再次打印该列表， 核实排列顺序未变。
8.使用reverse() 修改列表元素的排列顺序。 打印该列表， 核实排列顺序确实变了。
9.使用reverse() 再次修改列表元素的排列顺序。 打印该列表， 核实已恢复到原来的排列顺序。
10.使用sort() 修改该列表， 使其元素按字母顺序排列。 打印该列表， 核实排列顺序确实变了。
11.使用sort() 修改该列表， 使其元素按与字母顺序相反的顺序排列。 打印该列表， 核实排列顺序确实变了。
'''
travel_place=['Japan','America','Taiwan','Hongkong','Shanghai']
print(travel_place)
print(sorted(travel_place))
print(travel_place)
print(sorted(travel_place,reverse=True))
print(travel_place)
travel_place.reverse()
print(travel_place)
travel_place.reverse()
print(travel_place)
travel_place.sort()
print(travel_place)
travel_place.sort(reverse=True)
print(travel_place)