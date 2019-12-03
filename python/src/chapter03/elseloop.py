'''
Created on 2019年12月4日

@author: Ellite Service
'''
#只有循环正常结束了才会去执行else里面的语句
import random
num=[1,2,3,4,5,6]
for i in num:
    if i == random.randint(1,12):        
        print('循环未正常结束终止于',i)
        break;
else:
    print('循环正常结束')