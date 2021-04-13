alien_0 = {'color': 'green', 'points': 5, 'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x-position']}")

#move the alien to the right
#Determine how far to move the alien based on its current speed. 
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#this must be a fast alien
	x_increment = 3


#The new position is the old position plus the increment
alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New position: {alien_0['x-position']}")

