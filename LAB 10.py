# Lewis Muthomi
# 1250 01
# Lab 10
# 10/25/2022
# This program will let you create list of fruits and how many pounds
# there are of each and then display them back to you


# User greeting
print('Welcome to create a list using the program')

# Create and initialize variable for empty list
fruits = []
weights = []

# Program loop
runInput = True
while runInput == True:
    fruitInput = input('Please enter a type of fruit: ')
    if fruitInput == '':
        runInput = False
    else:
        weightInput = input('Please enter the weight of fruits in pounds: ')
        fruits.append(fruitInput)
        weights.append(weightInput)
    print()
    
# Display user input 
for listIndex in range(len(fruits)):
    print(format(fruits[listIndex], '<20'), format(weights[listIndex], '>10'), 
'lbs')
print()

# Exit Message
print('Have a nice day')

