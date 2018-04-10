# 游戏注册登录
lanqiao = []
while True:
    i = 0
    yeyu = {}
    name = input("请输入你的名字")
    for a in lanqiao:
        if name == a["name"]:
            i = 1
            print("名字重复了")
            break
    if i == 1:
        print("名字重复")
        continue 


    zhuce = input("请注册你的账号")
    fuwuqi = input("请选择服务大区")
    account = int(input("请输入你的账号"))
    yingxiong = input("请选择你的英雄")


    yeyu["name"] = name
    yeyu["zhuce"] = zhuce
    yeyu["fuwuqi"] = fuwuqi
    yeyu["account"] = account
    yeyu["yingxiong"] = yingxiong
    lanqiao.append("name")
    print("添加成功")
    break
