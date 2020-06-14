def dict_concate(dict_01: dict, dict_02: dict, dict_03: dict):
    """ Function gather the information from 'dict_01', 'dict_02' and
     'dict_03' into one dictionary
     :type dict_01: dict
     :type dict_02: dict
     :type dict_03: dict"""

    result = {}

    for key_01, value_01 in dict_01.items():
        result[key_01] = value_01

    for key_02, value_02 in dict_02.items():
        result[key_02] = value_02

    for key_03, value_03 in dict_03.items():
        result[key_03] = value_03

    return result


food = {'snack': 'chips', 'meet': 'shashluk', 'vegetables': 'tomatoes'}
drinks = {'alcohol': 'beer', 'non-alcohol': 'orange_juice'}
dessert = {'cake': 'Napoleon', 'candies': 'Barbariski'}

party = dict_concate(food, drinks, dessert)
print(party)
