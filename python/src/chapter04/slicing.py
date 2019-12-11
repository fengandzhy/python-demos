# 分片（Slicing)
# 分片：从一个序列中获取子序列
# 分片有3个参数：startIndex、endIndex和step
#  分片可以截取子字符串

url="https://geekori.com"
print(url[0:5])
print(url[8:len(url)])

#负数的截取法永远无法截取到最后一个字母
print(url[-3:-1])

#默认步长为整数，所以要确保第二个数的绝对值要大于第一个数
numbers = [1,2,3,4,5,6,7,8]
print(numbers[1:3])
print(numbers[-3:0]) #[]
print(numbers[4:-1]) #[5,6,7]
print(numbers[-3:8]) #[6,7,8]
print(numbers[-3:]) 


#设置步长
print(numbers[0:8:2])
print(numbers[1:8:2])

#当步长为负数时，要确保第一个数绝对值大于第二个数
print(numbers[::-2])
print(numbers[6::-2])
