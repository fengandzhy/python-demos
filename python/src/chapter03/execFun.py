'''
Created on 2019年12月5日

@author: Ellite Service
'''
#exec 执行语句的
codes = ""
while True:
    code = input('>>>')
    #当输入为回车时执行语句
    if code == "":
        exec(codes)
        codes = ""
        continue
    codes +=code + "\n"
    