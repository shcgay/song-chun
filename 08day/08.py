s_account = input("请输入账号")
s_password = input("请输入密码")
while s_account == account and s_password == password:
    print("登录成功")
    s_hero = int(input("选择英雄 0=adc 1= 肉 3=法师"))
    if s_hero == 0:
        print("鲁班大师")
    elif s_hero == 1:
        print("程咬金")
    elif s_hero == 3:
        print("王昭君")
                   
    
       # 1. 定义重复次数计算器        
        count="1"
        sum="0"
        while count < 11:
        sum = sum+count
            print("sum=%d,count=%d"%(sum,count))
        count = count + 1
            print("循环结束后的count=%d"%count)
        




i = 1
d_sum = 0 #定义偶数的和
s_sum = 0 #定义奇数的和
while i <=100:
    if i%2 == 0:# 偶数
        d_sum+= i#加起来一定是偶数
    else:
        s_sum+= i#加起来一定是奇数
    i+=1
print(%d %d_sum) 
print(%d %s_sum)


























