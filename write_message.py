filename = 'text_files/programming.txt'

#used the 'a' argument to append to the exisisting file.
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

