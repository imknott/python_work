responses = {}

#Set flag to indicate that polling is active. 
polling_active = True

while polling_active = True:
	#prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb one day? ")
#store the response in the dictionary
	responses[name] = response

	#Find out if someone else would like to take the poll.
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

#polling is complete show results 
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name.title()}, would like to climb {response.title()}")
