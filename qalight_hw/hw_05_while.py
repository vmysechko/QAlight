def number_comparison():

    """ Пользователь вводит два целых числа, для дальнейшего сравнения с помощью цикла while """

    a = int(input("Введите сравниваемое целое число А: "))
    b = int(input("Введите сравниваемо целое число Б: "))
    c = int(input("Введите добавочное целое число В: "))

    while a <= b:
        a = a + c
        if a < b:
            print("Значение А: " + str(a) + " - Пока что нет")
        elif a > b:
            print("Дождались!" + " Финальный А: " + str(a))


number_comparison()