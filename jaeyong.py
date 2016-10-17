"""

1. created by : Jae yong Park
2. created date : 10/12/2016

=======	=======	=======
player   com     result
=======	=======	=======
rock    scissor	player_win
rock    paper	com_win
scissor paper	player_win
scissor rock	com_win
paper	rock	player_win
paper	scissor	com_win
=======	=======	=======
"""


import random

# print when com wins
def com_win():
	print("컴퓨터가 이겼습니다.")

# print when player wins
def pl_win():
	print("플레이어가 이겼습니다.")

# print when game draws
def draw():
	print("비겼습니다.")

# decide who wins
def manage(p_choice,c_choice):
	print(p_choice,c_choice)

	if (p_choice == c_choice):
		draw()
		
	elif (p_choice == 1) and (c_choice == 2):
		com_win()
	
	elif (p_choice == 1) and (c_choice == 3):
		pl_win()
		
	elif (p_choice == 2) and (c_choice == 1):
		pl_win()
		
	elif (p_choice == 2) and (c_choice == 3):
		com_win()
	
	elif (p_choice == 3) and (c_choice == 1):
		com_win()
	
	elif (p_choice == 3) and (c_choice == 2):
		pl_win()

# when game starts
def main():
	count = 0
	while (count != 10):
		player_choice = int(input("가위,바위,보를 입력하세요.(가위:1,바위:2,보:3) :"))
		com_choice = random.randint(1,3)
		manage(player_choice,com_choice)
	

		count +=1

	print("게임이 끝났습니다.")

main()
