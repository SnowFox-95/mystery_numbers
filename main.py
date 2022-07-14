from random import *
import func

mystery = randint(1, 100)
print('Добро пожаловать в числовую угадайку')
while True:
    numb = input('Введите число от 1 до 100:')
    if func.is_valid(numb):
        print(func.comparison(mystery, numb))
        print('Хотите сыграем еще раз?')
        print('д - Да, н - Нет')
        if input().lower() not in ['д', 'да', 'da', 'd', 'y', 'yes']:
            print('Спасибо за игру в угадайку чисел. Увидимся...')
            break
    else:
        print('А может все-таки впишем число от 1 до 100?')
