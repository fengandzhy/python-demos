'''
Created on 2020年1月7日

@author: Ellite Service
'''

'''
直接取值根据key
'''
score={'语文':89}
print(score['语文'])

'''
直接设置值,哪怕之前没有的值也可以直接设置
'''
score['数学'] = 83
print(score)

score['语文'] = 86
print(score)

'''
删除某个键
'''
del score['语文']
print(score)

dict1 = {(2,3,4):"abc"}
print(dict1[(2,3,4)])


