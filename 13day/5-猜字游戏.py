import random
s_s = random.randint(1,100)
for i in range(10):#定义智能输入１０次
    s_a = int(input("请输入数字"))
    if s_a > s_s:
        print("输大了")
    if s_a < s_s:
        print("书笑了")
    else:
        print("猜对了%d"%s_a)
        break 
