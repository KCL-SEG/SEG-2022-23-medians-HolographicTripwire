"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# Return the median of a list of numbers
def median(list):
    # Sort the list
    list.sort();
    # Find the list's middle
    mid_index = int((len(list)-1)/2)

    # Return the median
    # If there are no elements, return None
    if(len(list) == 0):
        return None
    # If there are an even number of elements, take the average of the middle two
    elif((len(list) % 2) == 0):
        return (list[mid_index] + list[mid_index + 1])/2
    # If there are an odd number of elements, return the middleone
    else:
        return list[mid_index]

# Ask the user for a list of comma-separated numbers and return it
def receive_comma_separated_number_list():
    # Repeat until the user enters a valid list
    while True:
        # Ask the user for a list of numbers
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
        # Tell the user if they messed up, and retry
        except ValueError:
            print("Some input could not be converted to a number!")
        # If the user entered a valid list, exit the loop
        else:
            break
    # Return the list of numberes that the user entered
    return numbers;

# Run the program once
def bootstrap():
    numbers = receive_comma_separated_number_list()
    print(median(numbers))

bootstrap()