'''
x == y  x等于y
x < y   x 小于 y
x > y   x 大于 y
x <= y  x 小于等于 y
x >= y  x 大于等于 y
x != y  x 不等于 y

x is y   x和y是同一个对象
x is not y  x和y不是同一个对象

x in y   x 是 y容器的成员，y是列表[1,2,3,4]，1 in y,10 in y
x not in y  x 不是y容器的成员


'''

x=23
y=22 
s1="Hello"
s2="World"

#逻辑与
if x<y and s1<s2:
    print('满足条件')
elif s1<s2:
    print('满足部分条件')
else:
    print('不满足条件')
    
#逻辑或
if x<y or s1<s2:
    print('满足条件')
else:
    print('不满足条件')


