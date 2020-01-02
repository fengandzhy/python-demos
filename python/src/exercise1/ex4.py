'''
Created on 2020年1月2日

@author: Ellite Service
'''
strIn = str(input("请输入字符串:"))
a1 = strIn.find("not")
a2 = strIn.find("bad")

if a1!=-1 and a2!=-1:
    if a1 < a2 :
        s1 = strIn[0:a1]
        s2 = strIn[a2+3:len(strIn)]
        strIn = s1+'good'+s2
print(strIn)
        


