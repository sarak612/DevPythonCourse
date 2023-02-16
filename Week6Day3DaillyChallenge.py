# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

# number = int(input("Enter a number: "))
# length = int(input("Enter a length: "))
# print("The multiples are: ")
# for i in range(length):
#     print(number*(i+1), end =" ")

# Challenge 2
# Write a program that asks a string to the user, and display a new string with
# any duplicate consecutive letters removed.
def remove_consec_letter_duplicates(word):
    result_word = ""
    prev_char = ""
    for char in word:
        if len(result_word) == 0:
            result_word += char
            prev_char = char
        if char == prev_char:  # it's redundant you can male it one if statment
            continue
        else:
            result_word += char
            prev_char = char
    return result_word

word = input("Enter a word")
print(word)
word = remove_consec_letter_duplicates(word)
print(word)
