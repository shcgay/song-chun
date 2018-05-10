print("lol游戏商店简易系统".center(30,"*"))
print("1:新增商品".center(20," "))
print("2:查找商品".center(20," "))
print("3:购买商品".center(20," "))
print("4:修改商品".center(20," "))
print("5:删除商品".center(20," "))
print("6:退出界面".center(20," "))
list = []
while True:
    s_a = int(input("请选择功能"))
    if s_a == 1:
        flag = 0
        name = input("请输入商品的名字")
        dict = {}
        for i in list:
            if name == i["name"]:
                flag = 1
                break
        if flag == 1:
            continue
        price = float(input("请输入你心里能够承受的价格范围"))
        password = int(input("请输入你的支付密码"))
        buy = input("请选择你要购买的商品")
        dict["buy"]
        dict["name"]
        dict["price"]
        dict["password"]
        list.append(dict)
        print("上架新的皮肤与英雄")
    if s_a == 2:
        name = input("请输入你需要查找的皮肤的名字")
        flag = 0#假设不在里面
        count = 0#默认找到了零次
        for i in list:
            count +=1#记录找的次数
            if name == i["name"]:
                flag = 1
                print("名字:%s\n商品名字:%s\n价格:%s\n支付密码:%s\n"%(i["name"],i["buy"],i["price"],i["password"]))
                break
        if flag == 0:
            print("不好卖,不受欢迎,商品已下架")
        else:
            print("名字:%s\n商品名字:%s\n价格:%s\n支付密码:%s\n"%(i["name"],i["buy"],i["price"],i["password"]))
    if s_a == 4:
        name = input("请输入你想修改商品的名字")
        for i in list:
            if name == i["name"]:
                print("7:修改商品名字".center(15," "))
                print("8:修改价格范围".center(15," "))
                print("9:修改购买的商品".center(15," "))
                print("10:修改支付密码".center(15," "))
                a_s = input("请选择修改的序号")
                if a_s == 7:
                    name = input("输入新的名字")
                    i["name"] = name
                elif a_S == 8:
                    price = float(input("输入新的价格"))
                    i["price"] = price
                elif a_s == 9:
                    buy =input("输入新的需要购买的商品")
                    i["buy"] = buy
                elif a_s == 10:
                    password = int(input("新的支付密码"))
                    i["password"] = password
                else:
                    print("你老马得")
    if s_a == 5:
        name = input("请输入你想删除的商品的名字")
        flag = 0
        for i in list:
            flag = 1
            ss_a == input("确定要删除1:yes 2:no")
            if ss_a == 1:
                list.remove(i)
                print("yes成功")
            break
        if flag == 1:
            print("傻叉")
    if s_a == 6:
        print("退出商城")
