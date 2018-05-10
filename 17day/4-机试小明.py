all_sum = 0
for i in range(1,13):
    sum = 0
    money = 0
    dis = 0
    if i == 1 or i == 12:
        dis = 32
    elif i == 2 or i == 11:
        dis = 18
    elif i == 3 or i == 10:
        dis = 7
    elif i == 4 or i == 9:
        dis = 80
    elif i == 5 or i == 8:
        dis = 34
    elif i == 6 or i == 7:
        dis = 70
        for j in range(0,60):
            if dis > 6:
                money = 3
            elif dis > 6 and dis <= 12:
                money = 4
            elif dis > 12 and dis <= 22:
                money = 5
            elif dis > 22 and dis <= 32:
                money = 6
            elif dis > 32:
                if (dis - 32)%20 == 0:
                    money = 6 + (dis - 32)/20
                else:
                    money = 6 + int((dis-32)/20) +1
            if sum >= 100 and sum < 150:
                money = money * 0.8
            elif sum >= 150 and sum < 400:
                money = money * 0.5
            sum = sum + money
        print("%d月花了%0.2f"%(i,sum))
        all_sum = all_sum + sum
print("钱是%0.2f"%all_sum)


