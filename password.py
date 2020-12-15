import random

password = ''
length = int(input("Enter length of password: "))

# the loop that generates the password
for i in range(length):

	# a selection variable that decides the type of character appended
	selection = random.randint(0,2)

	# appending uppercase and lowercase characters
	if selection == 0:
		character = random.randint(97, 122)
		flip = random.randint(0,1)
		if flip:
			character-=32
		password+=chr(character)

	# appending numbers
	elif selection == 1:
		character = random.randint(48, 57)
		password+=chr(character)

	# appending special characters
	else:
		character = random.randint(35,38)
		atTest = random.randint(0, 4)
		if atTest == 1:
			password+=chr(64)
		password+=chr(character)

print("The Generated Password is:", password)