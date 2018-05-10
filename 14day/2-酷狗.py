print("Hello 酷狗".center(20,"*"))
print("1:打开菜单".center(20," "))
print("2:新增歌曲".center(20," "))
print("3:删除歌曲".center(20," "))
print("4:查找歌曲".center(20," "))
print("5:修改我喜欢的歌曲".center(20," "))
print("6:定时关与开".center(20," "))
print("7:退出酷狗".center(20," "))
list = []
while True:
    classes = input("请选择操作功能")
    if classes == 7:
        print("goodbay")
        break
    elif classes == 1:
        print("新增")
        flag = 0
        s_song = {}
        name = input("请输入名字")
        for i in list():
            if name == i("name"):
                flag = 1
                break
        if flag == 1:
            print("名字重复了")
            continue
        music = ("请输入歌曲名字:")
        music1 = ("请输入歌曲名字:")
        music2 = ("请输入歌曲名字:")
        music3 = ("请输入歌曲名字:")
        s_song["music"] = music
        s_song["music1"] = music1
        s_song["music2"] = music2
        s_song["music3"] = music3
        list.append(s_song)
        print("新增成功\n")
    elif classes == 4:
        nsme = ("请输入要查的歌曲名字:")
        flag = 0
        count = 0
        for i in  list():
            count+=1
            if name == i["name"]:
                flag = 1
                break
            if flag == 1:
                print("没有找到此歌曲")
            else:
                print("歌名:%s\n歌名1:%s\n歌名2:%s\n歌名3:%s\n"%list[count-1]["music"],list[count-1]["music1"],list[count-1]["music2"],list[count-1]["music3"])
    elif classes == 5:
        name = ("请输入要修改的名字")
        for i in list():
            if name == i["name"]:
                print("1:修改歌曲名字:".center(20," "))
                print("2:修改歌曲1名字:".center(20," "))
                print("3:修改歌曲2名字:".center(20," "))
                print("4:修改歌曲3名字:".center(20," "))
                s_chun = input("请选择功能")
                if s_chun == 1:
                    name = input("请输入新的名字")
                    i["name"] = name
                elif s_chun == 2:
                    name1 = input("请输入新的名字")
                    i["name"] = name1
                elif s_chun == 3:
                    name2 = input("请输入新的名字")
                    i["name"] = name2
                elif s_chun == 4:
                    name3 = input("请输入新的名字")
                    i["name"] = name3
                else:
                    print("输入有误")
    elif classes == 3:
        name = input("请输入要删除的歌曲名字")
        flag = 0
        for i in list():
             if name == i["name"]:
                 flag = 1
                 s_fang = int(input("确定删除吗1:确定 2:不删除"))
                 if s_fang == 1:
                     list.remove(i)
                     print("删除成功")
                     break
        if flag == 0:
            print("没有此类歌曲")                    
    elif classes == 6:
        print("打开定时")
    elif classes == 7:
        print("退出酷狗")
        break
        
        
