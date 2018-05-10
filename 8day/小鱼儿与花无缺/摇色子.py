import random 
point = random.randint(1,7)
print(point)
def shaizi(numbers = 3,points = None):
	print('-----摇色子-----')
	if points is None:
		points = []
	while numbers > 0:
		point = random.randint(1,7)
		points.append(point)
		numbers = numbers - 1
	return points
def shaizi_result(total):
	isbig = 11 <= total <= 18
	issmall = 3 <= total <= 10
	if isbig:
		return '大'
	elif issmall:
		return '小'
def start_game():
	your_money = 1000
	while your_money > 0:
		print('-----游戏开始-----')
		choses = ['大','小']
		your_chose = input('请下注,大 or 小:')
		your_bet = input('下注金额:')
		if your_chose in choses:
			points = shaizi()
			total = sum(points)
			youwin = your_chose == shaizi_result(total)
			if youwin:
				print('色子点数:',points)
				print('恭喜,你赢了{} 元,你现在有 {} 元本金'.format(your_bet,your_money + int(your_bet)))
				your_money = your_money = int(your_bet)
			else:
				print('色子点数:',points)
				print('很遗憾,你输了{} 元,你现在有 {} 元本金'.format(your_bet,your_money - int(your_bet)))
				your_money = your_money - int(your_bet)
		else:
			print('格式有误,请重新输入')
	else:
		print('游戏结束')
start_game()
