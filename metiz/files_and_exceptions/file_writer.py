filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")

# 'w' argument tells Python that we want to open a file in write mode.
#  In the write mode Python will erase the content of the file.
# 'r' - read mode
# 'a' - append mode
# 'r+' - read/write mode

with open(filename, 'a') as file_object:
    file_object.write("That should be the only stroke in the file.\n")
    file_object.write("I also love finding meaning in large data-sets. \n")
    file_object.write("I also love creating apps that can run in a browser. \n")

guest_name = input("Write your name, please: ")

with open(filename, 'a') as file_object:
    file_object.write(guest_name + "\n")

