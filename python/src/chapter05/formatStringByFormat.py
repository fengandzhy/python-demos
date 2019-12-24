'''
使用format方法格式化字符串
'''
# 按顺序来指定格式化参数值
s='Today is {} and the temperature is {} degree'
print(s.format('Sunday', '30'))

# 使用命名格式化参数
s='Today is {day} and the temperature is {degree} degree'
print(s.format(day='Sunday', degree=30))

# 使用序号格式化参数
s='{1}{3}{2}{0}{4}'
print(s.format('a','b','c','d','e'))




