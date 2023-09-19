import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha():
        print(s[:2])
        if len(s) >= 2 and len(s) <= 6:            
            if s[2:].isnumeric():
                return False
            else:
                return True

main()