def multiplication(first_number: int, second_number: int):
    """Function multiply first_number and second_number and return result
    :type first_number: int
    :type second_number: int
    """

    result = first_number * second_number
    return result


def print_multiplication_result():
    """Function print multiplication result"""

    f_number = int(input("\nEnter first number: "))
    s_number = int(input("Enter second number: "))
    mult_result = multiplication(f_number, s_number)
    print("\nMultiplication result: " + str(mult_result))


print_multiplication_result()
