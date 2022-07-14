def is_valid(n):
    return (n.isdigit() and int(n) in range(1, 101))


def comparison(m, n):
    tryes = 0
    while m != n:
        if is_valid(n):
            n = int(n)
            if n < m:
                print('Ваше число меньше загаданного, попробуйте еще раз')
                tryes += 1
                n = input()
            elif n > m:
                print('Ваше число больше чем загадано. Лучше попробовать еще раз')
                tryes += 1
                n = input()
            elif m == n:
                break
            else:
                print('Может быть все-таки число от 1 до 100?')
                tryes += 1
                n = input()

    return 'Вы угадали, поздравляем! Потребовалось всего ' + str(tryes) + ' попыток'
