age = int(input("请输入年龄"))
if age < 2:
    print("他是婴儿")
        
elif 2 <= age <4:
    print("胖善学步")
elif 4 <= age <13:
    print("他是儿童")
    print("正在参加六一儿童节")
elif 13 <= age<20:
    print("他是青年")
elif 20 <= age<65:
    print("他是成面额")
else:
    print("他已经死去")
