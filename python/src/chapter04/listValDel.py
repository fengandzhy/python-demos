# 列表的基本操作
# 赋值、删除列表元素、分片赋值

#赋值,对列表里某个元素赋值
numbers = [1,2,3,4,5,6,7,8]
numbers[1] = 'a'
print(numbers)

#删除,删除列表里某个元素
del(numbers[1])
print(numbers)
print(numbers[1])

#分片赋值
numbers = [1,2,3,4,5,6,7,8]
numbers[4:8]=[]
print(numbers)

