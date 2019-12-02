'''
Created on 2019年12月3日

@author: Ellite Service
'''
#对于当前循环退出
names=['Bill','Mike','Mary','Bob']
for name in names:
    if not name.startswith('B'):
        break;
    print(name)
print('----------------------------------------')

#对于当前循环跳出本次循环
names=['Bill','Mike','Mary','Bob']
for name in names:
    if not name.startswith('B'):
        continue;
    print(name)
    
r1=[1,2,3,4,5,6]
languages = ['Java','Python','JavaScript','Go']
print('----------------------------------------')
for i in r1:
    for lang in languages:
        if not lang.startswith('J'):
            break;
        print(lang)
print('----------------------------------------')
for i in r1:
    for lang in languages:
        if not lang.startswith('J'):
            continue;
        print(lang)
