"To get the ASCII code of a character, use the ord() function
ord('a');

"To get the character encoded by an ASCII code number, use the chr() function
chr(95)


"""Method-1"""
"""character to ASCII values"""
str1=eval(input("Enter any character: "));
print(ord(str1));

""" ASCII values to Character"""
str1=eval(input("Enter any ASCII: "));
print(chr(str1));

"""Method-2"""
print(ord(eval(input("enter character: ")))); # character to no
print(chr(eval(input("Entet number: "))));    # no to character


