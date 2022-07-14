def is_valid(n):
    return (n.isdigit() and int(n) in range(1, 101))


def comparison(m, n):
    while m != n:
        if is_valid(n):
            n = int(n)
            if n < m:
                print('Ваше число меньше загаданного, попробуйте еще раз')
                n = input()
            elif n > m:
                print('Ваше число больше чем загадано. Лучше попробовать еще раз')
                n = input()
            else:
                print('Может быть все-таки число от 1 до 100?')
                n = input()

    return 'Вы угадали, поздравляем!'