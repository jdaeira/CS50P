def convert(h, m):
    min = float(m) / 60
    return float(h) + min


def main():
    time = input("What time is it? ")

    hours, minutes = time.split(":")

    new_time = convert(hours, minutes)
   
    if new_time >= 7 and new_time <= 8:
        print("breakfast time")
    elif new_time >= 12 and new_time <= 13:
        print("lunch time") 
    elif new_time >= 18 and new_time <= 19:
        print("dinner time")

main()