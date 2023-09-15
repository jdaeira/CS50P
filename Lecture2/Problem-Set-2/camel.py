camel = input("camelCase: ")

for c in camel:
    if c.isupper():
        position = camel.index(c)
        print("yes")
        print(position)