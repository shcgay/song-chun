list = [{"北京":{"面积":"1000","人口":"200"},"上海":{"面积":"600","人口":"150"}}]
for i in list:
    for k,v in i.items():
        for l,n in v.items():
            print(k,l,n)
