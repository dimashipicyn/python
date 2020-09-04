print('Игра виселица, версия 1.0')

secret = 'python'
while True:
	result = input('Введите букву: ')
	if not result in secret:
		print('нет такой буквы')
	else:
		print('вы отгадали')
	if result == '0':
		break
print('игра окончена')
