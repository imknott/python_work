prompt = "if you tell us who you are we can personalize your experience. "
prompt += '\nWhat is your first name? '

name = input(prompt)


age = input('\nHow old are you? ')
print(f'\nHello, {name}. You are {age} years old')

age = int(age)
if age >= 18:
	print('Wow, how does it feel to be old?')
else:
	print("You are probably too young to use this app.")

prompt_2 = f"\n{name}, I have a pet parrot and if you say anything to her she will repeat it back"
prompt_2 += "\n(Enter 'quit' to shut her up.)"


while True:
	mesaage = input(prompt_2)

	
	if mesaage == 'quit':
		break
	else:
		print(mesaage)

#Create a function that says hello to a specified user. 
def greet_user(username):
	#display a simple greeting.
	print(f"Hello, {username.title()}!")

greet_user('Ian')


