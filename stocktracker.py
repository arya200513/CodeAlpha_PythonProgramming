def stock_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "AMZN": 3400,
        "MSFT": 300
    }
    
    print("Welcome to the Stock Investment Tracker!")
    print("Available stocks: " + ", ".join(stock_prices.keys()))
    print("Enter 'done' when finished.\n")

    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock symbol not recognized. Please try again.")
            continue
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty < 0:
                print("Quantity cannot be negative. Try again.")
                continue
        except ValueError:
            print("Please enter a valid integer quantity.")
            continue

        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total_investment = 0
    lines = ["Stock,Quantity,Price per Share,Total Value"]
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        lines.append(f"{stock},{qty},{price},{value}")

    print("\nPortfolio summary:")
    for line in lines:
        print(line)
    print(f"\nTotal investment value: ${total_investment}")

    # Save to CSV file
    filename = "stock_investment_summary.csv"
    with open(filename, "w") as f:
        f.write("\n".join(lines))
        f.write(f"\nTotal Investment,,,{total_investment}")

    print(f"\nSummary saved to {filename}")

if __name__ == "__main__":
    stock_tracker()

