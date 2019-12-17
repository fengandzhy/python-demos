'''
1.  元组可以在映射中作为键值使用，而列表是不能作为键值使用
2.  很多内建函数和方法的返回值就是元组，所以在使用这些函数和方法是必须使用元组
'''
#元祖用小括号来定义，另外元祖不能修改
a=(1,2,3)
b=((2,)*20)
print(a)
print(b)

alist = [1,2,3]
blist = [4,5,6]
print(alist+blist)

atuple = (1,2,3)
btuple = (4,5,6)
print(atuple+btuple)

#元祖和列表的相互转换
print(alist+list(btuple))
print(atuple+tuple(blist))

