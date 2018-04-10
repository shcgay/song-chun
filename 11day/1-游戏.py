list = [["传奇","贪玩蓝月"],["QQ飞车","QQ炫舞"],["天天酷跑","天天炫斗"],["王者荣耀","绝地求生"]]

list[1]=["QQ飞车","QQ炫舞"]
list[2]=["天天酷跑","天天炫斗"]
list[3]=["王者荣耀","绝地求生"]
list.pop(list[1])
list.pop(list[2])
list.pop(list[3])
for i in list:
    print("这个游戏叫%s"%传奇)
    print("这个游戏叫%s"%贪玩蓝月)

