# 服务器存的账号
print("欢迎来到英雄联盟")
s_acc = "742156464"
s_pwd = "sixtoisme5555"
choose_login = int(input("请选择登录方式 1=盒子登录 2=tgp登录 3=账号登录"))
if choose_login == 1:
    print("盒子登录成功")
yonghu = int(input("请选择大区 4=扭曲森林 5=恕瑞玛 6=德玛西亚"))
if yonghu == 4:
    print("登录扭曲森林成功")
elif yonghu == 5:
    print("登录恕瑞玛成功")
elif yonghu == 6:
    print("登录德玛西亚成功")
player = int(input("请选择英雄 7=亚索 8=薇恩 9=剑圣 10=机器 11=德玛"))
if player == 7:
    print("选择亚索")
elif player == 9:
    print("选择剑圣")
elif player == 8:
    print("选择薇恩")
elif pllayer == 10:
    print("选择机器")
elif player == 11:
    print("选择德玛")




elif choose_login == 2:
    print("tgp登陆成功")
elif choose_login == 3:

 account = input("请输入账号")
 password = input("请输入密码")
 if (account == s_acc) and (password == s_pwd):
     print("账号登录成功")
else:
    print("登录失败")


