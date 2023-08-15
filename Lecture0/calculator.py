# Convert strings into floats to be able to add integers
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

z = round(x+y)

# The z:, formats the number to put commas in the proper place
print(f"{z:,}")

# division

z = round(x / y, 2)

print(z)

# or also by formatting
print(f"{z:.2f}")


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()