#Instructions
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Example:
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    # split string and cast
    new_numbers = numbers.split(" ")
    #starting point
    highest = int(new_numbers[0])
    lowest = int(new_numbers[0])

    for n in new_numbers:
        if int(n) > highest:
            highest = int(n)
        if int(n) < lowest:
            lowest = int(n)

    return "{} {}".format(highest, lowest)

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
