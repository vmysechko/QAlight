def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file '{filename}' is not found.")
        pass
    else:
        words = content.split()
        num_words = len(words)

        if '/' in filename:
            slash_pos = filename.index('/') + 1
        print(f"Words in '{filename[slash_pos:]}' is: " + str(num_words))


# filename = 'text_files/alice.txt'
# count_words(filename)

filenames = ['text_files/alice.txt', 'text_files/little_women.txt', 'siddhartha.txt', 'text_files/moby_dick.txt']
for filename in filenames:
    count_words(filename)