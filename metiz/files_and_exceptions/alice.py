filename = 'text_files/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' is not found.")
else:
    words = content.split()
    num_words = len(words)
    print(f"Amount of words in '{filename}' is: " + str(num_words))

