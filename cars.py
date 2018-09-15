#-*-coding:utf-8 -*-
#组织列表（数组排序？）
#使用sort()对列表进行永久性排序
cars=['bmw','audi','toyota','subaru']
cars.sort();    #按字母序
print(cars)

#sort按字母逆序
cars.sort(reverse=True)
print(cars)

#使用sorted()对列表进行临时排序
print('here is the sorted list:')
print(sorted(cars))
print('here is the original list:')
print(cars)

#倒着打印列表
cars.reverse()
print(cars)

#确定列表长度
#print（len(cars))?? cmd中可行

