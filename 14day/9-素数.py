from random import randint
n = randint(1,100)
print("生程序奇数%d"%n)
i=0
while True:
    num = int(input("请输入数字"))
    i+=1
    if num < n:
        print("输大了")
    elif num >n:
        print("书笑了")
    else:
        print("数字正确")
        break
        print("一共才了%d次"%i)
    if num <=5:
        print("......")
    else:
        print(":::::::")
