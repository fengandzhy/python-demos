'''
python初始化字典有两种方法
1. 大括号直接定义 info = {'name','value'}
2. 用dict函数将一个序列转换为字典,但是这个序列的长度必须是2或者必须是由长度为2的子序列组成4


'''
dict1 = {'name','value'}
print(dict1)
dict2 = {(2,3):'abc',3:'def'}
print(dict2)

items = [['Bill',"4321"],("Mike","7891"),['John','4567']]
d = dict(items)
print(d)

