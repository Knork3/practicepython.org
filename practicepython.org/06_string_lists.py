string = str(input("Please enter the String to test: "))
compare = string[::-1]

if compare == string:
    print("Congratulations! You found a palindrome!")
else:
    print("Nope. This is just a usual unspecial stupid word.")
