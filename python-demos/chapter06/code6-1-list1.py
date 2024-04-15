list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print(list1[3])
print(list1[2:8:2])  # 从2 开始 到 8 结束, 中间隔 2

print(list1 + list('123456'))

numeric_list = list(map(int, '123456'))  # 这里的int 是函数
print(numeric_list)

"""
在 Python 中，当使用 < 比较两个列表时，比较是基于列表的元素进行的，类似于字典序比较。
这种比较首先检查两个列表的第一个元素，然后根据这些元素的值决定结果。
如果第一个元素相等，则比较下一个元素，依此类推，直到找到不相等的元素或者一个列表的元素耗尽。
"""
print([3, 2, 3, 4] < [2, 1])

list2 = ['a','c','d']
print(len(list2))  # 求元素个数
print(max(list2))  # 求元素的最大值
print(min(list2))  # 求元素的最小值
