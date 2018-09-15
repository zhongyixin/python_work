#-*-coding:utf-8 -*-
#创建数字列表
#使用函数range()
for value in range(1,5):   #左闭右开
  print(value)

#使用list创建数字列表
numbers=list(range(1,6))
print(numbers)

#range()函数可指定步长
even_numbers=list(range(2,11,2))
print(even_numbers)

#创建一个列表包含十以内数的平方
squares=[]
for value in range(1,11):
   squares.append(value**2)
print(squares)

#对数字列表执行简单的统计计算
#python环境

#列表解析，（省事）
squares=[value**2 for value in range(1,11)]
print(squares)
