'''
Created on 2020年1月1日
求从1到100的数字中所有能既能被3整除，又能被5整合的数字有哪些
@author: Ellite Service
'''
numbers = []
index = 1
while index<=100 :
    if index%3==0 and index%5==0 :
        numbers.append(index)        
    index = index +1
print(numbers)
        
