'''
'''
#简单创建一个字典
dict1 = {'name':'value'}
print(dict1)


#元祖可以为key
'''
元组可以作为 dict 的 key，但列表不能作为元组的 key。
这是由于 dict 要求 key 必须是不可变类型，但列表是可变类型，因此列表不能作为元组的 key
'''
dict2 = {(2,3):'abc',3:'def'}
print(dict2)

'''
将一个列表转换成字典
'''
vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
dict3 = dict(vegetables)
print(dict3)

'''
将一个元祖转换成字典
'''
vegetables = (('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19))
dict4 = dict(vegetables)
print(dict4)

'''
列表，元祖，必须由长度为2的子列表或者子元祖组成
'''
cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
dict5 = dict(cars)
print(dict5)


'''
指定关键字来创建字典，此时关键字不能为表达式，也即是说spinach和cabbage 不能是变量
key = 'name'
info = dict(key = 'cold')
这样无效，info 还是# {'key': 'cold'}
'''
dict6 = dict(spinach = 1.39, cabbage = 2.59)
print(dict6) # {'spinach': 1.39, 'cabbage': 2.59}
