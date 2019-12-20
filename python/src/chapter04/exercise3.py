'''
Created on 2019年12月20日

@author: Ellite Service
'''
num = input('请输入一个大于1的整数:')
value1 = []
lines = int(num)
begin = 0
while begin<lines:
    i = 1
    tempValue = []
    while i <=lines:
        tempValue.append(begin*lines+i)
        i +=1
    begin += 1
    value1.append(tempValue)
print(value1)
    
begin = 0
value2 = []
while begin<lines:
    i = 0
    tempValue = []
    while i<lines:
        tempValue.append(value1[i][begin])
        i +=1
    begin +=1
    value2.append(tempValue)
print(value2) 




