def pattern_b():
    i = 1
    while i <= 7:  # Loop until i reaches 7
        j = 1
        while j <= i:  # Repeat `i` number of times
            print(i, end="")  # Print the current value of i
            j += 1
        print()  # Move to the next line
        i += 2  # Increment i by 2 for the next row

# Call the function to display pattern b
pattern_b()