'''
更进一步控制字符串格式化参数
'''
s1 = "原样输出：{first!s}  调用repr函数：{first!r}  输出Unicode编码：{first!a}"
print(s1.format(first = "中"))

s1 = "原样输出：{first:s}  调用repr函数：{first!r}  输出Unicode编码：{first!a}" 
print(s1.format(first = "中"))

s3 = "十进制：{num}  二进制：{num:b} 八进制：{num:o}  十六进制：{num:x}"
print(s3.format(num = 78))


# 将整数按科学计数法
s4 = "科学计数法：{num:e}"
print(s4.format(num =6789))

#  将浮点数按百分比输出
s5 = "百分比：{num:%}"
print(s5.format(num = 0.34))


'''
a  将字符串按Unicode编码输出
b  将一个整数格式化为一个二进制数
c  将一个整数解释成ASCII
d  将整数格式化为十进制的数
e/E  科学计数法表示
f/F  将一个整数格式化为浮点数，（nan和inf）转换为小写
g/G  会根据整数值的位数，在浮点数和科学计数法之间切换，在整数位超过6位时，与e相同，否则与f相同
o   将一个整数格式化为八进制
s   按原样格式化字符串
x/X 将一个整数格式化为十六进制数
%   将一个数值格式化为百分比形式

'''
