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
 |    |
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
 |    |
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
 |    |
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
 |    |
 |    |
 |   | |
 |   | |
_________
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ('python', 'hello', 'dima') # кортеж слов
secret = random.choice(WORDS) # рандомное слово
used = [] # буквы которые уже были предложены
user_word = "-" * len(secret)

fail = 0
while fail <= MAX_WRONG:
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
		print("GAME OVER")
		break
	print("Отгаданное слово: ", user_word)
	if user_word == secret:
		print("Вы победили!")
		break
print('игра окончена')
