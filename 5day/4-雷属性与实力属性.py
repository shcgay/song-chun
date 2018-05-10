class AAA():
	aaa = 10
s1 = AAA()
s2 = AAA()
s3 = AAA()
print(s1.aaa,s2.aaa,s3.aaa)
s1.aaa+=2
print(s1.aaa,s2.aaa,s3.aaa)
AAA.aaa+=3
print(s1.aaa,s2.aaa,s3.aaa)
s1.aaa+=3
print(s1.aaa,s2.aaa,s3.aaa)
AAA.aaa+=3
print(s1.aaa,s2.aaa,s3.aaa)






class Test():
	name = 'python'
a = Test()
Test.name = 'python good'
print(Test.name)
print(a.name)



class Test():
	name = 'python'
a = Test()
a.name = 'python good'
print(Test.name)
print(a.name)




class Test():
	name = 'python'
a = Test()
a.abc = 123
print(dir(Test))
print(dir(a))






class Test():
	name = 'scolia'
print(Test.__doc__)
print(Test.__module__)
