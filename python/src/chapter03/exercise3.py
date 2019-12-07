'''
Created on 2019年12月8日

@author: Ellite Service
'''
lines = int(input('请输入行数必须为奇数:'))
if lines%2 !=0:
    line = 1
    while line <=lines:
        if line <= lines//2+1:
            startNum = 2*(line-1)+1            
        else:
            startNum = 2*(lines-line)+1            
        spaceNum = (lines - startNum)//2
        print(' '*spaceNum+'*'*startNum+' '*spaceNum)
        line +=1
         
        
