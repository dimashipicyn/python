# Крестики нолики

import random

# Глобальные константы
X = 'X'
O = 'O'
EMPTY = ' '
NUM_SQUARES = 9
TIE = 'Ничья'

def greeting():
# Приветствие пользователя и правила игры
	print('\n\t\t\tTic tac toe game. Version 1.0\n\n')
	print("""
Добро пожаловать на ринг одного из грандиознейших состязаний всех времен!\n
Твой мозг и мой процессор сойдутся в схватке за доской игры в Крестики-Нолики!
Чтобы сделать ход введи число от 0 до 8.
Числа соответствуют полям как показано ниже:""")
	print("""
	0 | 1 | 2
	---------
	3 | 4 | 5
	---------
	6 | 7 | 8""")
	print("Приготовься к бою жалкий белковый человечишка!")

def first_turn():
# Возвращает первый ход человека или компуктера
	turn = None
	while turn not in ('y', 'n'):
		turn = input("Хочешь оставить за собой первый ход? <y/n>:")
	if turn == "y":
		print("\nНу что ж, играй крестиками!")
		human = X
		computer = O
	else:
		print("\nИграешь ноликами, мой первый ход!")
		human = O
		computer = X
	return computer, human

def board_create():
# Создает новую доску
	board = []
	for i in range(NUM_SQUARES):
		board.append(EMPTY)
	return board

def board_print(board):
	print(board[0], '|', board[1], '|', board[2])
	print('---------')
	print(board[3], '|', board[4], '|', board[5])
	print('---------')
	print(board[6], '|', board[7], '|', board[8])
	print("\n\n")

def ask_number(question, low, high):
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

def legal_moves(board):
	moves = []
	for i in range(NUM_SQUARES):
		if board[i] == EMPTY:
			moves.append(i)
	return moves

def winner(board):
	TO_WIN = ((0, 1, 2),
			  (3, 4, 5),
			  (6, 7, 8),
			  (0, 3, 6),
			  (1, 4, 7),
			  (2, 5, 8),
			  (0, 4, 8),
			  (2, 4, 6))
	for row in TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
	if EMPTY not in board:
		return TIE
	return None

def human_move(board, human):
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Твой ход, выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
		if move not in legal:
			print("Это поле уже занято!")
	print("Ладно.. .")
	return move

def computer_move(board, computer, human):
	board = board[:]
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	legal = legal_moves(board)
	for move in legal:
		board[move] = computer
		if computer == winner(board):
			return move
		else:
			board[move] = EMPTY
	for move in legal:
		board[move] = human
		if human == winner(board):
			return move
		else:
			board[move] = EMPTY
	for move in BEST_MOVES:
		if move in legal:
			return move

def next_turn(turn):
	if turn == X:
		return O
	return X

def congrat_winner(the_winner, computer, human):
	if the_winner != TIE:
		print("Три", the_winner, "в ряд!")
	else:
		print("Ничья!")
	if the_winner == computer:
		print("Как я и предсказывал, победа осталась за мной!")
	elif the_winner == human:
		print("О нет!, этого не может быть, ты победил!")

def main():
	greeting()
	computer, human = first_turn()
	turn = X
	board = board_create()
	board_print(board)
	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
			print("Human:")
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
			print("Computer:")
		board_print(board)
		turn = next_turn(turn)
	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)

main()
