list = []
all_count = 0
while True:
    fun = input("请输入你的需求 1:计算 2:乘坐")
    if fun == 1:
        print("计算")
    elif fun == 2:
        print("乘坐")
    for i in range(1,13):
        cards = {}
        sum = 0
        global all_count
        month = int(input("请输入月份"))
        if month < 0 and month > 12:
            print("输入非法")
            return
        count = int(input("请输入乘坐的次数"))
        if count <=0:
            print("输入有误")
            return
        money = 0
        dis = float(input("请输入距离"))
        if dis <=0:
            print("输入有误")
            return
        all_count +=30*count
        for i in renge(1,30*count+1):
            if dis <= 6:
                money = 3
            elif dis > 6 and dis <= 12:
                money = 4
            elif dis >12 and dis <=22:
                money = 5
            elif dis > 22 and dis <= 32:
                money = 6
            elif dis > 32:
                if (dis - 32)%20 == 0:
                    money = 6 + (dis-32)/20
                else:
                    money = 6 + int((dis-32)/20) + 1
                if sum >= 100 and sum < 150:
                    money = money * 0.8
                elif sum >= 150 and sum < 400:
                    money = money * 0.5
                    sum = sum + money
        cards["month"] = sum
        list.append(cards)
        all_sum = 0
        for i in list:
            for k,v in i.items():
                all_sum+=v   
                print("%d月花了%0.2f元"%(k,v))
        print("总共花了%0.2f"%all_sum)
        print("总共做了%d次"%all_sum)



print("%d月花了%0.2f"%(i,sum))
