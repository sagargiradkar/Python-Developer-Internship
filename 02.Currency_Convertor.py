from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except:
        return "Conversion failed. Please check the currency codes."

# Main currency converter loop
while True:
    print("Currency Converter")
    print("Enter 'quit' to exit")

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency you are converting from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()

    if from_currency == "QUIT":
        break

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if isinstance(converted_amount, str):
        print(converted_amount)
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
