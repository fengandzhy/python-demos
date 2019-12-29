'''
# 字段宽度、精度和千位分隔符
#  100,000,000,000
'''

#字符串左对齐，数字右对齐
str1 = '{num:12}'
print(str1.format(num='3.1415926')) 

str1 = '{num:12}'
print(str1.format(num=3.1415926)) 


#带有精度的
str1 = '{num:12.2f}'
print(str1.format(num=3.1415926))

str1 = '{num:012.2f}'
print(str1.format(num=3.1415926))

str1 = '{num:012.2f}'
print(str1.format(num=3.1415926))


