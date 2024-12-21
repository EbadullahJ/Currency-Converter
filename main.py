def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    print("Currency Converter")
    amount = float(input("Enter amount to convert: "))
    currency_from = input("Enter the currency you are converting from (e.g., USD): ").upper()
    currency_to = input("Enter the currency you are converting to (e.g., EUR): ").upper()
    exchange_rate = float(input(f"Enter the exchange rate from {currency_from} to {currency_to}: "))
    converted_amount = convert_currency(amount, exchange_rate)
    
    print(f"{amount} {currency_from} is equal to {converted_amount:.2f} {currency_to}")

if __name__ == '__main__':
    main()
