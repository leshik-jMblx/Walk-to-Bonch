# Программа для поиска корней квадратного уравнения

# Импорт функции корня
from math import sqrt
# Инструкции для пользователя
print('\nSample: ax*x ± bx ± c = 0\nSpaces are important!')
print('To exit press "q" then "enter"')
# Инициализация переменных
a, b = '', ''

# Бесконечный цикл для повторного ввода
while True:
	s = input('\n').split()
	
	if s[0] == 'q': break

# Проверка корректности ввода пользователя
	try:
		
		if (s[1]!='-' and s[1]!='+') or (s[3]!='-' and s[3]!='+') \
		or len(s) != 7 or s[5] !='=' or s[6]!='0' or 'x*x' not in s[0] \
		or 'x' not in s[2] or float(s[4])!=float(s[4]):
			 
			print('Wrong input!')
			continue
			
	except (ValueError, IndexError):
		print('Wrong input!')
		continue

# Замена знака у аргумента 'b'
	if s[1] == '+':
		s[1] = '-'
		operation = '+'
	else:
		s[1] = '+'
		operation = '-'


# Выявление числовых значений аргументов 'a' и 'b'
	for i in s[0]:
		if i != 'x': a += i
		else: break
	for i in s[2]:
		if i != 'x': b += i
		else: break

# Если значения отстутствуют, они равны единице		
	if a == '': a = '1'
	elif a == '-': a = '-1'
	
	if b == '': b = '1'
	elif b == '-': b = '-1'

# Поиск корней по формуле	
	try:	
	
		x1=(float(s[1]+b)+sqrt(float(b)**2-4*float(a)*\
		float(s[3]+s[4])))/(2*float(a))
		x2=(float(s[1]+b)-sqrt(float(b)**2-4*float(a)*\
		float(s[3]+s[4])))/(2*float(a))
		
# Вывод		
		print('\nx1 =', x1)
		print('x2 =', x2)
		print('Top of a parabola =', float(s[1]+b)/(2*float(a)))
		print("Derivative's equation: {aarg}x {operation} {barg}" \
		.format(aarg = float(a)*2, operation = operation, barg = b))
		
	except ValueError:
		print("Empty set")

# Сброс значений переменных для повторного ввода
	a,b = '',''	
	continue
