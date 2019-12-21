'''
字符串基本操作
'''
s1 = "I love python."
print(s1[7])
print(s1[11])
#  print(s1[15])

#  利用分片截取字符串的子字符串
print(s1[7:13])
print(s1[7:])

print(s1[::2])

s2 = "a b c d e f g"
print(s2[::2])

s3 = "abc"
print(s3 * 10)

print("python" in s1)
print("java" in s1)
print("java" not in s1)

print(len(s1))
print(max(s1))
print(min(s1))

