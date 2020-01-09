'''
如果要判断字典是否包含指定的 key，则可以使用 in 或 not in 运算符。需要指出的是，对于 dict 而言，in 或 not in 运算符都是基于 key 来判断的
'''

cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print('BMW' in cars)
print('WAS' in cars)
print('WMT' not in cars)
