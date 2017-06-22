from random import randint

answer = str.lower(input('Would you like to flip a coin? Yes or No: '))
    

def coin_flip(answer):
	while answer == 'yes':
		try:
			number = int(input('How many times?'))
			
			while number > 0:
				flip = randint(0, 1)
				
				if flip == 0:
					print('Heads')
				else:
					print('Tails')
					
				number -= 1
				
			answer = str.lower(input('Would you like to flip a coin again?' \
			' Yes or No: '))
			
		except ValueError:
			print('Please enter an integer value.')
			
	if answer != 'yes':
		print('\nGoodbye')

coin_flip(answer)
	
