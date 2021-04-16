def print_models(unprinted_designs, completed_models):
#simulate printing each design, until there are none left.
#move each design to completed_models before printing
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}") 
		completed_models.append(current_design)

def show_completed_models(completed_models):
#display all completed models
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
