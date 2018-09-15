#-*-coding:utf-8 -*-
#列表
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())

#python最后一个元素，可将索引指定-1
print(bicycles[-1])

#修改列表元素，直接赋值？？即可
bicycles[0]='honda'
print(bicycles)

#在列表末尾添加元素
bicycles.append('forever')
print(bicycles)

#在列表中插入元素
bicycles.insert(1,'ducati')
print(bicycles)

#从列表中删除元素
#del法
del bicycles[2]
print(bicycles)
#pop法 删除末尾元素
popped_bicycle=bicycles.pop()
print(bicycles)
print(popped_bicycle)
#pop法删除任何位置元素
first_owned=bicycles.pop(0)
print('the first bicycle I owned was a '+first_owned.title()+'.')
#根据具体data删除元素
bicycles.remove('ducati')
print(bicycles)
#remove()只删除第一个指定的值，如果要删除的值在列表中出现多次，需要使用循环来判断

