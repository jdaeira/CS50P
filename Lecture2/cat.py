i = 0
while i < 3:
    print("meow")
    i += 1

for _ in range(3):
    print("meow")


print("meow\n" * 3,  end="")

while True:
    n = int(input("What's n? "))

    if n > 0:
        break

for _ in range(n):
    print("meow")
        

