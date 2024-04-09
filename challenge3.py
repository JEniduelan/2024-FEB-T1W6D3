# palindrome

# string reversed is also the same as the original string

# firetruck = kcurterif -> not a palindrome
# racecar = racecar -> palindrome

original_string = "racecar"

reversed_string = ""

for character in original_string:
    reversed_string = character + reversed_string

print(reversed_string)

if (reversed_string == original_string):
    print("A palindrome")
else:
    print("Not a palindrome")