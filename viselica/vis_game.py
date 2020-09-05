# The game

import random
print('Игра виселица, версия 1.0')

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
_________
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
_________
""",
"""
 ------
 |    |
 |    O
 |    |
 |
 |
 |
 |
 |
_________
""",
"""
 ------
 |    |
 |    O
 |    |
 |  /-+-\\
 |
 |
 |
 |
_________
""",
"""
 ------
 |    |
 |    O
 |    |
 |  /-+-\\
 | |  |  |
 |
 |
 |
_________
""",
"""
 ------
 |    |
 |    O
 |    |
 |  /-+-\\
 | |  |  |
 |    |
 |
 |
_________
""",
"""
 ------
 |    |
 |    O
 |    |
 |  /-+-\\
 | |  |  |
 |    |
 |   |
 |   |
_________
""",
"""
 ------
 |    |
 |    O
 |    |
 |  /-+-\\
 | |  |  |
 |    |
 |   | |
 |   | |
_________
""")

MAo_WRONG = len(HANGMAN) - 1

WORDS = ('python', 'hello', 'dima') # кортеж слов
secret = random.choice(WORDS) # рандомное слово
used = [] # буквы которые уже были предложены
user_word = "-" * len(secret)

fail = 0
while fail <= MAo_WRONG and user_word != secret:
	result = input('Введите букву: ')
	while result in used:
		print("Вы уже предлагали букву: ", result)
		result = input('\nВведите букву: ')
	used.append(result)
	print("Использованные буквы: ", used)
	if result in secret:
		print('вы отгадали, буква ', result, 'есть в слове!')
		new = ""
		for i in range(len(secret)):
			if result == secret[i]:
				new += result
			else:
				new += user_word[i]
		user_word = new
	else:
		print('Ошибка, такой буквы нет!\n', HANGMAN[fail])
		fail += 1
	if result == '0':
		break
	print("\nОтгаданное слово: ", user_word)
if user_word == secret:
	print("""
_____________________________________________________________________________
_____________________________________________________________________________
___oo___o__ooooooo__oo____o__________oo________oo___oo___oo______oo_____oo___
___oo___o__oo____o__oo____o__________oo________oo___oo___ooo_____oo_____oo___
___oo___o__oo____o__oo____o__________oo___o____oo___oo___oo_o____oo_____oo___
____oo_o___oo____o__oo____o__________oo___o____oo___oo___oo__o___oo_____oo___
_____oo____oo____o__oo____o__________oo___o____oo___oo___oo___o__oo_____oo___
_____oo____oo____o__oo____o__________oo__o_o___oo___oo___oo____o_oo_____oo___
_____oo____oo____o___oo__o___________oo_o___o_oo____oo___oo_____ooo__________
_____oo____ooooooo____ooo_____________oo_____oo_____oo___oo______oo_____oo___
_____________________________________________________________________________
_____________________________________________________________________________
""")
	print("\n\nВы выиграли!")
else:
	print("Вы проиграли")
	print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                                                           +
+   ooooooo   oooo   oo       o oooooo     ooooooo oo     o oooooo ooooo    +
+   oo    o  oo   o  ooo     oo oo         oo    o oo     o oo     oo   o   +
+   oo    o oo     o oo o   o o oo         oo    o oo     o oo     oo   o   +
+   oo      oo     o oo  o o  o oo         oo    o oo     o oo     oooooo   +
+   oo  ooo oo     o oo   o   o oooooo     oo    o oo     o oooooo oooo     +
+   oo  ooo oooooooo oo       o oo         oo    o oo     o oo     oo  o    +
+   oo    o oo     o oo       o oo         oo    o  oo   o  oo     oo   o   +
+   ooooooo oo     o oo       o oooooo     ooooooo    ooo   oooooo oo   o   +
+                                                                           +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
print('Игра окончена')
