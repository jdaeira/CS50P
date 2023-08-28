greeting = str(input("Greeting: ")).lower()

result = greeting.startswith("hello")
letter = greeting[0]

if result == True:
    print("$0")
elif greeting[0] == "h" and result == False:
    print("$20")
else:
    print("$100")

