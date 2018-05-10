#for i in range(1,10):
 #   for j in range(1,i+1):
  #      print("%d*%d=%d\t"%(i,j,i*j),end="")
   # print(" ")






print("1:账号注册".center,(20,"*"))
print("2:账号登录".center,(20,"*"))
list = []
while True:
    s_n = int(input("请选择功能"))
    if s_n == 1:
        flag = 0
        s_s = {}
        account = int(input("请输入账号"))
        for i in list:
            if account == i["account"]:
                flag = 1
                print("注册失败")
                break
        if flag == 0:
            print("名字重复")
            continue
        account = int(input("请重新输入账号"))
        s_s["account"] = account
        list.append(s_s)
        print("注册成功\n")
            
    

