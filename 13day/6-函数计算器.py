i = 0
number = input("请输入符号1:+ 2:- 3:* 4:/")
def song(x,y,number):
    for i in range(10):
        if number == 1:
            print("和是%d"%number)
        elif number == 2:
            print("减数是%d"%number)
        elif number == 3:
            print("积是%d"%number)
        elif number == 4:
            print("商是%d"%number)
        else:
            print("输入错误")
x = int(input("请输入你要的数字"))
y = int(input("请输入你想要的数字"))
number = int(input("请输入你想要的数字"))
i+=1
song(x,y,number)
