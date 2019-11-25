'''
Created on 2019年11月25日

@author: Ellite Service
'''
name = input(" 请输入您的名字")
if name.startswith('Bill'):
    if name.endswith('Gates'):
        print('Hello Bill Gates')
    elif name.endswith('Clinton'):
        print('Hello Bill Clinton')
    else:
        print('Hello Mr Bill')
else:
    print(name)