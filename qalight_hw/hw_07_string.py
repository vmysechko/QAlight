def symbol_count(symbol: str, phrase: str):
    """Фукнция считает сколько раз символ 'symbol' встречается в строке 'phrase'
    :type symbol: str
    :type phrase: str """

    count = 0

    for i in range(0, len(phrase), 1):
        if symbol == phrase[i]:
            count += 1

    print(f"Символ \n\"{symbol}\" "
          f"\nвстречается в строке "
          f"\n\"{phrase}\" "
          f"\n" + str(count) + " раз(а).")


symbol = 'у'
phrase = 'Денис даёт нам классные задачки, которые помогут нам найти лучшую работу'

symbol_count(symbol, phrase)

