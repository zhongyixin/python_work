#-*-coding:utf-8 -*-
#ʹ���б��һ���֣���Ƭ
players=['charles','martina','michael','florence','eli']
print(players[0:3])
#��ָ����һ���������Զ��ӱ�ͷ��ʼ
print(players[:4])
#ʡ����ֹ�������Զ�����β
print(players[2:])
#���Ҫ����������
print(players[-3:])

#������Ƭ
for player in players[:3]:
	print(player)

#�����б�  (��=����
other_players=players[:]
print(other_players)
