"""
实战与练习
1.  请将下面的数值转成另外3种进制，并使用print函数输出转换结果。例如，如果数值是10进制，需要转换成2、8、16进制，如果是16进制，需要转换为2、8、10进制。
（1）12345
（2）0xF98A
（3）0b1100010110

"""


print(bin(12345))
print(oct(12345))
print(hex(12345))

print(bin(0xF98A))
print(oct(0xF98A))
#print(int(str(0xF98A),16))
print(int("0xF98A",16))


print(oct(0b1100010110))
print(int("0b1100010110",2))
#print(int(str(0b1100010110),2)) 不能这样做，str(0b1100010110)会自动转成790
print(hex(0b1100010110))

print(str(0b1100010110))
print(str(0xF98A))
