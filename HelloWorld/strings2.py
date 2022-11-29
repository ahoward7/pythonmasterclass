numbers = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators = separators + char

values = "".join(char if char not in separators else " " for char in numbers).split()
print(sum([int(val) for val in values]))