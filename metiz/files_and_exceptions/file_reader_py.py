temp_text = ''
temp_text_list = []

with open("learning_python.txt") as python_object:
    temp_text = python_object.read()

# print(temp_text + "\n")

# with open("learning_python.txt") as python_object:
#     for line in python_object:
#         print(line.strip())

with open("learning_python.txt") as python_object:
    temp_text_list = python_object.readlines()
    for line in temp_text_list:
        print(line.strip())

print(temp_text_list)

temp_text_01 = ''

with open("learning_python.txt") as text_file:
    for lines in text_file:
        temp_text_01 += lines

print(temp_text_01 + "\n")

temp_text_01_replaced = temp_text_01.replace("Python", "Java")

print(temp_text_01_replaced + "\n")
