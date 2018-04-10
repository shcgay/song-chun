#登录界面

list = []
while True:
    
        flag = 0 #默认值,０代表不在里面
        dict = {}
        name = input("请输入你的名字")
        for temp in list:
            if name ==  temp["name"]:
                flag = 1 #在里面
        if flag == 1:
            print("名字重复了")
            continue        
        fuwuqi = input("请选择你需要的服务器")
        zhuce =input("请注册你的账号")
        account =int(input("请输入你的账号"))

        denglu = input("请选择你需要的登录方式")





        dict["fuwuqi"] = fuwuqi
        dict["zhuce"] = zhuce
        dict["account"] = account
        dict["name"] = name
        dict["denglu"] = denglu
        list.append(dict)
        print("创建人物成功")





