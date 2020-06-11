# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents + "\n")
#
# file_name = 'pi_digits.txt'
#
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())

file_name = 'pi_digits.txt'

# with open(file_name) as file_object:
#     lines = file_object.readlines()
#     # print(lines)
#     for line in lines:
#         print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

big_file_name = 'F:/Education/Python/No-Nonsense Python books/ehmatthes-pcc_2e-1.1-1-g9e7977b/chapter_10/pi_million_digits.txt'

big_pi_string = ''

with open(big_file_name) as big_file_object:
    big_lines = big_file_object.readlines()

for line in big_lines:
    big_pi_string += line.strip()

print(f"{big_pi_string[:52]}...")
print(len(big_pi_string))

birthday = input("\nEnter your birthday in format ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")