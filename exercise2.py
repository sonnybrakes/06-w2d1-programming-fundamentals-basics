# 1. How would you calculate a good tip for a 55 dollar meal?
# Use print to print the answer.

# 1. tip calulator
print('meal tip calulators')
cost = float(input('cost meal  $'))
tip = float(input('tip        %'))
tip_percent = float(tip/100)

print('meal       ${}'.format(cost))
tip_on_meal = cost * tip_percent
print('tip        ${}'.format(tip_on_meal))
print('total bill ${}'.format(cost + tip_on_meal))

# 2. Try adding a string and an integer with the + operator.
# What happens?
# Find a way to convert the integer into a string
# first and use print to print the result.

# 2. Answer: A string cannot be concatinated to an integer unless the integer is first turned into a string.

string = 'string'
number = 10000000
string_plus_number = string + ' ' +str(number)
print(string_plus_number)

# 3. Try outputting the result of 45628 multiplied by 7839 in a sentence by using string interpolation.

# 3. Answer
num1 = int(45628)
num2 = int(7839)
print(num1 * num2)
print('45628 times 7839 equals {}'.format(45628 * 7839))

# 4. What's the value of the expression (10 < 20 and 30 < 20) or not(10 == 11)? Try figuring it out on your own before typing it in.

# 4. Answer
print((10 < 20 and 30 < 20) or not(10 == 11))

# 4. The answer will be true.
