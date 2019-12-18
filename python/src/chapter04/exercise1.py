'''
输入一个整数，回车结束，然后降序排列
'''
numbers = []
while True:
    number = input('请输入一个整数,回车结束')
    if number == '':
        break
    numbers.append(int(number))
numbers.sort(reverse=True)
print(numbers)

