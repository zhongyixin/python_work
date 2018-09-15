#-*-coding:utf-8 -*-
#元组
#看起来像列表但用了圆括号
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#修改元组元素的操作是被禁止的

#遍历元组中的操作是和列表一样的
for dimension in dimensions:
	print(dimension)

#修改整个元组变量是可以的
dimensions=(400,100)
print(dimensions)
