'''
字符串格式化基础
'''
# 字符串格式化：静态和动态两部分  
# Hello Bill    Hello 李宁   Hello 张三
# Hello param_name  模板
# 字符串格式化就是把一个或多个值替换另一个字符串的某个标记

# %：格式化字符串
# step1:定义一个模板  %s：字符串类型标记
tempStr = 'Hello %s, Welcome to %s' #%s用来代替字符串
value1 = ('Sam','Hamilton') #元祖，里面的元素是来代替上面的占位符
print(tempStr % value1)


from math import pi
tempStr = 'Hello PI is %.2f, keep %d after the dot' #%f 和 %d 用来表示浮点数和整数
value2 = (pi,2)
print(tempStr % value2)

tempStr = 'It is %d%% success, after %s, it will be %d%%' #%在这里是转义的意思
value2 = (30,'temp',70)
print(tempStr % value2)

