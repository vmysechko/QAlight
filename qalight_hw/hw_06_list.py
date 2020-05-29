import random


def list_creation(max_value: int, list_size: int):
    """ Функция строит список длины list_size с максимальным значение max_value.
    Список заполняется произвольными целыми числами от 0 до max_value.
    :type max_value: int
    :type list_size: int
    """

    new_list = []

    for i in range(0, list_size, 1):
        new_list.append(random.randint(0, max_value))

    print(new_list)


list_creation(10, 5)
