'''
用Template类格式化字符串
'''
#用template的substitute方法
from string import Template
template1 = Template('I love $p and $J')
print(template1.substitute(p='Python',J='Java'))


template1 = Template('I hava $dollar$$ it equals $RMB')
print(template1.substitute(dollar='30',RMB='￥50'))

template4 = Template("$dollar$$相当于多少$pounds")
data = {}
data['dollar'] = 100
data['pounds'] = '英镑'
print(template4.substitute(data))