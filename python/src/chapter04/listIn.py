# 检查某个值是否属于一个序列
# in运算符：返回布尔类型值

#右边必须是字符串才能保证登录成功
accounts = [
    ['Frank',123],
    ['Sam',456],
    ['Peggy','789']
    ]
username=input("用户名:")
password=input("密码:")
if [username,password] in accounts:
    print('登录成功')
else:
    print('登录失败')

