camel = input("camelCase: ")

for c in camel:
    if c.isupper():
        position = camel.index(c)
        camel = camel[:position] + "_" + camel[position:]

print("snake_case:", camel.lower())