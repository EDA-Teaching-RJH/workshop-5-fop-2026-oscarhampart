camel = input("Enter in camelCase: ")

snake = ""

for char in camel:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char 

print("Here it is in snake_case: ", snake)