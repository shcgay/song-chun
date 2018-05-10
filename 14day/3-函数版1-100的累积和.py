def NUM(num):
    s=0
    i=1
    while i<=num:
        s=s+i
        i=i+1
    return s
s= NUM(200)
print("1~200的累积和为:%d"%s)
