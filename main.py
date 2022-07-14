from random import *
import func

mystery = randint(1, 100)
print('Добро пожаловать в числовую угадайку')
while True:
    n = input('Введите число от 1 до 100:')
    b = func.is_valid(n)
    if func.is_valid(n):
        number = int(n)
        break
    else:
        print('А может все-таки впишем число от 1 до 100?')
