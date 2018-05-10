def sum(x,y):
    c=x+y
    print(c)
all_sum+=c
def sum(x,y,*args,**kwargs):
    print(args)
    print(kwargs)
    for i in args:
    all_sum+=i
    for i in kwargs:
    all_sum+=i
t =(3,6,5,4)
d = {"date":7}
    





sum(x,y,*t,**d)

