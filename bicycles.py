#-*-coding:utf-8 -*-
#�б�
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())

#python���һ��Ԫ�أ��ɽ�����ָ��-1
print(bicycles[-1])

#�޸��б�Ԫ�أ�ֱ�Ӹ�ֵ��������
bicycles[0]='honda'
print(bicycles)

#���б�ĩβ���Ԫ��
bicycles.append('forever')
print(bicycles)

#���б��в���Ԫ��
bicycles.insert(1,'ducati')
print(bicycles)

#���б���ɾ��Ԫ��
#del��
del bicycles[2]
print(bicycles)
#pop�� ɾ��ĩβԪ��
popped_bicycle=bicycles.pop()
print(bicycles)
print(popped_bicycle)
#pop��ɾ���κ�λ��Ԫ��
first_owned=bicycles.pop(0)
print('the first bicycle I owned was a '+first_owned.title()+'.')
#���ݾ���dataɾ��Ԫ��
bicycles.remove('ducati')
print(bicycles)
#remove()ֻɾ����һ��ָ����ֵ�����Ҫɾ����ֵ���б��г��ֶ�Σ���Ҫʹ��ѭ�����ж�

