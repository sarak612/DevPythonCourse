
# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.

# Add two new numbers to the set.
# my_fav_numbers = {2,4,6,8}
# my_fav_numbers.add(1)
# my_fav_numbers.add(3)

# my_fav_numbers.remove(8)
# print(my_fav_numbers)
# # Remove the last number.
# # Create a set called friend_fav_numbers with your friend’s favorites numbers.
# #Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# friend_fav_numbers = {1,3,5,7,9}
# print(friend_fav_numbers)
# my_fav_numbers.update(friend_fav_numbers)
# print(my_fav_numbers)
# our_fav_numbers = my_fav_numbers
# print(our_fav_numbers)
# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers
# to the tuple? Not able to change tuples in anyway.
# tuple = (1,2,3)
# 🌟 Exercise 3: List
# Instructions
# # Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)
# basket.remove("Banana")
# basket.remove("Apples")
# basket.append("Kiwi")
# basket.insert(0, "Apples")

# print(basket)
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float? a float is a number with deimal places. An integer is a whole number
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# (don’t hard-code the sequence).

# seq = {1.5,2,2.5,3,3.5,4,4.5,5}
# print(seq)
# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# for i in range(1, 20 + 1):
#     print(i)

# Using a for loop, that loops from 1 to 20(inclusive),
# print out every element which has an even index.
# Python program to print Even Numbers in given range

# start, end = 1, 20
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         print(num, end=" ")
# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name,
# unless the input is equal to your name.
# my_name = "Sara"
# user_input = input("What is your name?")
# while user_input != my_name:
#     user_input = input("What is your name?")
# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits
# with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list,
# print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print,
# “You chose a new fruit. I hope you enjoy”.
# user_input = input("What are 3 of  your favorite fruits? Please list a space in between each fruit")
# print(user_input)
# user_list = user_input.split()
# print(user_list)
# new_user_input = input("Pick a fruit")
# result = user_list.count(new_user_input)
#
# if result >= 0:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy.")
# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings,
# when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add
# that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie
# and what the total price is (10 + 2.5 for each topping).
# pizza_cost = 10
# topping_cost = 2.50

# toppings = []
# user_topping = ("What topping would you like on your pizza?")
# user_topping += ("Enter 'quit' when you are finished: ")
#
# while True:
#     topping = input(user_topping)
#     if topping != 'quit':
#         print("  I'll add " + topping + " to your pizza.")
#     else:
#         break
# toppings.append(user_topping)
# for choice in toppings:
#     print(choice)
# print(f"Your total price is {10 + (len(toppings) * 2.50)}")

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.

# ticket_age = input("How old are you?")
#age = ticket_age
#age = int(age)
# while True:
#
#     if age < 3:
#         print("  You get in free!")
#         return
#     elif age < 13:
#         print("  Your ticket is $10.")
#         return
#     else:
#         print("  Your ticket is $15.")
#         return
# family_ages = []
# age = int(input("How old are you?(q to quit)"))
#
#
# if age < 3:
#         print("  You get in free!")
#         print(f"Your age is {age}")
# elif age < 13:
#         print("  Your ticket is $10.")
#         print(f"Your age is {age}")
# else:
#         print("  Your ticket is $15.")
#         print(f"Your age is {age}")
# while True:
#     if age < 3:
#         print("  You get in free!")
# print(f"Your age is {age}")
#     elif age < 13:
#          print("  Your ticket is $10.")
# print(f"Your age is {age}")
#     else:
#          print("  Your ticket is $15.")
# print(f"Your age is {age}")
#     if age == 'quit':
#         break


    # if age < 3:
    #     print("  You get in free!")
    #     break
    # elif age < 13:
    #     print("  Your ticket is $10.")
    #     break
    # else:
    #     print("  Your ticket is $15.")
    #     break
# Store the total cost of all the family’s tickets and print it out.
#
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


# Exercise 10 : Sandwich Orders
# Instructions
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

# print(sandwich_orders)
# while sandwich_orders:
#     new_sandwich = sandwich_orders.pop()
#     print(new_sandwich)
#     finished_sandwiches.append(new_sandwich)
#
# print(sandwich_orders)
# #
# for sandwich in finished_sandwiches:
#
#     print(f"I made your {sandwich}")
# print(finished_sandwiches)
# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’
# appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out
# of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

# sandwich_orders = ["Pastrami", "Tuna", "Avocado", "Pastrami","Egg", "Pastrami","Sabih", "Pastrami"]
# finished_sandwiches = []
#
# print(sandwich_orders)
# print("I'm sorry, we're all out of pastrami today.")
# while "Pastrami" in sandwich_orders:
#     sandwich_orders.remove("Pastrami")
# print(sandwich_orders)

D:\DesktopContent\DevPythonCourse\Week6Day3\Exercises1-11

