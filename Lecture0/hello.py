# Ask user for their name
name = input("What's your name? ").strip().title()

# Split name at the space in between into first and last name
first, last = name.split(" ")

print(f"Hello , {first} {last}")

# Remove whitespace from string
name = name.strip()

# Capitalize the users first name
name = name.capitalize()

# Capitalizes the first and last name
name = name.title()

# Can also chain the commands
name = name.strip().title()

# Say hello to user
print("Hello, " + name)
# or
# the comma automatically adds a space

print("Hello,", name)

# or with "f" in the beginning
print(f"Hello, {name} format")

# if you use single quotes on the outside then you can use 
# double quotes on the inside
print('Hello, "friend"')
# or this way
print("Hello, \"friend\"")

