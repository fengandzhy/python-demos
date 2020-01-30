'''
Created on 2020年1月30日

@author: Ellite Service
'''
x = 1234.56789

#保留小数点后两位
print(format(x, '0.2f'));

#右对齐
print(format(x, '>12.2f'));

#左对齐
print(format(x, '<12.2f'));

#补零右对齐
print(format(x, '0>12.2f'));

#补零左对齐
print(format(x, '0<12.2f'));

#中间对齐
print(format(x, '^12.2f'));

#补零中间对齐
print(format(x, '0^12.2f'));

#加上千分位
print(format(x, ',.2f'));


#加上千分位右对齐
print(format(x, '12,.2f'));

