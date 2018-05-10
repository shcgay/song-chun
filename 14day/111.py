from random import randint
n = randint(1,100)
print("生成随机数%d"%n)
i = 0
while True:
    num = int(input("请输入数字"))
    i+=1
    if num > n:
        print("输大了")
    elif num < n:
        print("速效了")
    else:
        print("回答正确")
        break

        print("一共才了%d次"%i)
        if i <=5:
            print("123456")
        else:
            print("789")
