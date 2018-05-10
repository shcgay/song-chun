Language_option = """\
	Language: Choose the language for System[OPTION]
			-1							Choose English Language
			-2							Choose Chinese Language
		"""
enter_str = 'please enter an integer:'
en_game_start_str = 'You choose English language!,Now, Game Start !'
cn_game_start_str = '你选择中文模式! 现在,开始游戏!'


en_game_rule_str = 'you should enter a number that from 0 to 9,then the \nSystem will print the infromation of the number'
cn_game_rule_str = '你输入一个0-9的数字, 系统会打印出该数字的信息'
en_game_over_str = 'Game Over!'
cn_game_over_str = '游戏结束!'
print('language_option')
number = int(input(enter_str))
en_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
cn_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
FLAG = True
en_play_again_str = """\
###################################################
	Do you wnat play again?
	-1				Play Again
	-2  			Exit Game
			"""
cn_play_again_str = """\
##################################################
	你还要继续玩吗?
	-1  			继续玩
	-2  			退出游戏
			"""
number = int(input(enter_str))
def print_info(num):
	if num in range(0,9):
																																																													print(num,en_list[num],cn_list[num])
	else:
		print('Error')
def start_game(num):
	if num == 1:
		print(en_game_rule_str)
	elif num == 2:
		print(cn_game_rule_str)
	else:
		print(en_game_rule_str)
	n = int(input(enter_str))
	print_info(n)
def play_again(n):
	if n ==1:
		print(en_play_again_str)
	elif n == 2:
		print(cn_play_again_str)
	else:
		print(en_play_again_str)
	again = int(input(enter_str))
	if again == 1:
		pass
	elif again == 2:
		global FLAG
		FLAG = False
while True:
	if FLAG:
		if number == 1:
			print(en_game_start_str)
			start_game(1)
			play_again(1)

		elif number == 2:
			print(cn_game_start_str)
			start_game(2)
			play_again(2)
		else:
			print(en_game_start_str)
			start_game(number)
			play_again(number)

	else:
		print(en_game_over_str)
		break
