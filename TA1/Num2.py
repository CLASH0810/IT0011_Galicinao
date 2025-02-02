def sum_of_digits(input_string):
    total_sum = 0
    
    for char in input_string:
        if char.isdigit():  # Check if the character is a digit
            total_sum += int(char)  # Add the digit to the sum
    
    print("Sum of digits:", total_sum)

# Example usage:
input_string = input("Enter a string: ")
sum_of_digits(input_string)