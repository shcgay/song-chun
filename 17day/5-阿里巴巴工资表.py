print("阿里巴巴员工内部系统".center(30,"*"))
print("1:录入信息".center(20," "))
print("2:查询信息".center(20," "))
print("3:删除信息".center(20," "))
print("4:退出系统".center(20," "))
list = []
while True:
    fun_ch = input("请选择功能")
    if fun_ch == 1:
        print("录入信息")
        for i in list:
            flag = 0
            cards = {}
            name = input("请输入名字")
            name = i["name"]
            flag = 1
            break
        if flag == 0:
            print("不在里面")
            gonghao = int(input("请输入功耗"))
            age = int(input("请输入年龄"))
            job = input("请输入工作岗位")
            gongzi = float(input("请输入工资")) 
            date = input("请输入入港日期") 
            cards["gonghao"] = gonghao
            cards["age"] = age
            cards["job"] = job
            cards["gongzi"] = gongzi
            cards["date"] = date         
            list.append(cards)
            print("录入成功")
        

