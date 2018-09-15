#-*-coding:utf-8 -*-
#使用列表的一部分：切片
players=['charles','martina','michael','florence','eli']
print(players[0:3])
#不指定第一个索引，自动从表头开始
print(players[:4])
#省略终止索引，自动到表尾
print(players[2:])
#如果要输出最后三个
print(players[-3:])

#遍历切片
for player in players[:3]:
	print(player)

#复制列表  (与=区别）
other_players=players[:]
print(other_players)
