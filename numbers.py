#-*-coding:utf-8 -*-
#���������б�
#ʹ�ú���range()
for value in range(1,5):   #����ҿ�
  print(value)

#ʹ��list���������б�
numbers=list(range(1,6))
print(numbers)

#range()������ָ������
even_numbers=list(range(2,11,2))
print(even_numbers)

#����һ���б����ʮ��������ƽ��
squares=[]
for value in range(1,11):
   squares.append(value**2)
print(squares)

#�������б�ִ�м򵥵�ͳ�Ƽ���
#python����

#�б��������ʡ�£�
squares=[value**2 for value in range(1,11)]
print(squares)
