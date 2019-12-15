# 列表方法
'''
1. append：在列表最后插入新的值
2. clear：用于清除列表的内容
3. copy：用于复制一个列表
4. count：用于统计某个元素在列表中出现的次数
5. extend：用于在列表结尾插入另一个列表，也就是让两个列表首尾相接。
   该方法改变的是被扩展的列表。 list1.extend(list2),列表的相加创建一个新的列表
6. index：用于从列表中找出某个值第一次出现的索引位置
7. insert：用于将值插入到列表中的指定位置
8. pop：用于移除列表中的元素（默认是最后一个元素），并返回该元素的值
9. remove：用于移除列表中某个值的第一次匹配项
10. reverse：用于将列表中的元素反向存放
11. sort：用于对列表进行排序，调用该方法会改变原来的列表
'''
print("--------append方法---------")
number=[1,2,3,4,5]
number.append(6)
number.append('a')
number.append([1,2,3])
print(number)

print("---------clear方法---------")
names = ["Bill", "Mary"]
print(names)
names.clear()
print(names)

print("----------copy方法----------")
a = [1,2,3,4,5]
acopy = a
acopy1 = a[:]
acopy2 = a.copy()
a[3] = "hello"
print(acopy)
print(acopy1)
print(acopy2)

print("----------count方法-----------")
search = ["he", "new", "he", [1,2,3],"he", "world", "peter",[1,2,3]]
# 搜素“he”在search出现的次数
print(search.count("he"))

print(search.count([1,2,3]))

print(search.count(20))  # 如果没有找到指定的列表元素，返回0

print("------extend方法------")

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
a[2] =123
print(a)
a = [1,2,3]
b = [4,5,6]

x = a
a = a + b
x[2] = 543
print(a)

print("------index方法------")
numbers = [5,3,6,8]
print(numbers.index(6))
# print(numbers.index(10))  # 如果指定的值在列表中不存在，会抛出异常

print("-------insert方法-------")
numbers = [1,2,3,4,5]
#numbers.insert(3,"four")
#print(numbers)

# 使用分片赋值完成同样的效果
numbers[3:3] = ["four"]
print(numbers)

print("-------pop方法-------")
numbers = [1,2,3]
print(numbers.pop())
print(numbers.pop(1))
print(numbers)

print("---------remove方法---------")
words = ["he", "new", "he","yes"]
words.remove("he")
print(words)

print("------reverse方法--------")
numbers = [1,2,3,4,5,6,7]
numbers.reverse()

print(numbers)

print("--------sort方法-------")
numbers = [4,3,1,7,4,83,2,-3]
# numbers.sort()
# print(numbers)

numbers1 = numbers[:]
numbers1.sort()
print(numbers)
print(numbers1)


# 使用sorted函数
x = [7,5,4,9,4]
y = sorted(x)
print(x)
print(y)

print(sorted("geekori.com"))
x = [7,3,9,2,1,12]
x.sort(reverse = False)
print(x)



