# Print out the correct emoji depending on the inputted message

def main():
    hello = input("Input the emotion: ")
    hello = convert(hello)
    print(hello)

def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message

main()