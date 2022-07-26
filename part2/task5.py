# Задание 5
# Исходные данные

def func1():
    result = {(1, 1): 1000, (1, 2): 2000, (1, 3): 3000}
    return result


def func2():
    result = {}
    result[(1, 1)] = 1000
    result[(1, 2)] = 2000
    result[(1, 3)] = 3000
    return result


def func3():
    result = {(1, i): i * 1000 for i in range(3)}
    return result

# Задание: необходимо выяснить какая из функций будет выполняться быстрее при выполнении 100000 раз
