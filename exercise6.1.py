# 6.1 You decide to get some exercise and fresh air, but you want to keep track of how far from home you are.

# Ask the user for input on what action to take - walk or run. If they walk, the total distance should go up by one, and you should update the user on their total distance traveled as follows:

# "Distance from home is 6 km."

# If they run, their total distance should go up by 5. Your program should keep asking for input - you don't know where you're going until you get there! Each time, you should print the total distance traveled.

# Allow the user to go home when they are done exercising. The program should stop asking for input if the user enters 'go home'.

# See if you can also make the program tell the user when they have entered a command that does not exist.

counter = 0

while counter >= 0:
    action = input('Do you want to walk, run or go home? ')
    if action == 'walk':
        counter += 1
    elif action == 'run':
        counter += 5
    elif action == 'go home':
        counter += 0
        print('You are now {}km away from home.'.format(counter))
        break
    else:
        print('Do you want to walk, run or go home? ')

    print('Distance from home is {}km.'.format(counter))
