user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
}

#A for loop that will display all the information within the user's dictionary
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

#new dictionary that holds the favorite languages of users
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'enrico': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

#For loop that loops through the favorite language dictionary to display each users favorite programming language. 
for name, languages in favorite_languages.items():
	if len(languages) == 2:
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")
	else:
		print(f"\n{name.title()}'s favorite language is:")
		for language in languages:
			print(f"\t{language.title()}")




