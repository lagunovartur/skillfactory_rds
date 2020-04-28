import numpy as np


def game_core_v1(number):

    """ Функция угадывает число (number) в заданном интервале и возвращает число попыток, за которое удалось это сделать.
        Параметры:
            number - int/float - угадываемое число
        Возвращаемое значение:
            count - int - число попыток поиска
        Переменные функции:
            top - int - верхняя граница поиска
            bottom - int - нижняя граница поиска
    """

    count = 0
    top = 101
    bottom = 1

    while True:

        count += 1
        predict = np.random.randint(bottom, top)  # предполагаемое число

        if number == predict:
            return count  # выход из цикла, если угадали
        elif number < predict:
            top = predict
        elif number > predict:
            bottom = predict


def score_game(game_core):
    """Функция тестирует игру (game_core) и возвращает среднее число попыток за которое удалось угадать неизвестное.
        Параметры:
            game_core - function -  функция исполняющая игру
        Возвращаемое значение:
            score - int - среднее число попыток, за которое удалось угадать случаное число
    """
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


score_game(game_core_v1)
