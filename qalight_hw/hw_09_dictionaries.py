def max_dict_values(dictionary: dict, amount_of_values: int):
    """Function look for three biggest values and and print corresponding key-value pairs
    :type dictionary: dict
    :type amount_of_values: int"""

    result_dictionary = {}
    values_list = []

    values_list = dictionary.values()
    sorted_list = sorted(values_list, reverse=True)
    result_list = sorted_list[0:amount_of_values]

    for key, value in dictionary.items():
        for i in range(len(result_list)):
            if result_list[i] == dictionary[key]:
                result_dictionary[key] = value

    print(str(amount_of_values) + " keys with a biggest values are: " + str(result_dictionary.keys()))


my_dict = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}

max_dict_values(my_dict, 3)


