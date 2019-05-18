# if statement exercises 06-w2d1-programming-fundamentals-basics
# 1. Ask the user to enter a number. Use an if statement to print "that's a big number!" if the number is 100 or more, or "why not dream a little bigger?" otherwise.

num = int(input('Enter a number: '))
if num >= 100:
    print('That\'s a big number!')
else:
    print('Why not dream a little bigger?')

# 2. Ask the user to enter their age, and then display a message telling them how many years apart in age you are from them. If they enter a number larger than 105, print "I'm not sure I believe you".

user_age = int(input('Enter your age: '))
if int(user_age) < 105:
    print('Our ages differ by {} years'.format(abs(55 - (user_age))))
else:
    print('I\'m not sure I believe you')

# 3. Save your name as a string into a variable, then ask the user to enter their name. If the two names match, print "We have the same name!".

my_name = 'Mitch'
user_name = input('what is your name? ')
if my_name == user_name:
    print('We have the same name!')

# 4. Pick a number and save it in a variable called secret_number. Ask the user to enter a number. If they enter the secret number, print "You win!". If they are off by 1, print "So close!". Otherwise, print "Try again".

secret_number = 7
user_number = int(input('Enter a number: '))
if (user_number) == secret_number:
    print('You win!')
elif abs((user_number - secret_number) == 1):
    print('So close!')
else:
    print('Try again')
