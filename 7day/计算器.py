cass jsq(object):
	def Call(self,x,y):
		return 0
class jia(jsq):
	def Call(self,x,y):
		return x+y

class jian(jsq):
	def Call(self,x,y):
		return x-y

class cheng(jsq):
	def Call(self,x,y):
		return x*y

class chu(jsq):
	def Call(self,x,y):
		if y != 0:
			return x/y

class Factury():
	@staticmethod
	def createMath(operate):
		math_dict = {r'+':jia,r'-':jian,r'*':cheng,r'/':chu}
		math_object = jsq()
		if operate in math_dict:
			math_object = math_dict[opreate]()
		return math_object

def Call(operate,x,y):
	call_object = Factury.createMath(opreate)
	return call_object.Call(x,y)

if __name__ == "__main__":
	while True:
		opreate = input("请输入操作方法+-*/中的一个")
		number1 = input("请输入参数")
		number2 = input("请输入参数")
		print(Call(opreate,int(number1),int(number2)))
