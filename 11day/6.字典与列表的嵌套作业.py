list = []
name_list = []
count =  0
while True:
    if count == 3:
    	break
    #输入
    dict = {}
    #for i in list:
    #    name_list.append(i.get("name"))


    name =  input("请输入你的名字")
    age = int(input ("请输入你的年龄"))
    sex = input("请输入你的性别")
    qq = int(input("请输入你的qq号"))
    weight = float(input("请输入你的体重"))
    #字典赋值
    if name not in name_list:


        dict["name"] = name
        dict["age"] = age
        dict["sex"] = sex
        dict["qq"] = qq
        dict["weight"] = weight

        #list = [{}]
        list.append(dict)
        print(list)
        count +=1
    else:
        print("名字冲了")


age_sum = 0

#遍历
for i in list:
    
    age_sum = age_sum + i.get("age")



    print(i)
print("年龄的平均值是%0.2f"%(age_sum/len(list)))
