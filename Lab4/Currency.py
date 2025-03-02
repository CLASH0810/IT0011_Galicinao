import csv

def load_currency_data(file_path):
    """Load currency exchange rates from a CSV file into a dictionary."""
    currency_data = {}
    with open(file_path, newline='', encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            code, name, rate = row[0], row[1], float(row[2])
            currency_data[code.upper()] = rate
    return currency_data

def convert_currency(currency_data, currency_code, amount_in_usd):
    """Convert USD to the specified currency."""
    if currency_code.upper() not in currency_data:
        return f"Currency code '{currency_code}' not found."
    exchange_rate = currency_data[currency_code.upper()]
    converted_amount = amount_in_usd * exchange_rate
    return f"{amount_in_usd} USD is equal to {converted_amount:.2f} {currency_code.upper()}"

if __name__ == "__main__":
    file_path = r"C:\Users\galic\Desktop\python\Lab4\currency.csv"  # Update this path if needed
    currency_data = load_currency_data(file_path)
    
    usd_amount = float(input("Enter amount in USD: "))
    currency_code = input("Enter target currency code (e.g., EUR, GBP, JPY): ")
    
    result = convert_currency(currency_data, currency_code, usd_amount)
    print(result)
