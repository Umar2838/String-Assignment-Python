#  Question no 01

# input = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# count = 0
# for char in input:
#     if char in vowels:
#         count += 1
# print("Number of vowels:", count)

# Question no 02

# str = input("Enter a string: ")

# upperCount = 0;
# lowerCount = 0;
# numberCount = 0;
# whiteSpace = 0;

# for char in str:
#     if char.isupper():
#         upperCount += 1
#     elif char.islower():
#         lowerCount += 1
#     elif char.isnumeric():
#         numberCount += 1
#     elif char.isspace():
#         whiteSpace += 1

# print("Upper case characters: ", upperCount)
# print("Lower case characters: ", lowerCount)    
# print("Numbers: ", numberCount)
# print("White space: ", whiteSpace)

# Question no 03

# str2 = input("Enter a string: ")

# newString = str2[-1] + str2[1:-1] + str2[0]

# print("New string: ",newString)

# Question no 04

user_input = input("Enter a string: ")

reversed_string = user_input[::-1]

print("Original string:", user_input)
print("Reversed string:", reversed_string)
   
