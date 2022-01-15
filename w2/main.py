# Original Code
# # 🚨 Don't change the code below 👇

# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# # Write your code below this line 👇
# first_number = two_digit_number[0]
# second_number = two_digit_number[1]
# first_int = int(first_number)
# second_int = int(second_number)
# print(first_int + second_int)

# Modified Code
# Find the product of a two digit number by multiplying the 2 numbers together
print("Find the product of a two digit number.")
two_digit = input("What is your two digit number?\n")
number_one = int(two_digit[0])
number_two = int(two_digit[1])
product = number_one * number_two
print(f"The product of {two_digit} is {product}.")

# The oringal code added the two numbers together
# the modification mainly cleans up the aboslute mess
# that was me converting strings to integers
# as well as it multiplying instead of adding