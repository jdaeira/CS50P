# Vertical Implementaion of bricks
# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()

# Horizontal Implementaion of bricks

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

# Print Multiple Blocks

def main():
    print_square(5)

def print_square(size):
    # For each row in a square
    for i in range(size):
        # For each brick in a row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()


main()

