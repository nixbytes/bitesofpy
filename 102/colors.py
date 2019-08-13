VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""

    while True:
        color = input("enter one of 3 prime colors \n: ")
        color = color.lower()
        if color in VALID_COLORS or color is "quit":
            print("bye")
            break
        else:
            print(f"{color} Not a valid color")
            continue
        pass

print_colors()
