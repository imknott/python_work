filename = 'text_files/guestbook.txt'

print("Welcome to the terminal, we ask that you please enter the following: \n")

while True:
    name = input("What is your name? ")
    with open(filename, 'a') as file_object:
        file_object.write(f'{name} \n')

    #Find out if someone else would like to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        break
        
