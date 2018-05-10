lol游戏简易系统
print("LOL第十赛季版本".center(20,"*"))
print("1:新增英雄".center(20," "))
print("2:查找故去的英雄".center(20," "))
print("3:修改英雄天赋".center(20," "))
print("4:删除旧版符文".center(20," "))
system = []
while True:
    fun_number = int(input("请选择功能"))
    if fun_number == 1:
        print("新增")
        flag = 0
        lan = {}
        yingxiong = input("请选择你需要的英雄")
        for i in system:
            if yingxiong == i["yingxiong"]:
                flag = 1
                break
        if flag == 1:
            print("英雄已被选择")
            continue

        fuwen = input("请选择你需要的符文")
        tianfu = input("请选择你需要修改的天赋")
        g_yingxiong = input("请选择你要查找的英雄")
        lan["yingxiong"] = yingxiong
        lan["fuwen"] = fuwen
        lan["tianfu"] = tianfu
        lan["g_yingxiong"] = g_yingxiong
        system.append(lan)
        print("选择成功")
    elif fun_number == 3:
        print("修改")
    elif fun_number == 2:
        yingxiong = input("请输入你要查找的英雄名字")
        flag = 0
        count = 0
        for i in system:
            count+=1
            if g_yingxiong == lan["g_yingxiong"]:
                flag = 1
                break
            if flag == 0:
                print("查找错误")
            else:
                print(">>>>>>")
    elif fun_number == 4:
         fuwen = ("请选择你需要删除的符文")
         flag = 0
         for i in syste:
             if fuwen == i["fuwen"]:
                 flag = 1
                 sure_sg = int(input("1确定删除 2考路考路"))
                 if sure_sg == 0:
                 system.remove(lan)
                 print("已被清理")
             if flag == 0:
                 print("从未出现")
     else:
         break
