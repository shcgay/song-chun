def age():
    age = int(input("请输入年龄"))
    if age > 0 or age< 2:
        print("他是婴儿")
    elif age >= 2 or age < 4:
        print("他学部")
    elif age >= 4 or age < 13:
        print("他是儿童")
    elif age >= 13 or age < 25:
        print("他是少年")
    elif age >= 25 or age < 50:
        print("他是请年")
    elif age >= 50 or age < 80:
        print("他是老年")
    elif age > 80:
        print("他是长寿老人")
    else:
        print("他已经去世")
age()
