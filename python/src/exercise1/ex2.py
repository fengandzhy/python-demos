'''
Created on 2020年1月1日

@author: Ellite Service
'''
strIn = str(input("请输入字符串:"))
length = len(strIn)
if length >= 3 :
    if strIn[-3:] == 'ing' :
        strIn = strIn + 'ly'
    else :
        strIn = strIn + 'ing'
    print(strIn)
else :
    print(strIn)    
    
