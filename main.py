# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:
#
# Hello world
# Hello world
# Hello world
# Hello world

print("Hello world " * 4)
# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
print(99 ** 3 * 8)

# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3 false
# >>> 3 == 3  true
# >>> 3 == "3" false
# >>> "3" > 3 false
# >>> "Hello" == "hello" false
# 🌟 Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following:
# "I have a <computer_brand> computer".
computer_brand = "Asus"
print(f"I have a {computer_brand} computer")
# 🌟 Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself.
# The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code
name = "Sara"
age = 56
shoe_size = 38

info = (f"I am {name} and I am {age} years old. I wish my age was still equal to {shoe_size} which is my shoe size")

print(info)
# 🌟 Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.
a = 5
b = 2
if a > b:
    print("Hello World")
# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input("please enter a number between 1 and 10: "))

if (number % 2) == 0:
    print("Your number is even")
else: print("Your number is odd")
# 🌟 Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name,
# print out a funny message based on the outcome.

name = input("What is your name?")
if (name == 'Sara'):
    print("What a coincidence! That's my name")
else:
    print("That's an unusual name. I like it!")
# 🌟 Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

h_inch = int(input("What is your height in inches? "))
h_cm = round(h_inch * 2.54, 1)
if (h_cm > 145):
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")