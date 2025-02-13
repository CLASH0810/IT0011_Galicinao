def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_line(line, line_number):
    numbers = line.strip().split(',')
    numbers = [int(num.strip()) for num in numbers]
    total = sum(numbers)
    
    result = f"Line {line_number}: {', '.join(map(str, numbers))} (sum {total}) - "
    result += "Palindrome" if is_palindrome(total) else "Not a palindrome"
    return result

def save_data(input_data, input_file):
    with open(input_file, "w") as file:
        file.write("\n".join(input_data))

def main():
    input_file = "numbers.txt"
    output_file = "results.txt"
    
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()
        
        results = [process_line(line, i + 1) for i, line in enumerate(lines)]
        
        with open(output_file, "w") as file:
            file.write("\n".join(results))
        
        print("Results saved to 'results.txt'.")
        for result in results:
            print(result)
    except FileNotFoundError:
        print("Error: 'numbers.txt' file not found. Please provide input data.")

if __name__ == "__main__":
    user_input = ["10,20,30,17", "1,2,3,4,5"]
    save_data(user_input, "numbers.txt")
    main()