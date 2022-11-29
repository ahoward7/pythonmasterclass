name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday, {0}!".format(name))
else:
    print("I'm sorry, {0}, but you are not eligible for this holiday.".format(name))