'''
Created on 2020年1月1日

@author: Ellite Service
'''
numbers = []
index = 1
while index<=100 :
    if index%3==0 :
        if index%5==0 :
            numbers.append(index)        
    index = index +1
print(numbers)
        
