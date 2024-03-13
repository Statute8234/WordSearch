import random
rows = 15
colloms = 7
name = input('what would you like to name this word serch? ')
name = name.title()
number = int(input('how many words would you like to add to this word serch? '))
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
space = ''
for x in range(number):
	word_name = input('what word would you like to add to the word serch? ') + space
	word_name = word_name.upper()
	space = word_name
print(name.center(62))
for x in range(colloms):
	list = (word_name,abc)
	word_name2 = random.choice(list)
	letter = random.choice(word_name)
	for x in range(rows):
		letters = letter + ' ' + random.choice(word_name2)
		letter = letters
	print(" ")
	print(' ' +letters)