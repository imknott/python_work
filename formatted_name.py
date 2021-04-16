def get_formated_name(first_name, last_name, middle_name=''):
	'''return a full name, neatly formatted'''
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

while True: 
	print("Please enter your favorite musician")
	print('\n(Enter "q" at any time to quit)')

	f_name = input("First name: ")
	if f_name == 'q':
		break
	m_name = input("Middle name: ")
	if m_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

musician = get_formated_name(f_name, l_name, m_name)
print(f"{musician} is a fantastic musician")
