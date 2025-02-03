def pattern_a():
    for i in range(1, 6):  # 5 rows
        for j in range(1, 6 - i):  # Leading spaces
            print(" ", end="")
        for j in range(1, i + 1):  # Numbers in the row
            print(j, end="")
        print()  # Move to the next line

# Call the function to display pattern a
pattern_a()