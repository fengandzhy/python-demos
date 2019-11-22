'''
Created on 2019年11月22日

@author: Ellite Service
'''
# 在Python语言中，每一种类型的值都可以被解释成布尔类型的值
# 都会被解释为False：None 0 ""  ()  []  {}

print('None = ',bool(None))
print('0 = ',bool(0))
print('"" = ',bool(""))
print('() = ',bool(()))
print('[] = ',bool([]))
print('{} = ',bool({}))

#Boolean 可以当成数值使用False 是0 True 是1
print(1 == True)
print(0 == False)
print(2 + True + False)




