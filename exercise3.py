#3. Let's make a Python program that greets someone by name.

name = input('What is your name? ')
print('Hello, {}.'.format(name))

#3. Use a Boolean function to check if the guess is True or False.

secret_password = 'please'
password_attempt = input('Guess the password? ')
correct_or_not = (password_attempt == secret_password)
print('That\'s {}!'.format(correct_or_not))

#3. Let's try asking the user how old they are and have the program output what year they were born in.

how_old_are_you = int(input('How old are you? '))
print('You were born in {}.'.format(2019 - how_old_are_you))
